```dataview
TABLE
  title,
  mutation,
  tags[3] as "from",
  tags[4] as "to",
  tags[2] as "mutation_type",
  link(file.name, "Zettel") as "Zettel Link"
FROM "zettel_lineage_with_tags"
WHERE contains(tags, "#lineage")
SORT file.name ascending
```