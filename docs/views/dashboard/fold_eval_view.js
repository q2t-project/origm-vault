
document.addEventListener("DOMContentLoaded", function() {
  const data = [
  {
    "id": "F01",
    "label": "構造テンプレ",
    "type": "structure",
    "slots": [
      "主張",
      "根拠",
      "帰結"
    ],
    "bridges": [
      {
        "to": "F02",
        "from_slot": "主張",
        "to_slot": "反論対象",
        "type": "contradiction",
        "label": "主張に対する反論"
      }
    ],
    "tension": 2
  },
  {
    "id": "F02",
    "label": "反論テンプレ",
    "type": "refutation",
    "slots": [
      "反論対象",
      "反論内容",
      "反証例"
    ],
    "bridges": [
      {
        "to": "F03",
        "from_slot": "反証例",
        "to_slot": "前提",
        "type": "transformation",
        "label": "反証例を起点に新たな展開"
      }
    ],
    "tension": 3
  },
  {
    "id": "F03",
    "label": "展開テンプレ",
    "type": "expansion",
    "slots": [
      "前提",
      "補助要素",
      "展開先"
    ],
    "tension": 4
  },
  {
    "id": "対照_原因",
    "from": [
      "対照"
    ],
    "to": [
      "原因"
    ],
    "type": "因果",
    "morph": "推論",
    "tension": 3,
    "φ_axis": "比較",
    "ψ_axis": "推論",
    "μ_axis": "相互作用",
    "tags": [
      "μ=3",
      "logic"
    ],
    "note": "比較から因果への進化",
    "label": "対照 → 原因",
    "eval": {
      "mu_score": 0.73,
      "psi_focus": "refutation",
      "comment": "初期評価：テンション構造は安定。分類・進化が明確。",
      "tension_state": "stable",
      "last_eval": "2025-07-13"
    },
    "dsl": {
      "from": "null",
      "to": "unknown",
      "mutation": "base_init",
      "mu": 0.73,
      "psi": "refutation",
      "state": "stable"
    }
  },
  {
    "name": "対照",
    "id": "対照",
    "φ_axis": "比較",
    "ψ_axis": "null",
    "μ_axis": "null",
    "eval": {
      "mu_score": 0.1,
      "psi_focus": null,
      "comment": "初期比較対象。意味テンションは極低。",
      "tension_state": "dormant",
      "last_eval": "2025-07-13"
    },
    "dsl": {
      "from": "対照_原因",
      "mutation": "unknown",
      "type": "unspecified",
      "mu": 0.1,
      "state": "dormant"
    }
  },
  {
    "name": "原因",
    "id": "原因",
    "φ_axis": "因果",
    "ψ_axis": "推論",
    "μ_axis": "相互作用",
    "eval": {
      "mu_score": 0.5,
      "psi_focus": "refutation",
      "comment": "原因構造として中程度のテンション。射の終点候補。",
      "tension_state": "stable",
      "last_eval": "2025-07-13"
    },
    "dsl": {
      "from": "対照",
      "mutation": "unknown",
      "type": "unspecified",
      "mu": 0.5,
      "state": "stable"
    }
  },
  {
    "name": "結論",
    "id": "結論",
    "φ_axis": "帰結",
    "ψ_axis": "推論",
    "μ_axis": "収束",
    "eval": {
      "mu_score": 0.8,
      "psi_focus": "assertion",
      "comment": "高テンション終点。議論のまとめ役。",
      "tension_state": "strong",
      "last_eval": "2025-07-13"
    },
    "dsl": {
      "from": "原因",
      "mutation": "unknown",
      "type": "unspecified",
      "mu": 0.8,
      "state": "strong"
    }
  },
  {
    "name": "前提",
    "id": "前提",
    "φ_axis": "準備",
    "ψ_axis": "条件",
    "μ_axis": "支持",
    "eval": {
      "mu_score": 0.4,
      "psi_focus": "foundation",
      "comment": "議論の出発点としてテンション中程度。",
      "tension_state": "moderate",
      "last_eval": "2025-07-13"
    },
    "dsl": {
      "from": "結論",
      "mutation": "unknown",
      "type": "unspecified",
      "mu": 0.4,
      "state": "moderate"
    }
  },
  {
    "name": "定義",
    "id": "定義",
    "φ_axis": "同一",
    "ψ_axis": "明確化",
    "μ_axis": "静止",
    "eval": {
      "mu_score": 0.3,
      "psi_focus": "definition",
      "comment": "論証ではないが安定構造。",
      "tension_state": "low",
      "last_eval": "2025-07-13"
    },
    "dsl": {
      "from": "前提",
      "mutation": "unknown",
      "type": "unspecified",
      "mu": 0.3,
      "state": "low"
    }
  },
  {
    "name": "譲歩",
    "id": "譲歩",
    "φ_axis": "対立",
    "ψ_axis": "修正",
    "μ_axis": "緩衝",
    "eval": {
      "mu_score": 0.6,
      "psi_focus": "concession",
      "comment": "反論的だが衝突回避的。μ高め。",
      "tension_state": "unstable",
      "last_eval": "2025-07-13"
    },
    "dsl": {
      "from": "定義",
      "mutation": "unknown",
      "type": "unspecified",
      "mu": 0.6,
      "state": "unstable"
    }
  },
  {
    "name": "否定",
    "id": "否定",
    "φ_axis": "否定",
    "ψ_axis": "反駁",
    "μ_axis": "断絶",
    "eval": {
      "mu_score": 0.9,
      "psi_focus": "refutation",
      "comment": "最大テンション。議論の衝突点。",
      "tension_state": "critical",
      "last_eval": "2025-07-13"
    },
    "dsl": {
      "from": "譲歩",
      "mutation": "unknown",
      "type": "unspecified",
      "mu": 0.9,
      "state": "critica"
    }
  },
  {
    "name": "説明",
    "id": "説明",
    "φ_axis": "展開",
    "ψ_axis": "解釈",
    "μ_axis": "拡張",
    "eval": {
      "mu_score": 0.55,
      "psi_focus": "explanation",
      "comment": "背景補完テンプレ。μ中程度。",
      "tension_state": "normal",
      "last_eval": "2025-07-13"
    },
    "dsl": {
      "from": "否定",
      "mutation": "unknown",
      "type": "unspecified",
      "mu": 0.55,
      "state": "norma"
    }
  },
  {
    "name": "質問",
    "id": "質問",
    "φ_axis": "不明",
    "ψ_axis": "探求",
    "μ_axis": "未定義",
    "eval": {
      "mu_score": 0.35,
      "psi_focus": "inquiry",
      "comment": "探索的テンプレ。定義前構造。",
      "tension_state": "inquiry",
      "last_eval": "2025-07-13"
    },
    "dsl": {
      "from": "説明",
      "mutation": "unknown",
      "type": "unspecified",
      "mu": 0.35,
      "state": "inquiry"
    }
  },
  {
    "name": "感嘆",
    "id": "感嘆",
    "φ_axis": "感情",
    "ψ_axis": "表現",
    "μ_axis": "発散",
    "eval": {
      "mu_score": 0.25,
      "psi_focus": "expression",
      "comment": "非論理的テンプレ。枠外扱い。",
      "tension_state": "expressive",
      "last_eval": "2025-07-13"
    },
    "dsl": {
      "from": "質問",
      "mutation": "unknown",
      "type": "unspecified",
      "mu": 0.25,
      "state": "expressive"
    }
  },
  {
    "title": "仮テンプレ Express",
    "fold_type": "express",
    "series_id": "simlog.null.01",
    "mu": 0,
    "phi": 0,
    "psi": 0
  },
  {
    "title": "仮テンプレ Compare",
    "fold_type": "compare",
    "series_id": "simlog.null.02",
    "mu": 0,
    "phi": 0,
    "psi": 0
  },
  {
    "title": "仮テンプレ Define",
    "fold_type": "define",
    "series_id": "simlog.null.03",
    "mu": 0,
    "phi": 0,
    "psi": 0
  },
  {
    "title": "仮テンプレ Explain",
    "fold_type": "explain",
    "series_id": "simlog.null.04",
    "mu": 0,
    "phi": 0,
    "psi": 0
  },
  {
    "title": "仮テンプレ Inquire",
    "fold_type": "inquire",
    "series_id": "simlog.null.05",
    "mu": 0,
    "phi": 0,
    "psi": 0
  },
  {
    "title": "SimLog派生テンプレ（原因→結論）",
    "fold_type": "結論",
    "from": "原因",
    "to": null,
    "mu": 1,
    "phi": 0,
    "psi": 0,
    "series_id": "simlog.ast.原因_結論"
  },
  {
    "title": "SimLog派生テンプレ（否定→質問）",
    "fold_type": "質問",
    "from": "否定",
    "to": null,
    "mu": 1,
    "phi": 0,
    "psi": 0,
    "series_id": "simlog.ast.否定_質問"
  },
  {
    "title": "SimLog派生テンプレ（定義→説明）",
    "fold_type": "説明",
    "from": "定義",
    "to": null,
    "mu": 1,
    "phi": 0,
    "psi": 0,
    "series_id": "simlog.ast.定義_説明"
  },
  {
    "title": "SimLog派生テンプレ（結論→否定）",
    "fold_type": "否定",
    "from": "結論",
    "to": null,
    "mu": 1,
    "phi": 0,
    "psi": 0,
    "series_id": "simlog.ast.結論_否定"
  },
  {
    "title": "SimLog派生テンプレ（結論→質問）",
    "fold_type": "質問",
    "from": "結論",
    "to": null,
    "mu": 1,
    "phi": 0,
    "psi": 0,
    "series_id": "simlog.ast.結論_質問"
  },
  {
    "title": "SimLog派生テンプレ（説明→定義）",
    "fold_type": "定義",
    "from": "説明",
    "to": null,
    "mu": 1,
    "phi": 0,
    "psi": 0,
    "series_id": "simlog.ast.説明_定義"
  },
  {
    "title": "SimLog派生テンプレ（質問→説明）",
    "fold_type": "説明",
    "from": "質問",
    "to": null,
    "mu": 1,
    "phi": 0,
    "psi": 0,
    "series_id": "simlog.ast.質問_説明"
  }
];
  const tbody = document.querySelector("#macroTable tbody");
  data.forEach(entry => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${entry.title || ""}</td>
      <td>${entry.fold_type || ""}</td>
      <td>${entry.mu || ""}</td>
      <td>${entry.phi || ""}</td>
      <td>${entry.psi || ""}</td>
      <td>${entry.from || ""}</td>
      <td>${entry.to || ""}</td>
      <td>${entry.series_id || ""}</td>
    `;
    tbody.appendChild(tr);
  });
});
