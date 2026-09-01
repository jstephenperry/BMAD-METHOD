import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "resolve_customization.py"

sys.path.insert(0, str(SCRIPT.parent))

from resolve_customization import (  # noqa: E402
    find_project_root,
    locate_project_root,
)


class ResolveCustomizationStdoutTests(unittest.TestCase):
    def test_missing_tomllib_exits_with_actionable_version_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            scripts = Path(temp_dir)
            shutil.copy2(SCRIPT, scripts / SCRIPT.name)
            shutil.copy2(SCRIPT.parent / "config_utils.py", scripts / "config_utils.py")
            (scripts / "tomllib.py").write_text(
                'raise ModuleNotFoundError("No module named tomllib", name="tomllib")\n',
                encoding="utf-8",
            )

            result = subprocess.run(
                [sys.executable, str(scripts / SCRIPT.name), "--help"],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )

            self.assertEqual(result.returncode, 3)
            self.assertEqual(
                result.stderr,
                "error: Python 3.11+ is required (stdlib `tomllib` not found).\n",
            )
            self.assertNotIn("Traceback", result.stderr)

    def test_writes_emoji_json_when_stdout_encoding_is_cp1252(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            skill_dir = Path(temp_dir) / "emoji-agent"
            skill_dir.mkdir()
            (skill_dir / "customize.toml").write_text(
                '[agent]\nname = "Emoji Agent"\nicon = "🧭"\n',
                encoding="utf-8",
            )

            env = os.environ.copy()
            env["PYTHONIOENCODING"] = "cp1252"
            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    "--skill",
                    str(skill_dir),
                    "--key",
                    "agent",
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=temp_dir,
                env=env,
                check=False,
            )

            stderr = result.stderr.decode("utf-8", errors="replace")
            self.assertEqual(result.returncode, 0, msg=stderr)

            output = result.stdout.decode("utf-8")
            self.assertIn("🧭", output)
            resolved = json.loads(output)
            self.assertEqual(resolved["agent"]["icon"], "🧭")


class ProjectRootDiscoveryTests(unittest.TestCase):
    """A repository nearer than the install must not end the root walk.

    A `.git` between the skill directory and `_bmad/` — a vendored checkout, a
    submodule, a nested documents repository — used to resolve the root to a
    directory holding no install, which returned shipped defaults with exit 0
    and no warning.
    """

    def _require_clean_ancestry(self, path: Path) -> None:
        # The walk runs to the filesystem root, so a `_bmad/` above the temp
        # directory would satisfy it first. Skip rather than assert a layout
        # this machine does not provide.
        for ancestor in path.resolve().parents:
            if (ancestor / "_bmad").exists():
                self.skipTest(f"an ancestor of the temp dir holds _bmad/: {ancestor}")

    def _install(self, temp_dir: str) -> Path:
        root = Path(temp_dir).resolve()
        (root / "_bmad" / "custom").mkdir(parents=True)
        return root

    def _probe_skill(self, parent: Path, default: str = "DEFAULT") -> Path:
        skill_dir = parent / "probe"
        skill_dir.mkdir(parents=True)
        (skill_dir / "customize.toml").write_text(
            f'[workflow]\nname = "{default}"\n', encoding="utf-8"
        )
        return skill_dir

    def _run(self, script: Path, skill_dir: Path, cwd: Path) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(script), "--skill", str(skill_dir), "--key", "workflow"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=cwd,
            check=False,
        )

    def test_nearer_git_does_not_end_the_walk(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._install(temp_dir)
            nested = root / "nested"
            (nested / ".git").mkdir(parents=True)
            skill_dir = nested / "deep" / "probe"
            skill_dir.mkdir(parents=True)

            self.assertEqual(find_project_root(skill_dir), root)

    def test_install_reachable_from_cwd_wins_when_skill_dir_has_none(self):
        # Skills installed outside the project, in a home directory that is
        # itself a repository, must not shadow the install the agent works in.
        with tempfile.TemporaryDirectory() as temp_dir:
            base = Path(temp_dir).resolve()
            self._require_clean_ancestry(base)
            home = base / "home"
            (home / ".git").mkdir(parents=True)
            skill_dir = home / "skills" / "probe"
            skill_dir.mkdir(parents=True)
            install = base / "work" / "project"
            (install / "_bmad" / "custom").mkdir(parents=True)
            cwd = install / "_bmad-output" / "specs"
            cwd.mkdir(parents=True)

            self.assertEqual(locate_project_root(skill_dir, cwd), install)

    def test_installed_script_location_names_root_without_a_walk(self):
        # `<root>/_bmad/scripts/` is where the installer places the script, and
        # that placement alone identifies the root.
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._install(temp_dir)
            script = root / "_bmad" / "scripts" / "resolve_customization.py"
            script.parent.mkdir()
            script.touch()
            elsewhere = root / "elsewhere"
            elsewhere.mkdir()

            self.assertEqual(locate_project_root(elsewhere, elsewhere, script), root)

    def test_team_layer_survives_nested_git_end_to_end(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = self._install(temp_dir)
            nested = root / "nested"
            (nested / ".git").mkdir(parents=True)
            skill_dir = self._probe_skill(nested)
            (root / "_bmad" / "custom" / "probe.toml").write_text(
                '[workflow]\nname = "TEAM"\n', encoding="utf-8"
            )

            result = self._run(SCRIPT, skill_dir, cwd=nested)

            self.assertEqual(result.returncode, 0, msg=result.stderr.decode("utf-8", "replace"))
            resolved = json.loads(result.stdout.decode("utf-8"))
            self.assertEqual(resolved["workflow"]["name"], "TEAM")

    def test_installed_script_finds_root_when_both_walks_would_miss(self):
        # The strongest case: skill directory and working directory both sit
        # outside the install, so only the script's own placement can name it.
        with tempfile.TemporaryDirectory() as install_dir, tempfile.TemporaryDirectory() as away_dir:
            root = self._install(install_dir)
            away = Path(away_dir).resolve()
            self._require_clean_ancestry(away)
            scripts = root / "_bmad" / "scripts"
            scripts.mkdir()
            for name in ("resolve_customization.py", "config_utils.py"):
                shutil.copy(SCRIPT.parent / name, scripts / name)
            skill_dir = self._probe_skill(away)
            (root / "_bmad" / "custom" / "probe.toml").write_text(
                '[workflow]\nname = "TEAM"\n', encoding="utf-8"
            )

            result = self._run(scripts / "resolve_customization.py", skill_dir, cwd=away)

            self.assertEqual(result.returncode, 0, msg=result.stderr.decode("utf-8", "replace"))
            resolved = json.loads(result.stdout.decode("utf-8"))
            self.assertEqual(resolved["workflow"]["name"], "TEAM")

    def test_warns_on_stderr_when_no_install_is_found(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            away = Path(temp_dir).resolve()
            self._require_clean_ancestry(away)
            skill_dir = self._probe_skill(away)

            result = self._run(SCRIPT, skill_dir, cwd=away)

            self.assertEqual(result.returncode, 0)
            self.assertIn("no _bmad/ install found", result.stderr.decode("utf-8"))
            resolved = json.loads(result.stdout.decode("utf-8"))
            self.assertEqual(resolved["workflow"]["name"], "DEFAULT")


if __name__ == "__main__":
    unittest.main()
