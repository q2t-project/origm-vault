# 🧪 Zettel生成チュートリアル：null → DSL → Canvas のステップ実践

このチュートリアルでは、q2tシステムにおいて Zettel を構造的に生成・評価・可視化する一連のステップを案内します。

---

## 📍 Step 1. Nullテンプレから始める

- **目的**：構造が未定義（null/init）であるZettelの起点を明示
- **実施**：`fold_type: null` のテンプレートを新規作成し、必要最小限の命令語で構成

```markdown
---
title: 新しいZettel案（null型）
fold_type: null
状態: init
---

ここに初期の構造的な問いや断片を書き始めます。
```

---

## ⚙️ Step 2. 評価テンプレでテンションを付加

- **目的**：構造が持つ意味テンション（μ）を定量化
- **実施**：`Z_eval_*.md` を生成し、foldテンプレに対する評価項目を記入

```markdown
---
title: 評価テンプレ：affect
語彙: affect
テンション: μ=5
---

この語彙はテンション起因の評価構造に強く関与する。
```

---

## 🧩 Step 3. DSLブロックへ変換する

- **目的**：評価Zettelやnull構造を fold DSL として進化記述
- **実施**：`@from null` → `@to affect` のような進化ブロックを記述

```dsl
@from null
@to affect
@reason テンション評価により構造的意味が強化されたため
```

---

## 🗺️ Step 4. Canvasで可視化する

- **目的**：評価→進化→構造の流れを Obsidian Canvas で俯瞰
- **実施**：テンション付きCanvas（例：`mu_tension_flow.canvas`）でノードと線の流れを確認

---

## ✅ 終了後の出力物一覧

| 種類       | ファイル                     | 説明                |
| -------- | ------------------------ | ----------------- |
| Nullテンプレ | `Z_null_*.md`            | 構造未定の初期ノード        |
| 評価Zettel | `Z_eval_*.md`            | μテンションの評価付きZettel |
| DSL構文    | `@from null → @to X`     | 評価からの進化記述         |
| Canvas   | `mu_tension_flow.canvas` | テンションの進化を視覚化      |

