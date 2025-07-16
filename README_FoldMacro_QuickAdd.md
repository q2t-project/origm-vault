# 📘 Foldテンプレート整合性管理システム（QuickAdd拡張）

Obsidian + QuickAdd + DataviewJS を使った、`fold_macro.yaml`・Canvasテンプレ・Zettel本文の **整合性保証付き自動生成ワークフロー** です。

---

## 🧩 目的

- fold_macro.yaml に **構造テンプレを登録**
- 対応する Canvas を自動生成（構造タイプ選択）
- Canvasに埋め込まれたノードから Zettel本文 を生成
- DataviewJS による整合性チェックで破綻を防止

---

## 📁 スクリプト構成

| ファイル名 | 機能 |
|------------|------|
| `fold_macro_entry_creator.js` | fold_macro.yaml へのテンプレ登録 |
| `fold_macro_canvas_creator.js` | 空Canvas + template_idノード生成 |
| `fold_macro_canvas_creator_with_nodes.js` | 構造タイプ付きCanvasノードセット生成 |
| `fold_zettel_generator_from_canvas.js` | CanvasからZettel本文（.md）生成 |
| `check_fold_macro_consistency_with_fixes.js` | 整合性チェック + 修正支援（DataviewJS） |

---

## 🛠 QuickAdd登録手順（例）

1. **QuickAdd → New Choice → Name: `Create Fold Entry`**
2. Action: `"Run Script"` → `fold_macro_entry_creator.js` を選択

同様に以下を追加：

| Name | Script |
|------|--------|
| `Create Fold Canvas` | `fold_macro_canvas_creator_with_nodes.js` |
| `Generate Fold Zettel` | `fold_zettel_generator_from_canvas.js` |

---

## 🔍 整合性チェック

`check_fold_macro_consistency_with_fixes.js` は `.md` 内で以下のように呼び出せます：

````markdown
```dataviewjs
await import("scripts/check_fold_macro_consistency_with_fixes.js")
```
````

---

## ✅ 推奨運用フロー

1. `Create Fold Entry` → macroにテンプレ登録
2. `Create Fold Canvas` → Canvasを自動生成（ノード付き）
3. Canvas編集（ノード内に内容を記入）
4. `Generate Fold Zettel` → 本文生成
5. `check_fold_macro_consistency_with_fixes.js` → 全体整合性チェック

---

整合性と再利用性を同時に確保しながら、foldテンプレートの設計〜展開を高速化できます。
