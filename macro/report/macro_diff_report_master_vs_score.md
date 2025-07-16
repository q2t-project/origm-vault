# 差分レポート：fold_macro_master.yaml vs fold_macro_with_score.yaml

## 差分対象
- マスター: fold_macro_master.yaml
- 比較対象: fold_macro_with_score.yaml

## 変更概要
- テンプレート数: 36 → 38 (+2)
- 主な変化:
  - type: 'assertion' → 'evaluation'
  - slot構成の追加・変更あり
  - μテンションの調整 (例: 3.0 → 3.5)

## 影響評価
- 評価テンプレ「主張」「意味」などのテンション上昇に対応
- SimLog評価パス再生成の必要あり