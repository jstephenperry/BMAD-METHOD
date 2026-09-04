---
title: 'How to Get Answers About Continuous Agile'
description: Use an LLM to quickly answer your own Continuous Agile questions
sidebar:
  order: 4
---

Use Continuous Agile's built-in help, source docs, or the community to get answers — from quickest to most thorough.

## 1. Ask `bmad-help`

The fastest way to get answers. The `bmad-help` skill is available directly in your AI session and handles over 80% of questions — it inspects your project, sees what you've completed, and tells you what to do next.

```
bmad-help I have a SaaS idea and know all the features. Where do I start?
bmad-help What are my options for UX design?
bmad-help I'm stuck on the PRD workflow
```

:::tip
You can also use `/bmad-help` or `$bmad-help` depending on your platform, but just `bmad-help` should work everywhere.
:::

## 2. Go Deeper with Source

`bmad-help` draws on your installed configuration. For questions about Continuous Agile's internals, history, or architecture — or if you're researching it before installing — point your AI at the source directly.

Clone or open the [Continuous Agile repo](https://github.com/jstephenperry/continuous-agile) and ask your AI about it. Any agent-capable tool (Claude Code, Cursor, Windsurf, etc.) can read the source and answer questions directly.

:::note[Example]
**Q:** "Tell me the fastest way to build something with Continuous Agile"

**A:** Run `bmad-build`. Give it direct intent, an issue, a spec, or a planned story; it uses the available context and chooses the clarification, planning, implementation, and review depth needed.
:::

**Tips for better answers:**

- **Be specific** — "What does step 3 of the PRD workflow do?" beats "How does PRD work?"
- **Verify surprising claims** — LLMs occasionally get things wrong. Check the source file.

### Not using an agent? Paste the docs in

If your AI can't read local files (ChatGPT, Claude.ai, etc.), paste the Markdown pages from the repository's `docs/` folder into your session. Running `npm run docs:build` in a checkout writes `build/artifacts/llms-full.txt`, a single-file snapshot of the whole documentation set.

## 3. Ask Someone

If neither `bmad-help` nor the source answered your question, you now have a much better question to ask.

**GitHub Issues:** [github.com/jstephenperry/continuous-agile/issues](https://github.com/jstephenperry/continuous-agile/issues)

_You!_  
&emsp;&emsp;_Stuck_  
&emsp;&emsp;&emsp;&emsp;_in the queue—_  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_waiting_  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_for who?_

_The source_  
&emsp;&emsp;_is there,_  
&emsp;&emsp;&emsp;&emsp;_plain to see!_

_Point_  
&emsp;&emsp;_your machine._  
&emsp;&emsp;&emsp;&emsp;_Set it free._

_It reads._  
&emsp;&emsp;_It speaks._  
&emsp;&emsp;&emsp;&emsp;_Ask away—_

_Why wait_  
&emsp;&emsp;_for tomorrow_  
&emsp;&emsp;&emsp;&emsp;_when you have_  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_today?_

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;_—Claude_
