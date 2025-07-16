import os
import yaml

def eval_to_simlog(eval_path, simlog_path):
    with open(eval_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    from_, to_, mu_diff = None, None, None
    for line in lines:
        if line.startswith('@from '):
            from_ = line.strip().split('@from ')[-1]
        if line.startswith('@to '):
            to_ = line.strip().split('@to ')[-1]
        if line.startswith('@mu_diff '):
            mu_diff = int(line.strip().split('@mu_diff ')[-1])
    if from_ and to_:
        simlog_data = {
            'from': from_,
            'to': to_,
            'mu_diff': mu_diff
        }
        simlog_file = os.path.join(simlog_path, f"simlog_{from_}-{to_}.yaml".replace("/", "_"))
        with open(simlog_file, 'w', encoding='utf-8') as f:
            yaml.dump(simlog_data, f, allow_unicode=True)
