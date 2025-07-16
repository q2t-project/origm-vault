# git_canvas_sync.py
# Git履歴からテンプレ構造の差分を抽出しCanvas構造に変換

import subprocess
import json
from pathlib import Path

macro_path = Path("macro/fold_macro.yaml")
canvas_out = Path("canvas/git_macro_diff.canvas")

# Gitログ取得コマンド
log_cmd = ["git", "log", "-p", "--", str(macro_path)]
result = subprocess.run(log_cmd, capture_output=True, text=True)
log_text = result.stdout

# 差分から fold_type 単位の変化を抽出（簡易版）
import re
fold_diffs = {}
current_commit = ""

for line in log_text.splitlines():
    if line.startswith("commit"):
        current_commit = line.split()[1][:7]
    if line.startswith("+fold_type:"):
        t = line.strip().split(":")[-1].strip()
        fold_diffs.setdefault(t, []).append({"commit": current_commit, "change": "+"})
    elif line.startswith("-fold_type:"):
        t = line.strip().split(":")[-1].strip()
        fold_diffs.setdefault(t, []).append({"commit": current_commit, "change": "-"})

# Canvas構造化（時間軸上に配置）
nodes = []
edges = []
offset_x = 300

for idx, (ftype, changes) in enumerate(fold_diffs.items()):
    x = idx * offset_x
    for j, change in enumerate(changes):
        y = j * 100
        label = f"{ftype} ({change['change']} {change['commit']})"
        nid = f"{ftype}_{j}"
        nodes.append({
            "id": nid, "type": "text", "x": x, "y": y,
            "width": 220, "height": 80, "text": label,
            "layer": "foreground"
        })
        if j > 0:
            edges.append({
                "id": f"edge_{ftype}_{j}",
                "fromNode": f"{ftype}_{j-1}", "toNode": nid,
                "label": "進化",
                "class": "history"
            })

canvas_data = {"nodes": nodes, "edges": edges}
canvas_out.parent.mkdir(parents=True, exist_ok=True)
with open(canvas_out, "w", encoding="utf-8") as f:
    json.dump(canvas_data, f, ensure_ascii=False, indent=2)

print("✅ Git差分Canvas出力完了 →", canvas_out)
