```markdown
---
id: fold_null-null
type: null
label: "Null（無）"
status: null
phi: null
psi: null
mu: 0
tags: [null, none, blank]
---

# Fold Null (none) Template

- **説明**:  
  このテンプレートはfoldテンプレ・Zettel等の「構造そのものが未生成・完全に空」であることを公式に示す純粋null型の雛形です。
- **主な用途**:  
  - fold_macro/DSL/SimLogなどの記述で“存在しないことの明示”
  - テンプレ進化・自動生成時の「非存在マーカー」
  - Canvasや進化系の“グレー表示・空白ノード”に対応

## 構造要素

- id: `fold_null-null`
- type: `null`
- label: `"Null（無）"`
- phi: null
- psi: null
- mu: 0
- tags: `null, none, blank`
- slots: （なし）

## サンプルDSL

```dsl
@node fold_null-null
@label "Null（無）"
@type null
@state null
@mu 0