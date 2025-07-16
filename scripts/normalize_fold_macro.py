import yaml

def normalize_entry(entry):
    # デフォルトフィールド
    defaults = {
        "label": entry.get("id", ""),
        "type": "unspecified",
        "status": "generated",
        "tags": [],
        "dsl": {},
        "eval": {},
    }

    for key, val in defaults.items():
        if key not in entry:
            entry[key] = val

    # タグがnullや非リストの場合
    if not isinstance(entry["tags"], list):
        entry["tags"] = ["auto_fixed"]

    # φ–ψ–μ axis の型チェック（文字列化）
    for axis in ["φ_axis", "ψ_axis", "μ_axis"]:
        if axis in entry and not isinstance(entry[axis], str):
            entry[axis] = str(entry[axis])

    return entry

# 読み込み
with open("fold_macro.yaml", "r", encoding="utf-8") as f:
    macro = yaml.safe_load(f)

# IDの重複チェック
ids_seen = set()
deduped = []
for entry in macro:
    if isinstance(entry, dict) and "id" in entry:
        if entry["id"] in ids_seen:
            continue  # 重複を除外
        ids_seen.add(entry["id"])
        deduped.append(normalize_entry(entry))

# 書き出し
with open("fold_macro.yaml", "w", encoding="utf-8") as f:
    yaml.dump(deduped, f, allow_unicode=True)

print(f"Normalized {len(deduped)} entries.")
