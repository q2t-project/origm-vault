<!--

simlog\_with\_bridge.dsl.md



概要:

&nbsp; SimLog系列進化ログとBridge（ノード間リンク）構造を統合的に記述したDSLテンプレート。

&nbsp; 各@seriesブロック内でノード定義（@node）、進化記録（@log）、Bridge定義（@bridge）等を組み合わせ、

&nbsp; テンプレ進化・テンション推移・系列リンクを一元化して表現する。

用途:

&nbsp; - SimLog×Bridgeパターンのサンプル／設計・自動生成スクリプトのリファレンス

&nbsp; - fold\_macro系列・テンプレ進化ロジックの統合管理・テストベンチ

編集ルール:

&nbsp; - 各@seriesごとの役割・フィールドの意味はこのコメント内で明示

&nbsp; - Bridge名・ノードID等は系列間で衝突しないよう命名規則を徹底

&nbsp; - テンション変化や進化理由などは現物@log/@bridgeブロック内に自然文で追記

&nbsp; - 必要に応じてDSL本体にもコメント（#や;等）を追加可

例:

&nbsp; @series simlog

&nbsp; @node F01

&nbsp; @log L01

&nbsp; @bridge B01

-->



@series simlog

@log L01
@from F01
@to F02
@tension\_delta +1
@bridge B01
@reason "主張に対する反論"

@log L02
@from F02
@to F03
@tension\_delta +1
@bridge B02
@reason "反証例を起点に新たな展開"

