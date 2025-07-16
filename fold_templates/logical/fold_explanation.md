```markdown

---

id: fold\_explanation

type: explanation

label: "Explanation（説明）"

status: standard

phi: context

psi: detail

mu: 0.6

tags: \[explanation, fold, template]

---



\# Fold Explanation Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートは「事象や命題を具体的に説明・解説」する説明型foldテンプレの雛形です。分析・学習・解釈ノードとして多用途。

\- \*\*主な用途\*\*:  

&nbsp; - fold\_macroやSimLogで「説明内容」「背景」「関連事項」を記録

&nbsp; - 意味展開・学習ノード・詳細説明・進化過程の記述

&nbsp; - 分岐系列・テンション変化の“説明点”に



\## 構造要素



\- id: `fold\_explanation`

\- type: `explanation`

\- label: `"Explanation（説明）"`

\- phi: context

\- psi: detail

\- mu: 0.6

\- tags: `explanation, fold, template`

\- slots: \["説明", "背景", "詳細"]



\## サンプルDSL



```dsl

@node fold\_explanation

@label "Explanation（説明）"

@type explanation

@slots

&nbsp; slot: 説明

&nbsp; slot: 背景

&nbsp; slot: 詳細

@phi context

@psi detail

@mu 0.6

