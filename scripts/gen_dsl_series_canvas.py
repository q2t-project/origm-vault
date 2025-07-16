# gen_dsl_series_canvas.py
# DSLファイル群から進化系列Canvasを生成（@from→@to）

import re
import json
from pathlib import Path

# 入出力設定
dsl_dir = Path("zettel/dsl")
canvas_out = Path("canvas/dsl_series.canvas")
canvas_out.parent.mkdir(parents=True, exist_ok=True)

# ノード・エッジ格納
dsl_edges = []
dsl_nodes = {}

# DSL構文をパース
def parse_dsl(file):
    dsl = file.read_text(encoding="utf-8")
    from_match = re.search(r"@from (\w+)", dsl)
    to_match = re.search(r"@to (\w+)", dsl)
    μ_match = re.search(r"@tension μ=([0-9]+)", dsl)
    if from_match and to_match:
        return {
            "from": from_match.group(1),
            "to": to_match.group(1),
            "μ": μ_match.group(1) if μ_match else ""
        }
    return None

for file in dsl_dir.glob("*.dsl.md"):
    entry = parse_dsl(file)
    if not entry:
        continue
    src, dst, mu = entry["from"], entry["to"], entry["μ"]

    dsl_edges.append((src, dst))
    dsl_nodes[dst] = mu
    dsl_nodes.setdefault(src, None)

# ノード配置
offset_x = 300
offset_y = 150
positions = {}
x, y = 0, 0
for i, node in enumerate(dsl_nodes.keys()):
    positions[node] = (x, y)
    x += offset_x
    y = offset_y * (i % 2)

# Canvas構造
nodes = []
edges = []
for node, mu in dsl_nodes.items():
    pos = positions[node]
    label = f"{node}\nμ={mu}" if mu else node
    nodes.append({
        "id": f"node_{node}", "type": "text",
        "x": pos[0], "y": pos[1],
        "width": 220, "height": 80,
        "text": label, "layer": "foreground"
    })

for src, dst in dsl_edges:
    edges.append({
        "id": f"edge_{src}_{dst}",
        "fromNode": f"node_{src}", "toNode": f"node_{dst}",
        "label": "→", "class": "evolution"
    })

canvas_data = {"nodes": nodes, "edges": edges}
with open(canvas_out, "w", encoding="utf-8") as f:
    json.dump(canvas_data, f, ensure_ascii=False, indent=2)

print("✅ DSL系列Canvas出力完了 →", canvas_out)
