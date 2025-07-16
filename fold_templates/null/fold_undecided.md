```markdown

---

id: fold\_undecided

type: null

label: "Undecided（未決）"

status: undecided

phi: null

psi: null

mu: 0

tags: \[null, undecided, blank]

---



\# Fold Undecided Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートはfoldテンプレやZettelが「分岐・判断保留」「fold\_type未決定」「一時未確定」な状態を表現するための雛形です。

\- \*\*主な用途\*\*:  

&nbsp; - SimLogやテンプレ進化で「途中分岐点」や「未決状態」を記録

&nbsp; - 評価テンプレや進化系テンプレの“分岐待ち”マーカー

&nbsp; - 自動化時の選択保留や未分類ノードとして



\## 構造要素



\- id: `fold\_undecided`

\- type: `null`

\- label: `"Undecided（未決）"`

\- phi: null

\- psi: null

\- mu: 0

\- tags: `null, undecided, blank`

\- slots: （なし）



\## サンプルDSL



```dsl

@node fold\_undecided

@label "Undecided（未決）"

@type null

@state undecided

@mu 0



