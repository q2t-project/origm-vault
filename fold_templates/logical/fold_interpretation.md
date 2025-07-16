```markdown

---

id: fold\_interpretation

type: interpretation

label: "Interpretation（解釈）"

status: standard

phi: statement

psi: meaning

mu: 0.5

tags: \[interpretation, fold, template]

---



\# Fold Interpretation Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートは「ある事象・記述・データを解釈し、意味や意義を与える」解釈型foldテンプレの標準雛形です。分析・翻訳・文脈付与・意味生成などに適用できます。

\- \*\*主な用途\*\*:  

&nbsp; - fold\_macroやSimLogで「解釈」「意味付け」「分析ノード」の記録

&nbsp; - 進化系列で「解釈過程」を明示・分岐

&nbsp; - Canvas・Zettelで意味の流れや解釈テンションの可視化



\## 構造要素



\- id: `fold\_interpretation`

\- type: `interpretation`

\- label: `"Interpretation（解釈）"`

\- phi: statement

\- psi: meaning

\- mu: 0.5

\- tags: `interpretation, fold, template`

\- slots: \["記述", "解釈", "意義"]



\## サンプルDSL



```dsl

@node fold\_interpretation

@label "Interpretation（解釈）"

@type interpretation

@slots

&nbsp; slot: 記述

&nbsp; slot: 解釈

&nbsp; slot: 意義

@phi statement

@psi meaning

@mu 0.5

