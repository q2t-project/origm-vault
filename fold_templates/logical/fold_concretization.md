```markdown

---

id: fold\_concretization

type: concretization

label: "Concretization（具体）"

status: standard

phi: concept

psi: instance

mu: 0.7

tags: \[concretization, concrete, fold, template]

---



\# Fold Concretization Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートは「抽象的な概念や理論を具体的な事例・応用に落とし込む」具体型foldテンプレ標準雛形です。現実化・適用・事例化・具体展開などに最適です。

\- \*\*主な用途\*\*:  

&nbsp; - fold\_macroやSimLogで「具体化」「事例化」「適用」ノードの記述

&nbsp; - 抽象→具体の進化、説明の現実化、実践展開

&nbsp; - 理論→事例変換や具体テンション増加の記録



\## 構造要素



\- id: `fold\_concretization`

\- type: `concretization`

\- label: `"Concretization（具体）"`

\- phi: concept

\- psi: instance

\- mu: 0.7

\- tags: `concretization, concrete, fold, template`

\- slots: \["概念", "具体化", "事例"]



\## サンプルDSL



```dsl

@node fold\_concretization

@label "Concretization（具体）"

@type concretization

@slots

&nbsp; slot: 概念

&nbsp; slot: 具体化

&nbsp; slot: 事例

@phi concept

@psi instance

@mu 0.7

