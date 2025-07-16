```dataview
TABLE
  title,
  from,
  to,
  mu,
  link(file.name, "Zettel") as "Zettel Link"
FROM "zettel_simlog_eval"
WHERE series_id = "eval_to_template"
SORT file.name ascending
```