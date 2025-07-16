```markdown

---

id: fold\_placeholder

type: null

label: "Placeholder（仮置）"

status: placeholder

phi: null

psi: null

mu: 0

tags: \[null, placeholder, blank]

---



\# Fold Placeholder Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートはfoldテンプレやZettelの「後で内容・構造を決めるための一時的な仮ノード・仮エリア」を表現するための雛形です。

\- \*\*主な用途\*\*:  

&nbsp; - fold\_macro自動展開やSimLog生成時の“未決定部分”のマーカー

&nbsp; - 部分埋め、テンプレ自動生成、将来分岐予定ノードの仮置き

&nbsp; - 編集・レビュー・生成スクリプトでの“埋め待ち枠”指定



\## 構造要素



\- id: `fold\_placeholder`

\- type: `null`

\- label: `"Placeholder（仮置）"`

\- phi: null

\- psi: null

\- mu: 0

\- tags: `null, placeholder, blank`

\- slots: （なし）



\## サンプルDSL



```dsl

@node fold\_placeholder

@label "Placeholder（仮置）"

@type null

@state placeholder

@mu 0

