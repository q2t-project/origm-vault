```markdown

---

id: fold\_concession

type: concession

label: "Concession（譲歩）"

status: standard

phi: original

psi: concession

mu: 0.4

tags: \[concession, fold, compromise, template]

---



\# Fold Concession Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートは「譲歩・妥協・立場調整」を記述する譲歩型foldテンプレの雛形です。対立調整・共同点の探索・交渉進化等で利用します。

\- \*\*主な用途\*\*:  

&nbsp; - fold\_macroやSimLogで「譲歩内容」「妥協点」の構造化

&nbsp; - 合意形成、評価分岐、調整進化系列

&nbsp; - 譲歩・妥協ノードのテンプレ起点



\## 構造要素



\- id: `fold\_concession`

\- type: `concession`

\- label: `"Concession（譲歩）"`

\- phi: original

\- psi: concession

\- mu: 0.4

\- tags: `concession, fold, compromise, template`

\- slots: \["立場", "譲歩点", "合意案"]



\## サンプルDSL



```dsl

@node fold\_concession

@label "Concession（譲歩）"

@type concession

@slots

&nbsp; slot: 立場

&nbsp; slot: 譲歩点

&nbsp; slot: 合意案

@phi original

@psi concession

@mu 0.4

