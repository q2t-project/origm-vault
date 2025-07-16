---
title: Origm Glossary v0.3
author: Origm Project
tags: [glossary, q2t, φ-ψ-μ, fold, structure-language]
version: 0.3
---

# 🧾 Origm Glossary v0.3（語彙総拡張版）

Origmシステムの運用に実際に用いられている構造語彙を、出現頻度・分類機能・構造単位ごとに再構成した総拡張版。

---

## 1. 中核構造語彙（φ–ψ–μ／fold系）

### φ（phi）
- 構造認識軸。人間または構造体が外的対象へ向ける「命題的関心」「注視ベクトル」。分類・視点の方向性を担う。

### ψ（psi）
- 構造認識軸。内部状態の変化・知覚・感情・曖昧さなど、「意味の揺れ」や生成に関わる次元。

### μ（mu）
- 構造認識軸。意志・判断・行為の出力ベクトルを司る。構造テンションの中核を成す。

### q2t図
- 構造空間モデル。質（quality）、量（quantity）、時間（time）の三軸で構造をマッピング・視覚化する手法。

### fold
- Origmにおける構造テンプレートの最小単位。意味構造・行為構造・判断構造などを「折り」として記述する。

### fold_macro.yaml
- foldテンプレ群の分類・進化・テンションなどを統合的に記述するマクロファイル。ZettelやCanvasと連動する。

### μテンション
- foldやZettel構造における「意味の圧力」。μ軸方向の強度・傾き・変化を数値化／視覚化する評価指標。

### morphism
- fold間の意味的・構造的対応（写像）。進化・連結・変換などのプロセスを構造として記述する。

### bridge_fold
- 異なるfold_type間の意味橋渡し構造。構造的断絶や系列分岐を連結する役割をもつ。

### SimLog
- テンプレ評価と構造進化を記録するログ。1テンプレ1ログ単位でテンション変化や進化過程を追跡可能にする。

### DSL（構造記述言語）
- foldテンプレやSimLogの進化記述に用いる専用構文。@from〜@toなどの記法で進化系列を定義可能。

### AST（構文木）
- テンプレ構造の木構造展開モデル。DSL・Zettel・評価情報から自動生成され、差分比較や進化記録に用いられる。

### canvas構造
- φ–ψ–μ空間上にZettel・テンプレ・SimLogを配置した視覚マップ。Obsidian Canvas v1.5準拠で表示。

### Zettel
- Origmにおける記述単位ファイル。foldテンプレ、morphism、SimLog、語彙など構造化された知的記録群。

---

（以下のセクションは構成・分類のみで定義文未挿入）

## 2. テンプレート構造・評価・進化関連

### fold_template
- fold型の構造テンプレート本体。Zettelとして記述され、SimLogや評価テンプレと連動する。

### fold_bridge
- fold同士を意味的に連結する構造要素。系列やmorphismの橋渡し役を担う。

### template_variant
- 同一fold_type内におけるテンプレ構造のバリエーション（構造の選択肢）。

### μ_tension_eval
- μテンション評価テンプレ。構造の意味強度・圧力を定量化し、評価Zettelとして記録される。

### refutation_eval
- fold構造の仮説・判断に対する反証評価テンプレ。構造的破綻点を探る。

### evolution_trace
- foldテンプレの進化過程をDSLやSimLogで記述した系列記録。

### fold_dsl_spec
- foldテンプレの進化・構造連結を定義するDSL仕様書。

### template_refactor
- 既存foldテンプレを構造的に再設計・再構成する工程。

### template_initializer
- nullテンプレや初期構造Zettelを自動生成・初期化するユーティリティ概念。

### template_version_tag
- foldテンプレのバージョン管理ラベル（例：v0, v1）による世代識別記号。

### eval_to_dsl_mapper
- 評価テンプレZettelをDSL記述へ変換する中間変換モジュール。

## 3. Zettel分類・記録構造関連

### Zettel_f
- foldテンプレを記述するZettel（zettel/fold/ 以下に格納）。fold_typeごとに分類される。

### Zettel_s
- SimLogを記述するZettel（zettel/simlog/ 以下）。1テンプレ1ログの原則に従う。

### Zettel_m
- morphism（構造写像）に関するZettel（zettel/morph/ 以下）。進化・派生の構造対応を記述。

### null_code_zettel
- null状態を記述する初期構造Zettel。fold_type未定義や未着手テンプレに対応。

