# ZdZ_fold_dsl-guide-v1.md
バージョン: 1.0  
対象: Obsidianユーザー（テンプレートを進化管理・構造整理したい人）  
目的: fold_dsl を導入し、テンプレ1つから Canvas可視化・Zettel連携まで使えるようになる

---

## 🔷 Vault構成と思想（q2t構造原理）

fold_dslシステムは、Vault全体を **φ–ψ–μ** の空間に分けて構造化します。  
その中心思想は「テンプレ進化＝構造変化＝意味の流れ」を明示することです。

### ✅ 正式構成

```plaintext
📁 your-vault/
├── fold_macro.yaml            ← ✅ Vault全体の「テンプレ進化法則」ファイル（ψ主権）
├── _fold/                     ← ψの展開（SimLog / DSL / Canvas）
│   ├── dsl/
│   ├── simlog/
│   ├── canvas/
├── _zettel/                   ← φ空間（思考断片や節点）
│   ├── templates/
│   ├── nodes/
│   └── simflows/
├── _config/                   ← μ空間（操作スクリプトやQuickAdd）
│   └── fold_quickadd.js
```

> 🧠 `fold_macro.yaml` は「思考がどう進化するべきか」を定義する ψの法典です。  
> そのため Vault直下に置かれ、全構造を統括する地位を与えられます。

---

## 🎯 ゴール：テンプレ1つ → 表示 → 登録までやってみよう

| ステップ | 内容 |
|----------|------|
| ①        | テンプレ1個を `.md` ファイルで書く |
| ②        | `fold_macro.yaml` に登録する |
| ③        | Canvasで構造を表示する |
| ④        | QuickAddでテンプレを呼び出す |

---

## 🧪 STEP 1｜テンプレZettelを書いてみよう

**ファイル**：`_zettel/templates/eval_対照_原因.md`

```markdown
---
zettel_id: eval_対照_原因
from: 対照
to: 原因
type: 因果
morph: 推論
μ_tension: 3
axis:
  φ: 比較
  ψ: 推論
  μ: 相互作用
tags: [μ=3, logic]
note: 比較から因果への進化
---
```

---

## 🛠 STEP 2｜テンプレを `fold_macro.yaml` に登録しよう

**ファイル**：Vault直下の `fold_macro.yaml`

```yaml
- id: 対照_原因
  from: [対照]
  to: [原因]
  type: 因果
  morph: 推論
  tension: 3
  φ_axis: 比較
  ψ_axis: 推論
  μ_axis: 相互作用
  tags: [μ=3, logic]
  note: 比較から因果への進化
  label: 対照 → 原因
```

> 💡 これは「テンプレ」というより「思考のつながりの構造定義」です。

---

## 🖼 STEP 3｜Canvasに表示してみよう

**ファイル**：`_fold/canvas/fold_canvas_対照.json`

```json
{
  "nodes": [
    { "id": "対照", "x": 0, "y": 0, "type": "text", "text": "対照" },
    { "id": "原因", "x": 300, "y": 0, "type": "text", "text": "原因" }
  ],
  "edges": [
    {
      "fromNode": "対照",
      "toNode": "原因",
      "label": "推論 (μ=3)",
      "color": "#ffcc66",
      "thickness": 2.0
    }
  ]
}
```

📂 ObsidianでCanvasとして開けば、テンプレの構造が視覚化されます。

---

## ⚡ STEP 4｜QuickAddでテンプレを呼び出す（任意）

**ファイル**：`_config/fold_quickadd.js`

```javascript
const macros = [
  { id: "対照_原因", label: "対照 → 原因", tension: 3 }
];

const choice = await tp.system.suggester(
  macros.map(m => `${m.label} (μ=${m.tension})`),
  macros.map(m => m.id)
);

await tp.file.create_new(choice + ".md", "zettel_templates");
```

📎 これでテンプレを選んでZettel生成ができるようになります。

---

## 🌊 発展：SimLogで思考の流れを記述しよう

**ファイル**：`_fold/simlog/simlog_reasoning.yaml`

```yaml
simlog:
  id: reasoning_flow
  route:
    - from: 同一性
      to: 対照
      morph: 変形
      tension: 2
    - from: 対照
      to: 原因
      morph: 推論
      tension: 3
    - from: 原因
      to: 計画
      morph: 構築
      tension: 4
```

> Canvas構造で流れの強度（μテンション）を色・線太さで可視化できます。

---

## 💡 テンプレ管理の3つのコツ

1. **fold_macro.yamlはVault直下に単独で置く（ψ主権の法典）**
2. **Zettelとテンプレは分けて保管する（φ＝記録、ψ＝構造）**
3. **μテンションは思考の「負荷」や「創発」を数値化する**

---

## 🏁 おわりに

fold_dslは、あなたの思考の「つながり」「意味の流れ」「変化の構造」を  
Obsidian上で記号として残すための小さな言語です。

むずかしく見えて、やることはシンプル：

- テンプレを1つ書く  
- 1つつなげる  
- 1つ見える化する

その循環が、生きた構造をつくっていきます。
