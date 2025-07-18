# 🧭 q2t-core 構造オーバービュー

このドキュメントは、q2t-core システムにおける構造的要素の関係性を図解とともに整理したものです。

## 📌 システム全体図（v1）

以下の図は、fold_macro.yaml を中核として、テンプレート、評価Zettel、SimLog、fold DSL、Canvas構造がどのように連動しているかを示す構成図です。

![q2t-core System Overview](./q2t-core-system-overview_PUML.png)

### 🔍 主な構造ポイント

- **fold_macro.yaml**：構造定義のマスター。テンプレ、評価、進化との中心的接点。
- **Null構造**：未分類・未評価・初期状態などの明示的な構造起点。
- **foldテンプレ群（Zettel）**：φ–ψ–μ分類に対応した単位構造。
- **評価Zettel → SimLog → DSL**：テンション評価→進化記述→構造出力のパイプライン。
- **SDL命令語・コア語彙**：操作構文の基盤であり、fold_macroやテンプレ操作に接続。
- **Obsidian Canvas構造**：構造の可視化・テンション推移の表示・操作支援を担う出力装置。

---

## 🛠 今後の拡張予定

- この構成図は今後 fold DSL の進化記述と自動生成機能に応じて更新されていきます。
- 将来的には `.puml` ソースコードから自動的に図を再構成する機能を導入予定です。

➡ 最新の構造テンプレ・評価・進化の一覧は `fold_macro.yaml` および `SimLog` 系ファイルをご参照ください。
