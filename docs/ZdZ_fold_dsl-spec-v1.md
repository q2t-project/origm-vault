# ZdZ_fold_dsl-spec-v1.md
バージョン: 1.0

## DSL命令語一覧

| 命令語 | 説明 |
|--------|------|
| `@from` | 出発ノード（構造の始点） |
| `@to` | 到達ノード（構造の終点） |
| `@type` | テンプレの分類種（例：planning, causation） |
| `@morph` | 意味変換の種類（例：inference, transform） |
| `@tension` | μテンション（変化の抵抗・創発負荷） |
| `@note` | 任意の説明文（人間が読むため） |

## AST対応表

各命令語は fold_macro.yaml に次のように対応：

| DSL命令語 | YAMLキー |
|-----------|----------|
| `@from` | `from` |
| `@to` | `to` |
| `@type` | `type` |
| `@morph` | `morph` |
| `@tension` | `tension` |
| `@note` | `note` |

## DSL構文例

```plaintext
@from contrast
@to cause
@type causation
@morph inference
@tension 3
@note: 比較から因果への進化
