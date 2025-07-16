---

id: fold\_causation

type: causation

label: "Causation（因果）"

status: standard

phi: cause

psi: effect

mu: 0.7

tags: \[causation, fold, causal, template]

---



\# Fold Causation Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートは「原因→結果」型のfoldテンプレ標準雛形です。因果推論やプロセス記述、論理的説明などあらゆる“因果構造”の基礎として使えます。

\- \*\*主な用途\*\*:  

&nbsp; - fold\_macroやSimLogで「原因・結果」の進化、テンプレ自動展開の原型

&nbsp; - 事例記述やテンプレ進化の起点、因果系列のテスト・評価

&nbsp; - 分岐・派生型への展開も容易



\## 構造要素



\- id: `fold\_causation`

\- type: `causation`

\- label: `"Causation（因果）"`

\- phi: cause

\- psi: effect

\- mu: 0.7

\- tags: `causation, fold, causal, template`

\- slots: \["原因", "結果"]



\## サンプルDSL



```dsl

@node fold\_causation

@label "Causation（因果）"

@type causation

@slots

&nbsp; slot: 原因

&nbsp; slot: 結果

@phi cause

@psi effect

@mu 0.7



