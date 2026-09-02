/**
 * Config Regime Guard
 *
 * Fails if any SKILL.md under src/ still reads the retired per-module YAML
 * config (`_bmad/<module>/config.yaml` or `config.user.yaml`). Skills resolve
 * central config through `_bmad/scripts/resolve_config.py` — the four-layer
 * TOML merge — so a team or personal pin in `_bmad/custom/` reaches every
 * skill. A YAML reference is a skill that pin can never reach.
 *
 * Usage: node test/test-config-regime.js
 * Exit codes: 0 = no violations, 1 = violations found
 */

const fs = require('node:fs');
const path = require('node:path');

// ANSI color codes
const colors = {
  reset: '[0m',
  green: '[32m',
  red: '[31m',
  cyan: '[36m',
  dim: '[2m',
};

const SRC_DIR = path.join(__dirname, '..', 'src');

// Directories exempt from the guard. Empty since the sprint-mode and v6-shim
// removal deleted the last skills that read a per-module config.yaml.
const EXCLUDED_DIRS = [];

const FORBIDDEN = /config(?:\.user)?\.yaml/;

/**
 * Recursively collect every SKILL.md under `dir`.
 * @param {string} dir - Absolute directory to walk.
 * @param {string[]} found - Accumulator of absolute SKILL.md paths.
 * @returns {string[]} The accumulator.
 */
function collectSkillFiles(dir, found = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      collectSkillFiles(fullPath, found);
    } else if (entry.name === 'SKILL.md') {
      found.push(fullPath);
    }
  }
  return found;
}

/**
 * Whether a src-relative path sits under one of the excluded directories.
 * @param {string} relativePath - Path relative to src/, posix separators.
 * @returns {boolean} True if excluded.
 */
function isExcluded(relativePath) {
  return EXCLUDED_DIRS.some((prefix) => relativePath.startsWith(prefix));
}

console.log(`\n${colors.cyan}Config Regime Guard — no SKILL.md reads _bmad/<module>/config.yaml${colors.reset}\n`);

const violations = [];
let scanned = 0;
let excluded = 0;

for (const fullPath of collectSkillFiles(SRC_DIR).sort()) {
  const relativePath = path.relative(SRC_DIR, fullPath).split(path.sep).join('/');
  if (isExcluded(relativePath)) {
    excluded++;
    continue;
  }
  scanned++;
  const lines = fs.readFileSync(fullPath, 'utf8').split('\n');
  for (const [index, line] of lines.entries()) {
    if (FORBIDDEN.test(line)) {
      violations.push({ file: `src/${relativePath}`, line: index + 1, text: line.trim() });
    }
  }
}

console.log(`  Scanned: ${scanned} SKILL.md files ${colors.dim}(${excluded} excluded)${colors.reset}`);

// --- Summary ---
console.log(`\n${colors.cyan}${'═'.repeat(55)}${colors.reset}`);
console.log(`${colors.cyan}Test Results:${colors.reset}`);
console.log(`  Violations: ${violations.length === 0 ? colors.green : colors.red}${violations.length}${colors.reset}`);
console.log(`${colors.cyan}${'═'.repeat(55)}${colors.reset}\n`);

if (violations.length > 0) {
  console.log(`${colors.red}SKILL.md files still reading the retired YAML config:${colors.reset}\n`);
  for (const violation of violations) {
    console.log(`${colors.red}✗${colors.reset} ${violation.file}:${violation.line}`);
    console.log(`  ${colors.dim}${violation.text}${colors.reset}\n`);
  }
  console.log('Replace the read with `uv run {project-root}/_bmad/scripts/resolve_config.py --project-root {project-root}`.\n');
  process.exit(1);
}

console.log(`${colors.green}All tests passed!${colors.reset}\n`);
process.exit(0);
