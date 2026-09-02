# Finalize: Retrospective Document

Phase 5. Finalize the retrospective document — the run's only write.

## The retrospective document

This document is the run's working artifact: it is created as a skeleton once the epic is fixed and filled as each phase completes, so Phase 5 finalizes rather than writes it from scratch. It lives at `{spec-folder}/RETROSPECTIVE.md` — a fixed name, so a resumed run finds it — in `{document_output_language}`, as readable markdown; the folder names the epic.

Open the document with YAML frontmatter a machine can read without parsing the prose — an epic gate or orchestrator keys off `verdict` to decide whether to hold the next epic:

```
---
date: {date}
verdict: accepted | accepted-with-open-items | rejected
criteria: declared | profiled
headless: true | false
---
```

Keep `verdict` in sync with the Acceptance verdict section below. Nothing else records the verdict — this skill never edits `SPEC.md`, `stories.yaml`, or a story artifact — so a gate or orchestrator that acts on it **must** read this document's frontmatter. That holds for a **rejected** epic too: the document exists whichever way the verdict went, because its presence means *the retrospective ran*, not *the epic passed*.

Sections:

- **Epic summary** — which spec folder, the diff ranges, stories completed, any stories still unfinished (`pending_stories`) that the user accepted retro-ing over, the evidence inventory (what was available, what was missing). Unfinished stories force the machine acceptance verdict to **rejected** (see `references/acceptance-verdict.md`).
- **Findings** — grouped by aggregate view and by lens, each with its source reference and disposition (fix now / defer / accept). This is the record; do not summarize away the provenance.
- **Behavior verification** — what was exercised end to end and what was observed, or an explicit note that runtime behavior was not exercised.
- **Previous-retro follow-through** — if prior retros exist, whether their action items landed, with evidence, and the status each argues for (`references/acceptance-verdict.md` specifies what to record).
- **Action items** — the routed fix-now items and process lessons, each with an owner. Note which are proposed remediation or spec reconciliations awaiting human application.
- **Acceptance verdict** — accepted / accepted-with-open-items / rejected, whether the criteria were declared or profiled, and the evidence behind the call.
- **Open questions** — what a human answer would materially change, and anything the analyses could not resolve.
- **Assumptions** — in headless runs, every choice made without the user: which spec folder was selected, any non-empty `pending_stories` proceeded over, a machine **rejected** verdict forced by unfinished stories or rendered with no human decision, each proposed item. Omit in interactive runs — an interactive run records the same facts where the user confirmed them, in Epic summary.

Do not state time estimates anywhere in the document.

## Finish

Report where the document was saved, the verdict, and the action-item count. Then, if `{workflow.on_complete}` is non-empty, follow it as the final terminal instruction before exiting.
