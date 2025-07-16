import os

def eval_to_dsl(eval_path, dsl_path):
    with open(eval_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    from_, to_, mu_diff = None, None, None
    for line in lines:
        if line.startswith('@from '):
            from_ = line.strip().split('@from ')[-1]
        if line.startswith('@to '):
            to_ = line.strip().split('@to ')[-1]
        if line.startswith('@mu_diff '):
            mu_diff = line.strip().split('@mu_diff ')[-1]
    if from_ and to_:
        dsl_content = f"""@template {to_}
@from {from_}
@to {to_}
@mu_diff {mu_diff}
@fold_type null
@μ {mu_diff}
"""
        dsl_file = os.path.join(dsl_path, f"fold_dsl_{to_}.dsl.md".replace("/", "_"))
        with open(dsl_file, 'w', encoding='utf-8') as f:
            f.write(dsl_content)
