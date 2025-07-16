---
id: fold_null
type: null
label: "Null（未定義）"
status: init
phi: null
psi: null
mu: 0
tags: [null, blank, undecided, placeholder]
---

# Fold Null Template

- **説明**:  
  このテンプレートはfoldテンプレ・Zettelなどあらゆる系列の「未定義」「初期化」「空白」「仮置」状態を公式に表現するための雛形です。
- **主な用途**:  
  - fold_macro・SimLog・DSL・Canvas等で「nullノード」「初期化ノード」として起点・空白領域・未定義状態を明示
  - 評価未着手・進化起点・構造分岐待ち等の一時保留枠
  - テンプレ進化記録や自動化パイプラインの“nullテンプレ”として

## 構造要素

- id: `fold_null`
- type: `null`
- label: `"Null（未定義）"`
- phi: null
- psi: null
- mu: 0
- tags: `null, blank, undecided, placeholder`
- slots: （なし、または["未定義"]）

## サンプルDSL

```dsl
@node fold_null
@label "Null（未定義）"
@type null
@phi null
@psi null
@mu 0
@state init
備考
必要に応じて、init, blank, undecided, placeholder など他のnull派生型も別ファイルで雛形化。

fold_macro.yaml・DSLテンプレ生成・SimLog進化起点などで「未定義」領域が必要な時に本ファイルを参照。