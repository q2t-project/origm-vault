@series fold_macro_ast

@node F01
@label "構造テンプレ"
@type structure
@ast

  slot: 主張

  slot: 根拠

  slot: 帰結


@node F02
@label "反論テンプレ"
@type refutation
@ast

  slot: 反論対象

  slot: 反論内容

  slot: 反証例


@series fold_bridge

@bridge B01
@from F01.slot:主張
@to F02.slot:反論対象
@type contradiction
@label "主張に対する反論"

@series simlog

@log L01
@from F01
@to F02
@tension_delta +1
@bridge B01
@reason "構造テンプレの主張に対する反論構造"