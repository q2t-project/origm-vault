# gen_simlog_canvas.py
# DSLファイル群（zettel/dsl/*.dsl.md）を元に SimLog 系列Canvasを生成

import re
import json
from pathlib import Path

# 入出力ディレクトリ
dsl_dir = Path("zettel/dsl")
canvas_out = Path("canvas/simlog_series.canvas")
canvas_out.parent.mkdir(parents=True, exist_ok=True)

# ノード・エッジの生成変数
nodes = []
edges = []

x, y = 0, 0
x_offset = 300
y_offset = 150

for i, file in enumerate(sorted(dsl_dir.glob("*.dsl.md"))):
    dsl = file.read_text(encoding="utf-8")
    name = file.stem

    # DSL構文抽出
    to_match = re.search(r"@to (\w+)", dsl)
    from_match = re.search(r"@from (\w+)", dsl)
    μ_match = re.search(r"@tension μ=([0-9]+)", dsl)
    if not to_match or not from_match:
        continue

    src = from_match.group(1)
    dst = to_match.group(1)
    μ = μ_match.group(1) if μ_match else ""

    # ノード追加（toノードのみ表示）
    nid = f"node_{dst}"
    nodes.append({
        "id": nid, "type": "text", "x": x, "y": y,
        "width": 220, "height": 80, "text": f"{dst}\nμ={μ}",
        "layer": "foreground"
    })

    # エッジ（nullから派生）
    edges.append({
        "id": f"edge_null_{dst}",
        "fromNode": f"node_null", "toNode": nid,
        "label": "from null",
        "class": "simlog"
    })

    x += x_offset
    y = y_offset * (i % 2)  # ジグザグ配置

# nullノード追加
nodes.insert(0, {
    "id": "node_null", "type": "text", "x": -300, "y": 0,
    "width": 200, "height": 80, "text": "null",
    "layer": "foreground"
})

canvas_data = {"nodes": nodes, "edges": edges}
with open(canvas_out, "w", encoding="utf-8") as f:
    json.dump(canvas_data, f, ensure_ascii=False, indent=2)

print("✅ SimLog系列Canvas出力完了 →", canvas_out)
