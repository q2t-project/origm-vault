
const deltaData = {};

const select = document.getElementById("seriesSelect");
const canvas = document.getElementById("deltaChart").getContext("2d");

Object.keys(deltaData).forEach((sid) => {
  const opt = document.createElement("option");
  opt.value = sid;
  opt.textContent = sid;
  select.appendChild(opt);
});

let chart;

function drawChart(sid) {
  const series = deltaData[sid];
  const labels = series.map(d => `${d.from}→${d.to}`);
  const data = series.map(d => d["Δμ"]);
  const bgColors = data.map(d => d > 0 ? "rgba(255,99,132,0.7)" : d < 0 ? "rgba(54,162,235,0.7)" : "rgba(255,206,86,0.7)");

  if (chart) chart.destroy();

  chart = new Chart(canvas, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [{
        label: `Δμ (テンション差分)`,
        data: data,
        backgroundColor: bgColors
      }]
    },
    options: {
      responsive: true,
      scales: {
        y: { beginAtZero: true, title: { display: true, text: "Δμ" } },
        x: { title: { display: true, text: "進化ステップ" } }
      }
    }
  });
}

select.addEventListener("change", (e) => {
  drawChart(e.target.value);
});

drawChart(select.value);
