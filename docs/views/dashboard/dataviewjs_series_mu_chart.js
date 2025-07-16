
// 系列ごとのμテンション推移ラインチャート
const pages = dv.pages('"zettel/fold"')
  .where(p => p.mu !== undefined && !isNaN(p.mu) && p.series_id);

const seriesMap = new Map();

for (const page of pages) {
  const series = page.series_id;
  if (!seriesMap.has(series)) seriesMap.set(series, []);
  seriesMap.get(series).push({ label: page.fold_type || page.file.name, mu: page.mu });
}

// ソート（μ順 or 登録順）
for (const [key, list] of seriesMap) {
  seriesMap.set(key, list.sort((a, b) => a.mu - b.mu));
}

const datasets = Array.from(seriesMap.entries()).map(([series, entries]) => ({
  label: series,
  data: entries.map(e => e.mu),
  fill: false,
  tension: 0.1
}));

const labels = Array.from({ length: Math.max(...datasets.map(d => d.data.length)) }, (_, i) => `Step ${i + 1}`);

const container = dv.el("div", "");
const canvas = document.createElement("canvas");
canvas.width = 700;
canvas.height = 400;
container.appendChild(canvas);

new Chart(canvas.getContext("2d"), {
  type: "line",
  data: {
    labels: labels,
    datasets: datasets
  },
  options: {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: '系列ごとのμテンション進化チャート'
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        title: { display: true, text: 'μテンション' }
      },
      x: {
        title: { display: true, text: '進化ステップ' }
      }
    }
  }
});
