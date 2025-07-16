import yaml
import difflib
from pathlib import Path

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def compare_macros(file1, file2):
    data1 = yaml.dump(load_yaml(file1), sort_keys=False).splitlines()
    data2 = yaml.dump(load_yaml(file2), sort_keys=False).splitlines()
    diff = difflib.unified_diff(data1, data2, fromfile=file1.name, tofile=file2.name)
    return "\n".join(diff)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python compare_macro_variants.py <file1.yaml> <file2.yaml>")
    else:
        f1, f2 = Path(sys.argv[1]), Path(sys.argv[2])
        print(compare_macros(f1, f2))