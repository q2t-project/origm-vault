# SDL語彙辞書 v1

## 🧠 コア語彙（φψμ分類）

| 英語 | 日本語 | φψμ | 定義 | 使用場面 | source |
|------|--------|-----|------|----------|--------|
| structure | 構造 | φ | q2tシステムにおいて、foldテンプレート・Zettel・DSLなどの内部で、要素同士の接続関係や配置パターンを統御する枠組み。テンション流の流路・分岐・接続・発生源などを構造的に規定する。 | fold_macro, template_core, DSL | Z001_core, fold/構造テンプレ |
| operation | 操作 | ψ | q2tにおける構造変化や意味生成に対する能動的な行為単位。foldテンプレの変化構文、Zettelの接続・分岐操作、DSLにおける命令的トークンなど、構造を動的に推移させる要素全般を指す。 | fold_macro, template_dynamics, DSL | Z010_operation, fold/操作テンプレ |
| semantic | 意味 | μ | q2tにおいて構造・文脈・テンプレ進化によって動的に生成される意味層。Zettelの主張が立ち上がる際の含意、foldテンプレの選択肢に潜在する意味の流れ、DSL構文の背後に暗在化する意味生成の場を含む。 | fold_macro, Zettel, evaluation, DSL | Z100_meaning, fold/意味テンプレ |
| logic | 論理 | φ | q2tにおける構造的記述の整合性や接続可能性を制御する形式層。foldテンプレにおける接続規則や、Zettel構造の展開順序、DSL構文の妥当性条件などに現れる。 | fold_macro, template_structure, DSL | Z002_logic, fold/論理テンプレ |
| assertion | 命題 | ψ | Zettelやテンプレ内で構造的に提示される主張・断定・仮説などの意味単位。評価の対象となり、foldの分岐やテンション変化を引き起こす。形式的整合性（logic）とは異なり、内容の可否・選択が問われる。 | Zettel, evaluation, fold_macro | Z020_assert, fold/命題テンプレ |
| value | 値 | μ | Zettelやfoldテンプレにおいて、意味的・評価的・量的な要素として構造内部に位置づけられる変数的単位。テンションの数値化、意味要素のスカラー的評価、DSL構文における属性値などに現れる。 | evaluation, template_evaluation, DSL | Z300_value, fold/評価テンプレ |
| symbol | 記号 | φ | 構造や意味の抽象的な指標として用いられる視覚・音声・文字などの表層表現。Zettelやテンプレ内での識別子、DSL構文のトークン、構造タグや記述単位として使われる。 | DSL, template_label, fold_macro | Z011_symbol, fold/記号テンプレ |
| proposition | 主張 | ψ | Zettelやテンプレ内で構造化された言語表現として明示的に提示される主張文。`assertion`がテンプレ的・構造的な命題単位であるのに対し、`proposition`は自然言語的表現として現れる主張そのものを指す。 | Zettel, output_surface, evaluation | Z021_proposition, fold/主張テンプレ |
| interpretation | 解釈 | μ | 構造・文脈・テンションなどから派生する意味の読み取り過程。Zettel間の接続によって生まれる意味の連鎖や、foldテンプレの選択結果として現れる意味の揺らぎ、DSL構文の含意の取り出しなどに現れる。 | Zettel, fold_macro, evaluation, DSL | Z110_interpret, fold/解釈テンプレ |
| rule | 規則 | φ | 構造記述・進化過程・意味生成において、foldやDSL、Zettelの構造が従うべき制約条件や判断基準の集合。形式的整合性・型制約・評価条件などがこれに該当する。 | fold_macro, DSL, evaluation | Z005_rule, fold/規則テンプレ |
| gesture | 動作 | ψ | 言語化されないまま構造や意味生成に影響を与える直感的・身体的な操作。foldテンプレの選択、Zettelの接続順序、テンション判断などにおける無意識的・即時的な振る舞いとして現れる。 | Zettel, template_selection, evaluation | Z070_gesture, fold/動作テンプレ |
| affect | 情動 | μ | 構造評価やテンション変化の深層に影響を及ぼす感情的・感覚的な動因。Zettelの意味判断、foldテンプレの選好、テンションの上昇・下降の起点として無意識的に作用する。 | evaluation, Zettel, fold_macro | Z200_affect, fold/情動テンプレ |
| formula | 式 | φ | 構造的・記号的関係を明示する形式的な記述単位。foldテンプレの条件指定、DSL構文のルール定義、Zettel内の意味生成ルールなどにおいて構文や関係式として現れる。 | DSL, fold_macro, Zettel | Z300_formula, fold/式テンプレ |
| question | 問い | ψ | fold展開・Zettel連鎖・評価過程の出発点として発せられる探索的構造。未決断状態を発火させ、テンプレ分岐やテンション変化を促す構造的起点として働く。 | Zettel, evaluation, template_branch | Z090_question, fold/問いテンプレ |
| image | 像 | μ | 意味や構造を感覚的に捉えるための内的表象。Zettelの直観的把握、テンプレの意味的連想、構造タグに対する視覚的・感情的な印象など、q2tの深層で意味を支える非言語的支柱。 | Zettel, fold_macro, template_design | Z400_image, fold/像テンプレ |

## 🛠 命令語（SDL構文操作）

