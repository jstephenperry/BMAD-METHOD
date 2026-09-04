---
title: '使用 Web Bundles'
description: 将 Continuous Agile 的 web bundle 安装为 Google Gemini Gem 或 ChatGPT Custom GPT
---

Web bundles 从仓库的 **[`web-bundles/`](https://github.com/jstephenperry/continuous-agile/tree/main/web-bundles)** 目录安装。

## 为什么只有一个入口

仓库里的 bundle 目录是架子上唯一支持的安装路径。Gemini 和 ChatGPT 演进时，步骤随代码一起更新；你拿到的 bundle 始终与所安装的版本一致。

## 要做什么

1. 在 `web-bundles/` 下选一个 bundle 子目录。
2. 打开该目录的 `INSTRUCTIONS.md`。开头分别给出 **Gemini Gem** 和 **ChatGPT GPT** 的步骤。
3. 准备好该目录里的 knowledge files（`SKILL.md` 及其数据文件）。
4. 按步骤操作：创建 Gem 或 Custom GPT，上传 knowledge files，粘贴 **PASTE BOUNDARY** 以下的 instructions 块，保存。

## 前置条件

- **Gemini Gems**：Gemini Advanced 订阅。
- **ChatGPT Custom GPTs**：Plus、Pro、Business 或 Enterprise 计划。
- 使用 **Deep Research** 的 bundle（当前是 Market & Industry Research）：在 prompt bar 启用（Tools → Deep Research）。Deep Research 有各自的 plan 限制。

## 自定义 persona

每个 bundle 的 `INSTRUCTIONS.md`（ZIP 内）在 paste boundary 上方有 **Persona Swap Example**。把已安装 instructions 里的 `[persona]` 块换成 swap 示例，即可换 voice 而不动协议。也可以从零写 persona；协议不变。

## 你会得到什么

- 一个可复用的 Gem 或 Custom GPT，scoped 到一项 Continuous Agile 规划能力。
- 打磨好的 artifact（brief、PRD、研究报告、UX spec），可直接丢进 IDE 做实现。
- 规划对话跑在现有 Web LLM 订阅上，而不是 metered IDE token。

:::caution[Persona 漂移]
Web LLM 偶尔在长会话中途掉 persona。若模型开始 out of character，提醒它的 persona 或开新会话。
:::

## 自己构建

要把现有 Continuous Agile skill 变成 web bundle，用 [bmad-utility-skills](https://github.com/bmad-code-org/bmad-utility-skills) 里的 `bmad-os-skill-to-bundle` 工具 skill。它产出 bundle 文件，persona 从所属 agent 继承，并带 swap-example 对比 voice。提交 bundle 到架子：在 [continuous-agile](https://github.com/jstephenperry/continuous-agile) 开 PR，添加 bundle 目录并在 `web-bundles/bundles.json` 里加条目。
