import sys
import json
from pathlib import Path

def convert_canvas_to_dsl(canvas_json):
    dsl_lines = []
    for node in canvas_json.get("nodes", []):
        node_id = node.get("id", "")
        label = node.get("text", "")
        dsl_lines.append(f"@node {node_id}")
        dsl_lines.append(f"@label \"{label}\"")
        dsl_lines.append("")  # 空行で区切り

    for edge in canvas_json.get("edges", []):
        src = edge.get("source")
        tgt = edge.get("target")
        label = edge.get("label", "")
        dsl_lines.append(f"@edge {src} -> {tgt}")
        if label:
            dsl_lines.append(f"@label \"{label}\"")
        dsl_lines.append("")

    return "\n".join(dsl_lines)

def main(input_path):
    input_file = Path(input_path)
    output_file = input_file.with_suffix(".dsl.md")

    with input_file.open("r", encoding="utf-8") as f:
        canvas_data = json.load(f)

    dsl_text = convert_canvas_to_dsl(canvas_data)

    with output_file.open("w", encoding="utf-8") as f:
        f.write(dsl_text)

    print(f"✅ DSL file generated: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gen_dsl_from_canvas.py input.canvas.json")
    else:
        main(sys.argv[1])