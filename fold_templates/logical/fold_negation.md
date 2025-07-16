```markdown

---

id: fold\_negation

type: negation

label: "Negation（否定）"

status: standard

phi: target

psi: reason

mu: 0.2

tags: \[negation, contradiction, fold, template]

---



\# Fold Negation Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートは「否定・反証・異議申し立て」を表現する否定型foldテンプレの標準雛形です。対立・反論・矛盾進化の記録に活用します。

\- \*\*主な用途\*\*:  

&nbsp; - fold\_macroやSimLogで「否定対象」「否定理由」の構造化

&nbsp; - 対立系列やSimLog進化での矛盾点記録

&nbsp; - 反論ノード、評価分岐



\## 構造要素



\- id: `fold\_negation`

\- type: `negation`

\- label: `"Negation（否定）"`

\- phi: target

\- psi: reason

\- mu: 0.2

\- tags: `negation, contradiction, fold, template`

\- slots: \["否定対象", "否定理由", "反証例"]



\## サンプルDSL



```dsl

@node fold\_negation

@label "Negation（否定）"

@type negation

@slots

&nbsp; slot: 否定対象

&nbsp; slot: 否定理由

&nbsp; slot: 反証例

@phi target

@psi reason

@mu 0.2

