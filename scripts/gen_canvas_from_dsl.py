import sys
import re
import json
from pathlib import Path

def parse_dsl_to_canvas_v15(dsl_text: str):
    nodes = []
    edges = []
    current_node = {}
    index = 0
    for line in dsl_text.splitlines():
        line = line.strip()
        if line.startswith("@node "):
            if current_node:
                nodes.append(current_node)
                index += 1
            node_id = line.split()[1]
            current_node = {
                "id": node_id,
                "type": "text",
                "text": node_id,
                "x": index * 300,
                "y": 100,
                "width": 250,
                "height": 60
            }
        elif line.startswith("@label "):
            label = re.findall(r'"(.*?)"', line)
            if label and current_node:
                current_node["text"] = label[0]
    if current_node:
        nodes.append(current_node)

    # エッジは Obsidian 1.5仕様では以下の形式
    # ただし最小構成では空でOK
    return {
        "nodes": nodes,
        "edges": edges
    }

def main(input_path):
    input_file = Path(input_path)
    output_file = input_file.with_suffix(".canvas.json")

    with input_file.open("r", encoding="utf-8") as f:
        dsl_text = f.read()

    canvas_data = parse_dsl_to_canvas_v15(dsl_text)

    with output_file.open("w", encoding="utf-8") as f:
        json.dump(canvas_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Canvas file generated: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gen_canvas_from_dsl.py input.dsl.md")
    else:
        main(sys.argv[1])