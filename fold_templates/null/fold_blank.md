---
id: fold_blank
type: null
label: "Blank（空白）"
status: blank
phi: null
psi: null
mu: 0
tags: [null, blank]
---

# Fold Blank Template

- **説明**:  
  このテンプレートはfoldやZettelの「意図的な空白状態」（未入力・保留・後続分岐待ち等）を表現するための標準雛形です。
- **主な用途**:  
  - fold_macroやSimLogで「空欄ノード」「未設定領域」を公式化
  - テンプレ自動生成や部分埋め時の“空スロット”枠
  - 編集途中や保留ノード、暫定構造の一時格納など

## 構造要素

- id: `fold_blank`
- type: `null`
- label: `"Blank（空白）"`
- phi: null
- psi: null
- mu: 0
- tags: `null, blank`
- slots: （なし）

## サンプルDSL

```dsl
@node fold_blank
@label "Blank（空白）"
@type null
@state blank
@mu 0
