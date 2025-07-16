```markdown

---

id: fold\_assertion

type: assertion

label: "Assertion（主張）"

status: standard

phi: claim

psi: reason

mu: 0.6

tags: \[assertion, fold, claim, template]

---



\# Fold Assertion Template



\- \*\*説明\*\*:  

&nbsp; このテンプレートは「ある主張・見解・意見を述べる」主張型foldテンプレの標準雛形です。議論・意見表明・論説・説明などで基礎的に使われます。

\- \*\*主な用途\*\*:  

&nbsp; - fold\_macroやSimLogで「主張」「根拠」「展開」を構造化

&nbsp; - 対比・反証・評価ノードへの展開起点

&nbsp; - 主張系列の進化やSimLogテンション分析



\## 構造要素



\- id: `fold\_assertion`

\- type: `assertion`

\- label: `"Assertion（主張）"`

\- phi: claim

\- psi: reason

\- mu: 0.6

\- tags: `assertion, fold, claim, template`

\- slots: \["主張", "根拠", "展開"]



\## サンプルDSL



```dsl

@node fold\_assertion

@label "Assertion（主張）"

@type assertion

@slots

&nbsp; slot: 主張

&nbsp; slot: 根拠

&nbsp; slot: 展開

@phi claim

@psi reason

@mu 0.6

