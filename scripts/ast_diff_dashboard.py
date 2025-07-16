# ast_diff_dashboard.py
# fold_macroテンプレの差分とμテンション推移をダッシュボード形式で出力

import yaml
import json
from pathlib import Path

macro_path = Path("macro/fold_macro.yaml")
json_out = Path("data/fold_macro_tension.json")

with open(macro_path, encoding="utf-8") as f:
    macro_data = yaml.safe_load(f)

# 必要項目だけ抽出
tension_summary = []
for entry in macro_data:
    fold_type = entry.get("fold_type", "?")
    μ = entry.get("テンション", {}).get("μ")
    μ_focus = entry.get("テンション", {}).get("μ_focus")
    if μ is not None:
        tension_summary.append({
            "fold_type": fold_type,
            "μ": μ,
            "μ_focus": μ_focus
        })

with open(json_out, "w", encoding="utf-8") as f:
    json.dump(tension_summary, f, ensure_ascii=False, indent=2)

print("✅ fold_macroのテンションサマリを出力 →", json_out)
