import yaml
import json
from pathlib import Path

def load_macro(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def generate_dsl(macros):
    lines = ["@series fold_macro_ast"]
    bridges = []
    simlogs = []
    for macro in macros:
        lines.append(f"\n@node {macro['id']}")
        lines.append(f"@label \"{macro['label']}\"")
        lines.append(f"@type {macro['type']}")
        lines.append("@ast")
        for slot in macro.get("slots", []):
            lines.append(f"  slot: {slot}")
        for bridge in macro.get("bridges", []):
            bid = f"B_{macro['id']}_{bridge['to']}"
            bridges.append((bid, macro['id'], bridge))
            simlogs.append((f"L_{macro['id']}_{bridge['to']}", macro['id'], bridge['to'], bid, bridge['label']))
    lines.append("\n@series fold_bridge")
    for bid, from_id, b in bridges:
        lines.append(f"\n@bridge {bid}")
        lines.append(f"@from {from_id}.slot:{b['from_slot']}")
        lines.append(f"@to {b['to']}.slot:{b['to_slot']}")
        lines.append(f"@type {b['type']}")
        lines.append(f"@label \"{b['label']}\"")
    lines.append("\n@series simlog")
    for lid, f1, f2, bid, reason in simlogs:
        lines.append(f"\n@log {lid}")
        lines.append(f"@from {f1}")
        lines.append(f"@to {f2}")
        lines.append(f"@tension_delta +1")
        lines.append(f"@bridge {bid}")
        lines.append(f"@reason \"{reason}\"")
    return "\n".join(lines)

def generate_canvas(macros):
    nodes, edges = [], []
    slot_map = {}
    for i, macro in enumerate(macros):
        base_x = i * 400
        base_y = 0
        tid = macro["id"]
        nodes.append({
            "id": tid, "type": "text", "text": macro["label"],
            "x": base_x, "y": base_y, "width": 250, "height": 60
        })
        for j, slot in enumerate(macro.get("slots", [])):
            sid = f"{tid}_slot{j+1}"
            slot_key = f"{tid}.slot:{slot}"
            x = base_x
            y = base_y + 100 + j * 70
            nodes.append({
                "id": sid, "type": "text", "text": f"slot: {slot}",
                "x": x, "y": y, "width": 200, "height": 50
            })
            edges.append({"id": f"edge_{tid}_{sid}", "type": "edge", "source": tid, "target": sid, "label": ""})
            slot_map[slot_key] = sid

    # Bridge edges
    for macro in macros:
        from_id = macro["id"]
        for b in macro.get("bridges", []):
            k1 = f"{from_id}.slot:{b['from_slot']}"
            k2 = f"{b['to']}.slot:{b['to_slot']}"
            if k1 in slot_map and k2 in slot_map:
                edges.append({
                    "id": f"bridge_{from_id}_{b['to']}",
                    "type": "edge",
                    "source": slot_map[k1],
                    "target": slot_map[k2],
                    "label": "Bridge"
                })
        # SimLog edges
        for b in macro.get("bridges", []):
            edges.append({
                "id": f"simlog_{from_id}_{b['to']}",
                "type": "edge",
                "source": from_id,
                "target": b['to'],
                "label": "Δ+1"
            })
    return {"nodes": nodes, "edges": edges}

def generate_dot(macros):
    lines = ["digraph FoldBridgeSimLog {", "  rankdir=LR;", "  node [shape=box, style=filled, fillcolor=lightgray];"]
    for m in macros:
        lines.append(f"  {m['id']} [label=\"{m['id']}\\n{m['label']}\"];")
        for i, slot in enumerate(m.get("slots", [])):
            sid = f"{m['id']}_s{i+1}"
            lines.append(f"  {sid} [label=\"slot: {slot}\", shape=ellipse];")
            lines.append(f"  {m['id']} -> {sid};")
    for m in macros:
        for b in m.get("bridges", []):
            from_sid = f"{m['id']}_s{m['slots'].index(b['from_slot'])+1}"
            to_sid = f"{b['to']}_s1"  # assume first slot
            lines.append(f"  {from_sid} -> {to_sid} [label=\"{b['label']}\"];")
            lines.append(f"  {m['id']} -> {b['to']} [label=\"Δ+1\", color=blue, penwidth=2];")
    lines.append("}")
    return "\n".join(lines)

def main():
    macro_file = Path("fold_macro.yaml")
    macros = load_macro(macro_file)

    dsl = generate_dsl(macros)
    canvas = generate_canvas(macros)
    dot = generate_dot(macros)

    Path("fold_dsl").mkdir(exist_ok=True)
    Path("fold_canvas").mkdir(exist_ok=True)
    Path("fold_graphviz").mkdir(exist_ok=True)

    Path("fold_dsl/generated_from_macro.dsl.md").write_text(dsl, encoding="utf-8")
    with open("fold_canvas/generated_from_macro.canvas.json", "w", encoding="utf-8") as f:
        json.dump(canvas, f, ensure_ascii=False, indent=2)
    Path("fold_graphviz/generated_from_macro.dot").write_text(dot, encoding="utf-8")

    print("✅ All outputs generated.")

if __name__ == "__main__":
    main()