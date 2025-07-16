<!--
@zettel_type: simlog_eval
@description: SimLogに基づく進化評価Zettel。@from〜@toでテンプレートの進化とテンション変化を記録。
-->

@series fold_macro_ast
@node F01
@label "構造テンプレ"
@type structure
@tension 2
@ast
  slot: 主張
  slot: 根拠
  slot: 帰結

@series fold_bridge
@bridge B_F01_F02
@from F01.slot:主張
@to F02.slot:反論対象
@type contradiction
@label "主張に対する反論"

@series simlog
@log L_F01_F02
@from F01
@to F02
@tension_delta +1
@bridge B_F01_F02
@reason "主張に対する反論"