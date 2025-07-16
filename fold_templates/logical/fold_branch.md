```markdown

---

id: fold\_branch

type: branch

label: "Branch（分岐）"

status: standard

phi: decision

psi: options

mu: 0.5

tags: \[branch, fork, fold, template]

---



\# Fold Branch Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートは「一つの起点から複数の分岐・選択肢が生じる」分岐型foldテンプレの標準雛形です。論点整理・意思決定・条件分岐・多ルート進化などで利用します。

\- \*\*主な用途\*\*:  

&nbsp; - SimLogやfold\_macroで「選択肢分岐」「ルート決定」記録

&nbsp; - テンプレ進化・派生・分岐系列展開の起点

&nbsp; - 意思決定フローや論理分岐のテスト



\## 構造要素



\- id: `fold\_branch`

\- type: `branch`

\- label: `"Branch（分岐）"`

\- phi: decision

\- psi: options

\- mu: 0.5

\- tags: `branch, fork, fold, template`

\- slots: \["起点", "選択肢A", "選択肢B"]



\## サンプルDSL



```dsl

@node fold\_branch

@label "Branch（分岐）"

@type branch

@slots

&nbsp; slot: 起点

&nbsp; slot: 選択肢A

&nbsp; slot: 選択肢B

@phi decision

@psi options

@mu 0.5

