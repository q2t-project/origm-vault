
import yaml, json, os

dsl_file = "simlog_eval_to_template.dsl.yaml"
fold_macro_file = "fold_macro_with_zettel_refs.yaml"
canvas_file = "eval_template_links_with_fold.canvas"
report_file = "dsl_structure_linter_report.md"

# Load files
with open(dsl_file, "r", encoding="utf-8") as f:
    dsl_entries = yaml.safe_load(f)

with open(fold_macro_file, "r", encoding="utf-8") as f:
    fold_macro = yaml.safe_load(f)

with open(canvas_file, "r", encoding="utf-8") as f:
    canvas_data = json.load(f)

# Prepare data
dsl_to_names = set(d["to"] for d in dsl_entries)
fold_macro_names = set(t["name"] for t in fold_macro if "name" in t)
canvas_nodes = {n["id"]: n for n in canvas_data["nodes"]}
canvas_edge_pairs = set()

for e in canvas_data["edges"]:
    if e.get("label") == "evaluation_based":
        from_text = canvas_nodes[e["fromNode"]]["text"].split("\n")[0]
        to_text = canvas_nodes[e["toNode"]]["text"].split("\n")[0]
        canvas_edge_pairs.add((from_text, to_text))

# Run Linter Checks
errors = []

# DSL構文
for i, d in enumerate(dsl_entries, 1):
    if not all(k in d for k in ["from", "to", "mutation", "mu"]):
        errors.append({
            "type": "DSL構文エラー",
            "target": f"DSL-{i:03}",
            "detail": f"必須キー不足: {d}"
        })

# DSL→fold_macro存在チェック
for d in dsl_entries:
    if d["to"] not in fold_macro_names:
        errors.append({
            "type": "未定義テンプレ参照",
            "target": d["to"],
            "detail": "DSLで参照されているが fold_macro に存在しない"
        })

# Canvas DSL整合性
for from_text, to_text in canvas_edge_pairs:
    if not any(d["from"] == from_text and d["to"] == to_text for d in dsl_entries):
        errors.append({
            "type": "Canvas⇔DSL不整合",
            "target": f"{from_text} → {to_text}",
            "detail": "CanvasにあるがDSLに存在しない"
        })

# fold_macro未参照テンプレ
for name in fold_macro_names:
    if name not in dsl_to_names:
        errors.append({
            "type": "DSL未参照テンプレ",
            "target": name,
            "detail": "fold_macroに存在するがDSLに参照されていない"
        })

# Export report
lines = ["# DSL構造Linterレポート\n"]
if not errors:
    lines.append("✅ すべての構造は整合しています。\n")
else:
    lines.append(f"❌ 構造整合性に {len(errors)} 件のエラーがあります。\n")
    lines.append("| エラー種別 | 対象ID | 詳細 |")
    lines.append("|------------|---------|------|")
    for err in errors:
        lines.append(f"| {err['type']} | {err['target']} | {err['detail']} |")

with open(report_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("Linter completed. Report written to", report_file)
