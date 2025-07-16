```markdown

---

id: fold\_eval

type: eval

label: "Evaluation（評価）"

status: standard

phi: criterion

psi: object

mu: 0.6

tags: \[evaluation, eval, fold, template]

---



\# Fold Evaluation Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートは「基準に基づいて対象を評価する」評価型foldテンプレの雛形です。判定・審査・採点・レビューなど多様な評価プロセスを構造化します。

\- \*\*主な用途\*\*:  

&nbsp; - fold\_macroやSimLogで「評価点・観点」の記録

&nbsp; - テンプレ進化や分岐（評価基準による流れ変化）実験

&nbsp; - 評価テンプレ/SimLog/Canvasなど多用



\## 構造要素



\- id: `fold\_eval`

\- type: `eval`

\- label: `"Evaluation（評価）"`

\- phi: criterion

\- psi: object

\- mu: 0.6

\- tags: `evaluation, eval, fold, template`

\- slots: \["評価観点", "評価対象", "評価結果"]



\## サンプルDSL



```dsl

@node fold\_eval

@label "Evaluation（評価）"

@type eval

@slots

&nbsp; slot: 評価観点

&nbsp; slot: 評価対象

&nbsp; slot: 評価結果

@phi criterion

@psi object

@mu 0.6

