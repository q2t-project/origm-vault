# simlog_mu_flow_analyzer.py
# μテンション流解析スクリプト（Phase 2 - Step ⑥）

import os
import json
import re
from pathlib import Path

# 評価Zettelディレクトリ（Z_eval_*.md）
zettel_dir = Path("zettel")
output_json = Path("data/mu_tension_flows.json")

# fold_macro データ（仮のμ値ベース）
# 本実装では fold_macro.yaml を直接参照して差分を比較する
fold_macro_mu = {
    "semantic": 4,
    "assertion": 3,
    "value": 3,
    "proposition": 3,
    "interpretation": 3,
    "affect": 4,
    "image": 4,
}

def extract_mu_tension_from_zettel(filepath):
    """Zettelファイルから μテンション値を抽出"""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"テンション: μ=([0-9]+)", content)
    if match:
        return int(match.group(1))
    return None

def main():
    flows = {}
    for file in zettel_dir.glob("Z_eval_*.md"):
        term = file.stem.replace("Z_eval_", "")
        eval_mu = extract_mu_tension_from_zettel(file)
        macro_mu = fold_macro_mu.get(term)
        if eval_mu is not None and macro_mu is not None:
            flows[term] = {
                "from_eval": eval_mu,
                "to_macro": macro_mu,
                "delta": macro_mu - eval_mu,
                "status": (
                    "上昇" if macro_mu > eval_mu
                    else "維持" if macro_mu == eval_mu
                    else "下降"
                )
            }

    output_json.parent.mkdir(exist_ok=True, parents=True)
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(flows, f, ensure_ascii=False, indent=2)
    print("✅ μテンション流を出力しました →", output_json)

if __name__ == "__main__":
    main()