### eval_zettel
- 構造の評価・判断を記述するZettel。μテンションや構造破綻点の記録が中心。

### simlog_unit
- SimLogの最小構造単位。1テンプレ1ログの原則に則り、テンプレごとの進化・評価が記述される。

### simlog_series
- 複数のsimlog_unitを連結した進化系列。Canvas表示やテンション推移の視覚化に用いる。

## 4. UI・連携・出力構造関連

### QuickAdd_template
- Obsidian QuickAdd プラグインと連携して展開されるテンプレ単位。選択UIとの同期が可能。

### template_selector_ui
- fold_typeやμテンション分類などでテンプレ選択を可能にするUI部品。

### dataview_eval_table
- 評価テンプレ（refutation_eval, μ_tension_evalなど）のDataview一覧表示。構造評価の一覧比較に使用。

### dataviewjs_tension_graph
- μテンション推移をDataviewJSでグラフ化した出力。系列構造の評価変化を視覚的に把握できる。

### Graphviz_template_map
- foldテンプレ間の進化・派生・連結をGraphviz記法で描画する系統マップ。

### AST_diff_view
- DSLまたはZettel由来のAST構造間で差分比較を行うUI。テンプレ構造の変化点を明示。

### DSL_canvas_mapper
- fold_dsl構文とObsidian Canvas構造を相互変換するモジュール。構造テンプレの視覚・記述整合を担保する。

## 5. morphism・系列・テンション構造関連

### morphism_type
- morphism（構造写像）の分類型。強制、誘導、逆転、交換など、fold間の意味対応のパターンを記述。

### morphism_eval
- morphism構造の評価テンプレ。変換の妥当性、意味の保存度、テンションの整合性を評価する。

### morphism_bridge
- fold同士のmorphism関係を媒介する構造的接続体。系列上の意味連結や進化の分岐地点で用いられる。

### μ_tension_flow
- μテンションの時間的・構造的推移の連続体。テンプレ系列の評価変化を流れとして追跡するモデル。

### canvas_tension_map
- Obsidian Canvas上にμテンションの分布・強度・遷移をマップ化した構造図。SimLog系列と連携する。

## 6. Null構造語彙（拡張）

### init
- 初期化直後の構造状態。まだ意味・分類が付与されていない段階。

### blank
- 意図的に空白化された構造テンプレ。内容を一時的に空とする操作。

### undecided
- fold_typeや構造型が未決定の状態。構造的保留または分類未処理。

### null
- 構造が存在しない、または進化の起点としての非存在記号。

### pending
- 評価・進化が未実行である仮置き状態。処理待ちの構造ステータス。

### ghost
- 表示されない構造的存在。CanvasやAST上では不可視の仮想ノード。

### phantom
- 過去に存在した構造の痕跡。Zettelやテンプレの進化履歴にのみ現れる。

### shadow_fold
- 顕在化していないfold構造。現在のテンプレには見えないが、派生や連結に関与している。

### null_fold_template
- fold_type未定義の構造初期テンプレート。テンプレート初期化時に用いられる。

### null_dsl_entry
- DSL記述上の未定義構造位置。@from null などで使用され、進化開始点を示す。

## 7. 分岐・変化・構造制御関連語彙

### fork
- テンプレ進化の分岐点。意味の選択的展開や派生パスを記述する。

### loop
- 構造が再帰的または循環的に展開される状態。反復型進化の記述に使用。

### cascade
- 構造テンプレの連鎖的派生。複数foldが連続して展開される構造系列。

### conflict_node
- 意味的・構造的に判断不能または衝突が生じる節点。テンプレ評価で検出される。

### hybrid_fold
- 複数のfold_typeが融合・混在した構造テンプレ。構造上の再構成や連結点に現れる。

### tension_flow
- μテンションの時間的な変化と流れを表す指標。SimLogやテンプレ系列で用いられる。

### judgment_node
- 判断が構造的に下されるポイント。μテンションのピークや意味的分岐点を指す。

### pre-intentional
- 意図や判断の発生前段階。構造がまだ出力化されていないが、内部に兆しがある状態。

### ambiguity_tension
- 意味や構造の曖昧さから発生するテンション。テンプレの不確定性や二義性に関連。

### redundancy_check
- 意味構造の重複や冗長性を検出する操作。foldテンプレの最適化や再構成時に用いる。

## 8. 比較・参照語彙（準備中）
...

---

（今後、glossary_spec.md にて語彙分類原則と更新規定を管理予定）

