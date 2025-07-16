<!--

series\_merged\_all.dsl.md



概要: 

&nbsp; Origm Vaultにおけるfold\_macro/SimLog/DSL\_trace/initなど、主要系列を1ファイルに統合したDSLテンプレートサンプル。

&nbsp; 各@seriesセクションごとにfoldノード・SimLogテンションログ・進化系列・初期化ノードなどを記述。

用途:

&nbsp; - テンプレート生成・システム設計の全体統合例

&nbsp; - 自動生成スクリプトや構造検証のリファレンス

編集ルール:

&nbsp; - 各@seriesの用途とノードの意味は本コメントと現物ラベルで明記

&nbsp; - 系列やテンション値・ラベル命名はfold\_macroやZettel資産と常に同期

&nbsp; - サンプル拡張時は、系列間のノード重複・ID衝突に注意

&nbsp; - 必要に応じて各@series内にもDSLコメント（#や;など）可

例:

&nbsp; @series fold\_macro

&nbsp; @node F01

&nbsp; @label "構造テンプレ"

&nbsp; @type structure

&nbsp; @tension 2

-->



@series fold\_macro

@node F01
@label "構造テンプレ"
@type structure
@tension 2

@node F02
@label "反論テンプレ"
@type refutation
@tension 3

@node F03
@label "展開テンプレ"
@type expansion
@tension 4

@series simlog

@log L01
@from F01
@to F02
@tension\_delta +1
@reason "対立視点の導入による構造緊張の増加"

@log L02
@from F02
@to F03
@tension\_delta +1
@reason "要素追加によりテンションが上昇"

@series dsl\_trace

@node T0
@label "初期化テンプレ"
@type null
@tension 0
@series init

@node T1
@label "構造テンプレ"
@type structure
@tension 2
@series fold\_macro

@node T2
@label "反論テンプレ"
@type refutation
@tension 3
@series fold\_macro

@node T3
@label "展開テンプレ"
@type expansion
@tension 4
@series fold\_macro

@node T4
@label "解釈テンプレ"
@type interpretation
@tension 2
@series fold\_macro

