# 🧠 μスコア視覚化 (DataviewJS)

```dataviewjs
const pages = dv.pages('"zettel/fold"')
  .where(p => p.mu_score !== undefined)
  .sort(p => p.mu_score, 'desc');

dv.header(2, "🧠 Foldテンプレ μスコア可視化");
for (let page of pages) {
  const barLength = Math.round((page.mu_score ?? 0) * 20);
  const bar = "█".repeat(barLength).padEnd(20, "░");
  dv.paragraph(`${page.file.name.padEnd(20)} μ: ${page.mu_score.toFixed(2)}  ${bar}`);
}
```