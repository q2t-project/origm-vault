
// DataviewJS: φ–ψ–μによるfoldテンプレ分類フィルタ
let phiFilter = dv.input.select("φ軸でフィルタ", ["比較", "準備", "因果", "否定", "帰結", "すべて"], "すべて");
let psiFilter = dv.input.select("ψ軸でフィルタ", ["null", "条件", "推論", "反駁", "主張", "すべて"], "すべて");
let muRange = dv.input.slider("μ上限（≦）", 0, 3, 0.1, 3.0);

let macros = dv.page("fold_macro.yaml").file.tasks;

if (!macros) {
  dv.paragraph("fold_macro.yaml が読み込めませんでした。");
} else {
  let filtered = macros
    .filter(t => t.text.includes("id:") && t.text.includes("μ_axis:"))
    .map(t => {
      let id = t.text.match(/id:\s*(\S+)/)?.[1];
      let phi = t.text.match(/φ_axis:\s*(\S+)/)?.[1];
      let psi = t.text.match(/ψ_axis:\s*(\S+)/)?.[1];
      let mu = t.text.match(/μ_axis:\s*(\S+)/)?.[1];
      return {id, phi, psi, mu};
    }).filter(e =>
      (phiFilter === "すべて" || e.phi === phiFilter) &&
      (psiFilter === "すべて" || e.psi === psiFilter) &&
      (e.mu && ["支持", "相互作用", "収束", "発散", "中性"].includes(e.mu))
    );

  dv.table(["ID", "φ", "ψ", "μ"], filtered.map(e => [e.id, e.phi, e.psi, e.mu]));
}
