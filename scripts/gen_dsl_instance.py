import json
import sys
from pathlib import Path
from jinja2 import Template

def main(template_path, data_path, output_path):
    # テンプレート読み込み
    with open(template_path, "r", encoding="utf-8") as f:
        template = Template(f.read())

    # データ読み込み
    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # レンダリング
    rendered = template.render(**data)

    # 出力
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered)

    print(f"✅ DSL generated: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python gen_dsl_instance.py <template.j2> <data.json> <output.dsl.md>")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])