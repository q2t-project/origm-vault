```markdown

---

id: fold\_transformation

type: transformation

label: "Transformation（転換）"

status: standard

phi: input

psi: output

mu: 0.8

tags: \[transformation, change, fold, template]

---



\# Fold Transformation Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートは「ある状態や構造が変換・転換される」転換型foldテンプレの標準雛形です。プロセス変化・進化・変形・翻訳・再解釈などに適用できます。

\- \*\*主な用途\*\*:  

&nbsp; - fold\_macroやSimLogで「状態変化」「転換」の進化系列を記述

&nbsp; - 変換点・分岐・統合ノードの可視化・記録

&nbsp; - 多段階進化やプロセス設計のテンプレ起点



\## 構造要素



\- id: `fold\_transformation`

\- type: `transformation`

\- label: `"Transformation（転換）"`

\- phi: input

\- psi: output

\- mu: 0.8

\- tags: `transformation, change, fold, template`

\- slots: \["入力", "変換処理", "出力"]



\## サンプルDSL



```dsl

@node fold\_transformation

@label "Transformation（転換）"

@type transformation

@slots

&nbsp; slot: 入力

&nbsp; slot: 変換処理

&nbsp; slot: 出力

@phi input

@psi output

@mu 0.8