| 英語 | 日本語 | 定義 | 使用場面 | source |
|------|--------|------|----------|--------|
| node | 節点 | foldテンプレやDSL構文において、構造の最小単位を構成するノード。Zettelや構造記述において意味や操作の中心となる単位。 | fold_macro, DSL, Zettel | fold/節点テンプレ |
| connect | 接続 | 構造要素間の関係性を明示する操作。ノード同士の意味的・構造的な関連付け、foldテンプレの流れ、Zettel間の論理的リンクなどを構成する。 | fold_macro, DSL, Canvas構造 | fold/接続テンプレ |
| attribute | 属性 | 構造要素に対して意味や状態に関する補助的な情報を付加する操作。Zettelやノードに対するタグ付け、テンプレの分類補足、DSLでのプロパティ設定などに用いられる。 | fold_macro, DSL, Zettel | fold/属性テンプレ |
| semantic | 意味 | 構造要素と意味層を接続する操作。foldテンプレやZettelが持つ意味的意図を構造内に組み込む際、またDSLにおける語彙の意味分類やテンション評価の際に用いられる。 | fold_macro, evaluation, DSL | fold/意味接続テンプレ |
| state | 状態 | 構造要素が現在どの段階・モード・テンションにあるかを記述・制御する操作。foldテンプレの確定・未定、Zettelの編集状態、テンションの進行度などを管理する。 | fold_macro, evaluation, SimLog | fold/状態テンプレ |
| type | 型 | foldテンプレや構造要素に対して、分類・機能・意味的役割を割り当てるための操作。fold_type、Zettelの分類ラベル、テンプレ系列の定義付けなどで使われる。 | fold_macro, DSL, template_class | fold/型テンプレ |
| branch | 分岐 | 構造や意味の選択肢を展開する操作。foldテンプレにおける可変パターンの提示、Zettelの多義的進行、DSLにおける分岐制御などに使われる。 | fold_macro, DSL, evaluation | fold/分岐テンプレ |
| annotation | 注釈 | 構造要素に対して補足情報・背景文脈・コメントなどを加える操作。foldテンプレやZettel、DSLの構成要素に対して明示的なメタ情報を与える。 | Zettel, fold_macro, DSL | fold/注釈テンプレ |
| change | 変化 | 構造や意味の状態を意図的に更新・変形させる操作。foldテンプレの進化、テンション推移、Zettel間の意味転位などを引き起こす行為。 | fold_macro, SimLog, evaluation | fold/変化テンプレ |
| label | ラベル | 構造要素に識別名や視覚的表記を与える操作。Zettelやノードに付加される記号的名称であり、構造認識・分類・表示制御の補助となる。 | Zettel, DSL, template_label | fold/ラベルテンプレ |
| expand | 展開 | テンプレートや構造記述のスコープを展開・複製・分岐させる操作。foldテンプレの継承展開、DSLによるマクロ展開、Zettelの派生構造の生成などに使われる。 | fold_macro, DSL, template_inheritance | fold/展開テンプレ |
| include | 包含 | 構造要素やスコープを他の構造内部に組み込む操作。foldテンプレのネスト、Zettel内ブロックの包含、DSLでのテンプレ再利用指定などに用いられる。 | fold_macro, DSL, template_embed | fold/包含テンプレ |
| exclude | 除外 | 構造から特定の要素や属性を意図的に取り除く操作。foldテンプレの削除条件、DSLでの無視指定、Zettel内の枝刈り処理などに用いられる。 | fold_macro, DSL, evaluation | fold/除外テンプレ |
| map | 対応付け | 構造要素間または語彙・型・意味タグ間の関係を対応づける操作。fold_macroでの分類タグ付与、DSLでの語彙分類、構造タグ同士の整合処理などに用いられる。 | fold_macro, DSL, classification | fold/対応テンプレ |

## 🌫 null語彙バリアント

| タグ | 表記 | 定義 | 使用場面 | source |
|------|------|------|----------|--------|
| init | 初期化 | foldテンプレやZettelが生成直後でまだ構造・型・意味が確定していない状態。意味テンション=0であり、進化の出発点を明示する。 | fold_macro, evaluation, SimLog, DSL | fold/null-init, Z000_init |
| blank | 空白 | 構造的に意味や型をあえて未設定とし、保留・開放状態を保つための意図的な空欄。後続の編集やテンプレ分岐の余地として用いられる。 | fold_macro, Zettel, template_seed | fold/null-blank, Z000_blank |
| undecided | 未決 | 構造や意味が途中段階で分岐・判断待ちとなっている状態。fold_typeの未決定、評価テンプレの未確定項目、テンション分岐における選択保留などを含む。 | fold_macro, evaluation, DSL | fold/null-undecided, Z000_undecided |
| null | 無 | 構造そのものが未生成・不在であることを示す状態。fold_macroやテンプレDSLの記述において、構造的に存在しないことを明示する。SimLogやCanvasではグレーで可視化される。 | fold_macro, DSL, SimLog, Canvas構造 | fold/null-null, Z000_null |
| placeholder | 仮置 | 後から意味・構造を与える前提で一時的に配置された仮ノード・仮要素。foldテンプレの部分埋めやテンプレ自動生成時の空スロットに用いられる。 | fold_macro, template_seed, DSL | fold/null-placeholder, Z000_placeholder |
| detached | 分離 | 本来接続されていた構造から切り離され、独立・孤立した状態。Zettelのリンク切れ、foldテンプレの破断、DSL構文の参照漏れなどに該当する。 | fold_macro, DSL, Canvas構造 | fold/null-detached, Z000_detached |
| obsolete | 廃棄 | かつて意味や機能を持っていたが、現在では無効・不要となった構造状態。テンプレ進化後の旧構造、Zettelの脱リンク化要素などが該当する。 | fold_macro, SimLog, Canvas構造 | fold/null-obsolete, Z000_obsolete |