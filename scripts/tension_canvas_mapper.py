# tension_canvas_mapper.py
# μテンション流をCanvas構造にマッピング

import json
from pathlib import Path

json_path = Path("data/mu_tension_flows.json")
canvas_path = Path("canvas/mu_tension_flow.canvas")

with open(json_path, encoding="utf-8") as f:
    flows = json.load(f)

nodes = []
edges = []
offset_x = 300

for idx, (term, data) in enumerate(flows.items()):
    x = idx * offset_x
    from_y = 0
    to_y = -data["delta"] * 100

    # ノード：評価Zettelとmacro構造の2点
    nodes.append({
        "id": f"eval_{term}",
        "type": "text",
        "x": x,
        "y": from_y,
        "width": 200,
        "height": 80,
        "text": f"{term} (評価: μ={data['from_eval']})",
        "layer": "foreground"
    })
    nodes.append({
        "id": f"macro_{term}",
        "type": "text",
        "x": x,
        "y": to_y,
        "width": 200,
        "height": 80,
        "text": f"{term} (macro: μ={data['to_macro']})",
        "layer": "foreground"
    })

    # エッジ：テンション差分を表す線（statusで色分け）
    color = {
        "上昇": "green",
        "維持": "gray",
        "下降": "red"
    }[data["status"]]

    edges.append({
        "id": f"edge_{term}",
        "fromNode": f"eval_{term}",
        "toNode": f"macro_{term}",
        "label": f"μ差分: {data['delta']} ({data['status']})",
        "class": color
    })

canvas_data = {
    "nodes": nodes,
    "edges": edges
}

canvas_path.parent.mkdir(exist_ok=True, parents=True)
with open(canvas_path, "w", encoding="utf-8") as f:
    json.dump(canvas_data, f, ensure_ascii=False, indent=2)

print("✅ Canvasテンション流マップ生成完了 →", canvas_path)
