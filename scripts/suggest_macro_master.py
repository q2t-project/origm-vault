import yaml
from pathlib import Path
from collections import defaultdict

def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def score_macro(macro):
    score = 0
    if 'tension' in macro:
        score += macro['tension']
    if macro.get('type') and macro['type'] != 'null':
        score += 1
    if macro.get('slots'):
        score += len(macro['slots']) * 0.5
    return score

def rank_macros(macros):
    return sorted(macros, key=score_macro, reverse=True)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python suggest_macro_master.py <macro.yaml>")
    else:
        macros = load_yaml(Path(sys.argv[1]))
        ranked = rank_macros(macros)
        for m in ranked[:5]:
            print(f"{m['id']} (score={score_macro(m)})")