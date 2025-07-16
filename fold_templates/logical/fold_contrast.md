---

id: fold\_contrast

type: contrast

label: "Contrast（対比）"

status: standard

phi: side\_a

psi: side\_b

mu: 0.4

tags: \[contrast, comparison, fold, template]

---



\# Fold Contrast Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートは「二つ以上の対象や立場を比較・対比する」対比型foldテンプレの標準雛形です。比較検討・差異分析・二項対立の整理などに適用できます。

\- \*\*主な用途\*\*:  

&nbsp; - fold\_macroやSimLogで「比較対象A/B」「共通点・差異」などの記述

&nbsp; - 対比進化・差異テンション分析・系列分岐の起点

&nbsp; - 議論・分析・レビューなどあらゆる比較構造で活用



\## 構造要素



\- id: `fold\_contrast`

\- type: `contrast`

\- label: `"Contrast（対比）"`

\- phi: side\_a

\- psi: side\_b

\- mu: 0.4

\- tags: `contrast, comparison, fold, template`

\- slots: \["対象A", "対象B", "比較軸"]



\## サンプルDSL



```dsl

@node fold\_contrast

@label "Contrast（対比）"

@type contrast

@slots

&nbsp; slot: 対象A

&nbsp; slot: 対象B

&nbsp; slot: 比較軸

@phi side\_a

@psi side\_b

@mu 0.4

