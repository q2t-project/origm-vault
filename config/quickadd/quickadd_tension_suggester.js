module.exports = {
  getSuggestions: async function (currentTemplateId) {
    const macroFile = app.vault.getAbstractFileByPath("fold_macro.yaml");
    if (!macroFile) {
      console.error("fold_macro.yaml not found");
      return [];
    }

    const macroText = await app.vault.read(macroFile);
    const macros = window.jsyaml.load(macroText);

    const current = macros.find(m => m.id === currentTemplateId);
    if (!current || !current.bridges) return [];

    const suggestions = current.bridges.map(b => {
      const target = macros.find(m => m.id === b.to);
      const delta = (target.tension || 0) - (current.tension || 0);
      return {
        id: b.to,
        label: `${target.label}（μ+${delta}）：${b.label}`,
        value: b.to  // QuickAddが返す値
      };
    });

    return suggestions;
  }
};