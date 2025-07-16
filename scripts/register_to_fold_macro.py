import sys, yaml

def register(zettel_id):
    with open("fold_macro.yaml", "r", encoding="utf-8") as f:
        macro = yaml.safe_load(f)
    if not any(x.get("id") == zettel_id for x in macro):
        macro.append({
            "id": zettel_id,
            "label": zettel_id,
            "type": "from_canvas",
            "status": "generated",
            "tags": ["auto_from_canvas"]
        })
        with open("fold_macro.yaml", "w", encoding="utf-8") as f:
            yaml.dump(macro, f, allow_unicode=True)

if __name__ == "__main__":
    register(sys.argv[1])
