import os
import yaml

def eval_to_macro(eval_path, macro_path):
    with open(eval_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    to_, mu_diff = None, None
    for line in lines:
        if line.startswith('@to '):
            to_ = line.strip().split('@to ')[-1]
        if line.startswith('@mu_diff '):
            mu_diff = int(line.strip().split('@mu_diff ')[-1])
    with open(macro_path, 'r', encoding='utf-8') as f:
        macro_data = yaml.safe_load(f)
    for item in macro_data:
        if item.get('name') == to_:
            item['mu'] = mu_diff
    with open(macro_path, 'w', encoding='utf-8') as f:
        yaml.dump(macro_data, f, allow_unicode=True)
