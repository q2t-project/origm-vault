---

id: fold\_proposition

type: proposition

label: "Proposition（命題）"

status: standard

phi: statement

psi: assertion

mu: 0.5

tags: \[proposition, fold, statement, template]

---



\# Fold Proposition Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートは「ある命題・命令・判断を公式に提示する」命題型foldテンプレの標準雛形です。議論・説明・論証などあらゆる論理展開の基本となる“主張の提示”に適します。

\- \*\*主な用途\*\*:  

&nbsp; - fold\_macroやSimLogで「命題」「論点」「宣言」を記述

&nbsp; - 主張／反証／評価の起点や分岐系列の展開

&nbsp; - SimLog進化の基礎単位として



\## 構造要素



\- id: `fold\_proposition`

\- type: `proposition`

\- label: `"Proposition（命題）"`

\- phi: statement

\- psi: assertion

\- mu: 0.5

\- tags: `proposition, fold, statement, template`

\- slots: \["命題", "裏付け", "帰結"]



\## サンプルDSL



```dsl

@node fold\_proposition

@label "Proposition（命題）"

@type proposition

@slots

&nbsp; slot: 命題

&nbsp; slot: 裏付け

&nbsp; slot: 帰結

@phi statement

@psi assertion

@mu 0.5

