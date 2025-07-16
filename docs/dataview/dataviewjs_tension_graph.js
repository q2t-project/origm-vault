
```dataviewjs
const ids = ['対照_原因', '対照', '原因', '結論', '前提', '定義', '譲歩', '否定', '説明', '質問', '感嘆'];
const mu_values = [0.73, 0.1, 0.5, 0.8, 0.4, 0.3, 0.6, 0.9, 0.55, 0.35, 0.25];

const ctx = this.container.createEl("canvas");
ctx.width = 800;
ctx.height = 400;
this.container.appendChild(ctx);

new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ids,
    datasets: [{
      label: 'μテンション値',
      data: mu_values,
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
      borderColor: 'rgba(255, 99, 132, 1)',
      borderWidth: 1
    }]
  },
  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
        max: 1
      }
    }
  }
});
```
