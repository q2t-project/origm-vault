# fold_bridge_designer.py
# foldテンプレート間のBridge構造（進化・連鎖）定義・出力

import yaml
import json
from pathlib import Path

# foldテンプレBridge定義（例示）
bridge_definitions = [
    {
        "from": "null",
        "to": "assertion",
        "via": "evaluation",
        "type": "linear",
        "μ_gain": 3,
        "label": "問いの構造化（仮説化）"
    },
    {
        "from": "assertion",
        "to": "refutation",
        "via": "counter",
        "type": "branch",
        "μ_gain": 1,
        "label": "反例による評価テンプレ分岐"
    },
    {
        "from": "refutation",
        "to": "synthesis",
        "via": "reframe",
        "type": "merge",
        "μ_gain": 2,
        "label": "統合構造への接続"
    }
]

# 出力ファイル
yaml_path = Path("macro/fold_bridges.yaml")
json_path = Path("macro/fold_bridges.json")

# 保存
with open(yaml_path, "w", encoding="utf-8") as f:
    yaml.dump(bridge_definitions, f, allow_unicode=True)

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(bridge_definitions, f, ensure_ascii=False, indent=2)

print("✅ foldテンプレBridge構造を出力 →", yaml_path, json_path)
