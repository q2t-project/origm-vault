import yaml
from pathlib import Path

def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def extract_patch(master, variant):
    patch = []
    master_ids = {entry['id']: entry for entry in master}
    for entry in variant:
        mid = entry['id']
        if mid not in master_ids or master_ids[mid] != entry:
            patch.append(entry)
    return patch

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python generate_patch_from_diff.py <master.yaml> <variant.yaml>")
    else:
        master = load_yaml(Path(sys.argv[1]))
        variant = load_yaml(Path(sys.argv[2]))
        patch = extract_patch(master, variant)
        print(yaml.dump(patch, allow_unicode=True, sort_keys=False))