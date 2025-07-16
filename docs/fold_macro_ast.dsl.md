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

@node F03
@label "展開テンプレ"
@type expansion
@ast
  slot: 前提
  slot: 補助要素
  slot: 展開先