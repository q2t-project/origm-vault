const macros = [
  { id: "contrast_cause", label: "対照 → 原因", tension: 3 }
];

const choice = await tp.system.suggester(
  macros.map(m => `${m.label} (μ=${m.tension})`),
  macros.map(m => m.id)
);

await tp.file.create_new(choice + ".md", "zettel_templates");
