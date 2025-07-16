---

id: fold\_abstraction

type: abstraction

label: "Abstraction（抽象）"

status: standard

phi: instance

psi: concept

mu: 0.6

tags: \[abstraction, abstract, fold, template]

---



\# Fold Abstraction Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートは「具体的な事例や事象を抽象的な概念・モデルへまとめ上げる」抽象型foldテンプレ標準雛形です。一般化・類型化・モデル構築など、思考の抽象化工程に使います。

\- \*\*主な用途\*\*:  

&nbsp; - fold\_macroやSimLogで「抽象化」「一般化」「モデル化」進化ノードを記述

&nbsp; - 具体→抽象の階層上昇、概念構造の整理

&nbsp; - テンプレ進化や意味生成の“上昇点”に



\## 構造要素



\- id: `fold\_abstraction`

\- type: `abstraction`

\- label: `"Abstraction（抽象）"`

\- phi: instance

\- psi: concept

\- mu: 0.6

\- tags: `abstraction, abstract, fold, template`

\- slots: \["具体例", "抽象化", "モデル"]



\## サンプルDSL



```dsl

@node fold\_abstraction

@label "Abstraction（抽象）"

@type abstraction

@slots

&nbsp; slot: 具体例

&nbsp; slot: 抽象化

&nbsp; slot: モデル

@phi instance

@psi concept

@mu 0.6

