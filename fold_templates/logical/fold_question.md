---

id: fold\_question

type: question

label: "Question（質問）"

status: standard

phi: inquirer

psi: topic

mu: 0.3

tags: \[question, inquiry, fold, template]

---



\# Fold Question Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートは「問いかけ・情報要求・論点提示」の質問型foldテンプレ標準雛形です。議論開始・探索・分岐の起点などに最適です。

\- \*\*主な用途\*\*:  

&nbsp; - fold\_macroやSimLogで「質問」「論点提示」「課題提起」を記録

&nbsp; - 分岐進化の起点ノードやSimLogでの分岐点マーカー

&nbsp; - Q\&A構造、議論整理



\## 構造要素



\- id: `fold\_question`

\- type: `question`

\- label: `"Question（質問）"`

\- phi: inquirer

\- psi: topic

\- mu: 0.3

\- tags: `question, inquiry, fold, template`

\- slots: \["質問", "背景", "回答候補"]



\## サンプルDSL



```dsl

@node fold\_question

@label "Question（質問）"

@type question

@slots

&nbsp; slot: 質問

&nbsp; slot: 背景

&nbsp; slot: 回答候補

@phi inquirer

@psi topic

@mu 0.3

