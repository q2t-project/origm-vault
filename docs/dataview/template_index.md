# 📇 foldテンプレート一覧ビュー（Dataview用）

このビューは fold_macro.yaml に定義されたテンプレート群を一覧表示し、以下の属性を確認可能にします：

- fold_type（分類）
- μテンション（テンション強度）
- μ_focus（テンション焦点語）
- 評価状態（評価済 / 未評価）
- SimLogリンク（進化記録）

---

## 📑 Dataview 表示コード（Obsidian用）

```dataview
TABLE
  fold_type,
  テンション.μ as μテンション,
  テンション.μ_focus as μ_focus,
  状態,
  評価Zettel,
  SimLog
FROM "fold_templates"
WHERE fold_type != null
SORT テンション.μ DESC
```

---

## 🔍 活用例

- μテンションが高いテンプレートを優先確認・評価
- 未評価テンプレートをフィルタし、評価Zettelを新規作成
- μ_focus 語彙の分布から語彙テンションの偏りを分析

---

## 📁 前提条件

- 各テンプレートには以下のYAMLフィールドが必要：

```yaml
fold_type: argument
テンション:
  μ: 4
  μ_focus: affect
状態: evaluated
評価Zettel: Z_eval_affect
SimLog: simlog_argument
```

