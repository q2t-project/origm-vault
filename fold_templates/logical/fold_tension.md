```markdown

---

id: fold\_tension

type: tension

label: "Tension（テンション）"

status: special

phi: null

psi: null

mu: 1.0

tags: \[tension, fold, template]

---



\# Fold Tension Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートは「テンション（μ値）そのものの強度や変化を明示する」テンション型foldテンプレです。進化記録、テンション可視化、分岐の“張力点”などに最適。

\- \*\*主な用途\*\*:  

&nbsp; - SimLog/Canvas等でテンション変化のみを表現するノード

&nbsp; - μ変化の境界点やテンション評価の“マーカー”

&nbsp; - テンション・緊張度分析の基準



\## 構造要素



\- id: `fold\_tension`

\- type: `tension`

\- label: `"Tension（テンション）"`

\- phi: null

\- psi: null

\- mu: 1.0

\- tags: `tension, fold, template`

\- slots: \["テンション値"]



\## サンプルDSL



```dsl

@node fold\_tension

@label "Tension（テンション）"

@type tension

@slots

&nbsp; slot: テンション値

@mu 1.0

