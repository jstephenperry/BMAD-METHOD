# Continuous Agile

[![Version](https://img.shields.io/npm/v/continuous-agile?color=blue&label=version)](https://www.npmjs.com/package/continuous-agile)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Full-lifecycle agentic development — turn an idea or change request into working software without giving up the thinking.**

Continuous Agile covers the whole effort, not only the code: what to build, how it holds together, and how it changes as you learn. It keeps what agile was always for — decisions stay explicit, context carries forward, the process sizes itself to the work — and drops the scaffolding that only existed because humans batch their coordination. There are no sprints, no velocity, and no estimates. Work flows continuously through spec folders, which are the unit of execution and the unit of handoff between teams.

Small changes go straight to build. Complex work gets the depth it needs. The same method covers a weekend prototype and a system with years of history behind it.

![The delivery loop: a vague notion starts at Clarify, a big clear idea at Plan, and a small change at Build and verify; Learn and adjust loops back to Plan](docs/images/bmad-delivery-loop.svg)

_Start anywhere. Use Continuous Agile end to end, or carry its briefs, specifications, and architecture into your existing delivery workflow._

> Continuous Agile is an independent hard fork of [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) by BMad Code, LLC, maintained separately. It is not affiliated with or endorsed by BMad Code, LLC. See [NOTICE](NOTICE).

## Start Building

**Prerequisites:** [Node.js](https://nodejs.org) 20.12+, [Python](https://www.python.org) 3.10+, and [uv](https://docs.astral.sh/uv/)

```bash
npx continuous-agile install
```

Open your project in your AI coding tool, invoke `bmad-build` with what you want to change, and keep making the decisions that matter. Run `bmad-help` whenever you want guidance on what comes next or what is optional.

**[Build your first project →](docs/tutorials/getting-started.md)**

**[Add Continuous Agile to an existing codebase →](docs/how-to/established-projects.md)**

Continuous Agile is free and open source. For prerelease builds, CI/CD, configuration overrides, and non-interactive setup, see the [installation guide](docs/how-to/install-bmad.md).

## Why Continuous Agile?

Coding assistants are effective at implementation, but they often turn unstated assumptions into code. Continuous Agile keeps you in control while its agents and workflows make the important decisions explicit and preserve them as context for the work that follows.

- **Right-sized process** — Go directly to implementation for clear changes or add deeper planning for larger initiatives.
- **New or existing code** — Start from nothing, or establish verified context on a codebase you inherited and work from what is actually there.
- **Durable context** — Carry product and technical decisions forward instead of re-explaining them in every chat.
- **Specialized perspectives** — Bring in product, architecture, UX, development, and testing expertise when it helps.
- **Guided collaboration** — Use structured workflows and multiple-agent discussions without handing over judgment.
- **One delivery path** — Move from early thinking through reviewed implementation, correction, and learning.

[See how the workflows fit together →](docs/reference/workflow-map.md)

## Modules

Install the core method, or add modules for specialized work. The add-on modules below are published by BMad Code, LLC and remain installable in Continuous Agile; they are listed here to describe compatibility, not affiliation.

| Module | Purpose |
| --- | --- |
| **Continuous Agile** (this repository) | Plan and deliver software, from new prototypes to established codebases |
| **[BMad Builder](https://github.com/bmad-code-org/bmad-builder)** | Skill, workflow, and agent builder |
| **[BMad Creative Intelligence Suite](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite)** | Creative thinking partners for innovation, design thinking, and storytelling |
| **[BMad Test Architect](https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise)** | Enterprise testing add-on |
| **[BMad Loop](https://github.com/bmad-code-org/bmad-loop)** | Builds, verifies, and retros a whole epic unattended |
| **[BMad Game Dev Studio](https://github.com/bmad-code-org/bmad-module-game-dev-studio)** | Ideate, design, and build games in any framework, including Unity, Unreal, Godot, and Phaser |

## Plan on the Web

The bundles under [`web-bundles/`](web-bundles/) package selected planning workflows as Google Gemini Gems and ChatGPT Custom GPTs. Use them for planning in your existing web subscription, then bring the resulting artifacts into your AI coding tool for implementation.

## Documentation

- **[Getting Started](docs/tutorials/getting-started.md)** — Install Continuous Agile and build a small project.
- **[Workflow Map](docs/reference/workflow-map.md)** — Understand the available paths and outputs.
- **[Established Projects](docs/how-to/established-projects.md)** — Add Continuous Agile to an existing codebase.
- **[Upgrade to V6](docs/how-to/upgrade-to-v6.md)** — Migrate from an earlier version.

## Community

- [GitHub Issues](https://github.com/jstephenperry/continuous-agile/issues) — Report bugs and request features.
- [GitHub Discussions](https://github.com/jstephenperry/continuous-agile/discussions) — Join longer conversations.

## Support and Contributing

Continuous Agile is free and open source.

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

## License

MIT License — see [LICENSE](LICENSE) for details.

**BMad** and **BMAD-METHOD** are trademarks of BMad Code, LLC. See [TRADEMARK.md](TRADEMARK.md) for details.

If you would like to contribute, read [CONTRIBUTING.md](CONTRIBUTING.md) and [CONTRIBUTORS.md](CONTRIBUTORS.md) first.
