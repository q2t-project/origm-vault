
// シリーズ選択UI付き μテンショングラフ
const pages = dv.pages('"zettel/fold"')
  .where(p => p.series_id && !isNaN(p.mu));

const seriesMap = new Map();
for (const p of pages) {
  const sid = p.series_id;
  if (!seriesMap.has(sid)) seriesMap.set(sid, []);
  seriesMap.get(sid).push({ label: p.fold_type || p.file.name, mu: p.mu });
}

// ソート
for (const [sid, list] of seriesMap) {
  list.sort((a, b) => a.mu - b.mu);
}

// UI
const container = dv.el("div", "");
const selector = document.createElement("select");
for (const sid of seriesMap.keys()) {
  const opt = document.createElement("option");
  opt.value = sid;
  opt.textContent = sid;
  selector.appendChild(opt);
}
container.appendChild(selector);

const canvas = document.createElement("canvas");
canvas.width = 640;
canvas.height = 300;
container.appendChild(canvas);

function drawChart(seriesId) {
  const items = seriesMap.get(seriesId);
  const labels = items.map(x => x.label);
  const mus = items.map(x => x.mu);

  new Chart(canvas.getContext("2d"), {
    type: "line",
    data: {
      labels: labels,
      datasets: [{
        label: `μテンション推移: ${seriesId}`,
        data: mus,
        fill: false,
        borderColor: "rgba(255, 99, 132, 1)",
        tension: 0.2
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
}

selector.addEventListener("change", e => {
  canvas.getContext("2d").clearRect(0, 0, canvas.width, canvas.height);
  drawChart(e.target.value);
});

// 初期描画
drawChart(selector.value);
