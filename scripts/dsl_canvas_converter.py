# dsl_canvas_converter.py
# fold DSL構文と Obsidian Canvas 構造の双方向変換器

import json
import re
from pathlib import Path

# DSL構文例
example_dsl = """
@from null
@to assertion
@via evaluation
@reason 構造が未確定だった問いに仮説が与えられたため
"""

def dsl_to_canvas_nodes(dsl_text, x0=0, y0=0, offset=300):
    """DSL構文からCanvas構造ノード・エッジへ変換"""
    from_match = re.search(r"@from (\w+)", dsl_text)
    to_match = re.search(r"@to (\w+)", dsl_text)
    via_match = re.search(r"@via (\w+)", dsl_text)
    reason_match = re.search(r"@reason (.+)", dsl_text)

    if not from_match or not to_match:
        raise ValueError("DSL構文に @from / @to が不足しています")

    from_node = from_match.group(1)
    to_node = to_match.group(1)
    via = via_match.group(1) if via_match else "bridge"
    reason = reason_match.group(1) if reason_match else ""

    nodes = [
        {"id": f"{from_node}_src", "type": "text", "x": x0, "y": y0,
         "width": 200, "height": 80, "text": f"{from_node}", "layer": "foreground"},
        {"id": f"{to_node}_dst", "type": "text", "x": x0 + offset, "y": y0,
         "width": 200, "height": 80, "text": f"{to_node}", "layer": "foreground"}
    ]

    edges = [
        {"id": f"edge_{from_node}_to_{to_node}",
         "fromNode": f"{from_node}_src", "toNode": f"{to_node}_dst",
         "label": via + (" / " + reason if reason else ""),
         "class": "bridge"}
    ]

    return {"nodes": nodes, "edges": edges}

def canvas_to_dsl(canvas_json):
    """Canvas JSON から簡易 DSL 構文へ変換（仮定：1本のエッジ構造）"""
    edges = canvas_json.get("edges", [])
    if not edges:
        return "# Canvasにエッジがありません"

    edge = edges[0]
    label = edge.get("label", "")
    via, _, reason = label.partition(" / ")

    from_node = edge.get("fromNode", "").replace("_src", "")
    to_node = edge.get("toNode", "").replace("_dst", "")

    lines = [
        f"@from {from_node}",
        f"@to {to_node}",
        f"@via {via}"
    ]
    if reason:
        lines.append(f"@reason {reason}")
    return "\n".join(lines)

# テスト出力（任意）
if __name__ == "__main__":
    canvas_data = dsl_to_canvas_nodes(example_dsl)
    with open("canvas/bridge_example.canvas", "w", encoding="utf-8") as f:
        json.dump(canvas_data, f, ensure_ascii=False, indent=2)
    print("✅ DSL→Canvas変換サンプル出力 → canvas/bridge_example.canvas")
