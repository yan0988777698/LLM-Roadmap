# Taiwan Job Alignment

職缺觀察日期：2026-08-30
課程／求職里程碑調整日期：2026-09-05（同步新版排程；未重新抽樣職缺）。

## 結論

依下述 2026-08 的定性觀察，這條 Roadmap 的主方向與當時台灣 AI / LLM 工程職缺相符，但「涵蓋技能主題」不等於已符合職缺的年資、學歷、領域經驗或上線實績要求。

大致可分成兩條市場路線：

```text
                     AI / LLM
                        │
          ┌─────────────┴─────────────┐
          │                           │
AI / LLM Application           Model / LLM Engineer
          │                           │
Python                         PyTorch
FastAPI                        Transformer
RAG                            Hugging Face
Vector DB                      Fine-tuning
Tool Calling                   LoRA / QLoRA
Agent                          vLLM
Docker                         Quantization
Evaluation                     GPU / Inference
```

從當時搜尋結果可觀察到大量 Application / Integration 類職缺；純 Model Training 類職缺相對集中在較特定的模型、推論與研究團隊。這是定性觀察，不作為精確職缺數量統計。

因此本 Roadmap 採用策略：

1. 保留 Transformer / PyTorch / Mini GPT，建立模型底層理解。
2. 優先把 SQL、API、RAG、Evaluation、Tool Calling、Docker 做到能展示與說明。
3. Fine-tuning、vLLM、GPU optimization 與 MCP／Kubernetes 改為主線完成後另排的選修，優先保留整合與部署時間。

---

## 技能優先級

| 技能 | 求職重要性 | 定位 |
|---|---|---|
| Python | ★★★★★ | 必學 |
| Git / Linux | ★★★★★ | 必學 |
| SQL | ★★★★★ | 必學 |
| FastAPI / REST API | ★★★★★ | 必學 |
| LLM API | ★★★★★ | 必學 |
| Prompt / Context Engineering | ★★★★★ | 必學 |
| Embedding | ★★★★★ | 必學 |
| Vector Search / Vector DB | ★★★★★ | 必學 |
| RAG | ★★★★★ | 核心 |
| LLM Evaluation | ★★★★★ | 核心 |
| Tool Calling | ★★★★★ | 核心 |
| Docker | ★★★★★ | 核心 |
| Testing / Observability | ★★★★☆ | 高優先 |
| Cloud Deployment | ★★★★☆ | 高優先 |
| Agent | ★★★★☆ | 高優先 |
| Transformer | ★★★★☆ | 建議深入 |
| PyTorch | ★★★★☆ | 建議深入 |
| Hugging Face | ★★★★☆ | 建議深入 |
| Kubernetes | ★★★☆☆ | 部署職缺加分 |
| MCP | ★★★☆☆ | 新興加分 |
| LoRA / QLoRA | ★★★☆☆ | 模型職缺重要 |
| vLLM | ★★★☆☆ | 模型部署重要 |
| Mini GPT from Scratch | ★★★☆☆ | 非必要但差異化高 |
| CUDA / Distributed Training | ★★☆☆☆ | 後期選修 |

---

## 2026-08 台灣職缺觀察

### AI Application / Integration 類職缺常見要求

高頻出現：

- Python
- FastAPI / Flask
- RAG
- LangChain / LangGraph / LlamaIndex
- Vector Database
- SQL
- Git
- Docker
- Testing / Logging / Tracing
- Cloud deployment
- Prompt Engineering
- LLM API
- Agent
- Linux

部分職缺還會要求：

- 非同步 Python / Pydantic / ORM
- 文件解析、資料清理與 ETL
- Kubernetes / CI/CD / MLOps
- AWS / Azure / GCP 擇一

因此求職導向不應該把所有時間花在「從零訓練大型模型」。

---

### Model / LLM Engineering 類職缺常見加深項目

較偏模型的職缺會增加：

- PyTorch
- Transformer
- Model training / inference
- Fine-tuning
- LoRA / QLoRA
- Quantization
- vLLM / SGLang
- GPU resource management
- Latency / Throughput optimization

這些能力決定之後能否從 AI Application Engineer 往更偏 LLM / ML Engineer 移動。

---

### Evaluation 的重要性

Evaluation 不應該放在 Roadmap 最後。

2026-08 的金融科技相關職缺觀察包含：

- Accuracy
- Relevance
- Faithfulness
- Consistency
- Golden Dataset
- Synthetic Data
- RAG Evaluation
- Prompt Injection / Jailbreak
- CI/CD Regression Testing

因此本專案規定：

> Week 36 建立 retrieval baseline；Week 39 第一個完整 RAG 同週加入答案／citation／拒答檢查；Week 43–44 擴充 Golden Dataset、held-out 與正式回歸評估。後續 Agent 與選修的 Fine-tuning／Model Serving 改動都應比較前後效果。

---

## Roadmap 與職缺吻合度

以下只表示「技能主題覆蓋」，不代表錄取機率或完整職務勝任度；選修列在能力地圖，不代表完成第一年就已實作。由於目前沒有固定樣本數與逐項計分規則，因此不使用 95% 等無法重現的百分比。

| 目標職位 | 技能主題覆蓋 | 仍需依職缺補強 |
|---|---|---|
| AI Application Engineer | 高 | 更深入 Cloud／企業部署、Kubernetes、特定 Agent framework、前端或既有系統整合 |
| GenAI Engineer | 高 | Production 經驗、LLMOps、成本與安全治理 |
| LLM Engineer | 主線涵蓋基礎；深度需選修 | Fine-tuning、模型訓練深度、vLLM／推論效能、GPU 與分散式系統 |
| ML Engineer | 中 | 資料工程、特徵工程、統計、MLOps 與非 LLM 模型廣度 |
| LLM Research / Training Engineer | 入門至中 | 深入數學、論文重現、大規模資料與分散式訓練 |

若目標轉向 Research / Foundation Model Training，需要額外補：

- 更深入 Probability / Optimization
- Distributed Training
- CUDA
- Triton
- Parallelism
- Large-scale Dataset Pipeline
- Paper reproduction

目前不列為第一年主線。

---

## 參考職缺來源與限制

以下為 2026-08 搜尋入口，職缺內容與筆數會持續變動：

- [104 AI 工程師職缺搜尋](https://www.104.com.tw/jobs/search/?jobcat=2007001020&order=15&page=1)
- [104 AI 軟體工程師搜尋](https://www.104.com.tw/jobs/search/?keyword=AI%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%E5%B8%AB)
- [Cake LLM 職缺搜尋](https://www.cake.me/jobs/LLM?locale=zh-TW)
- [Cake RAG 職缺搜尋](https://www.cake.me/jobs/rag?locale=en)

限制：

- 搜尋頁會混入 CV、Data、Infrastructure 與非 LLM 職缺。
- 關鍵字出現不代表該技能是必備條件。
- 同一職缺可能重複出現在多個搜尋結果。
- 年資、學歷、產業知識、英文與溝通能力不屬於本 Roadmap 的技能覆蓋率。

若要產生可重現的百分比，應固定搜尋條件、抽樣日期與樣本數，逐筆標記 must-have / nice-to-have 後再統計。

---

## 求職策略

排程以 [52_WEEK_PLAN.md](52_WEEK_PLAN.md) 為準；年度 48 週主線／288h + 4 週緩衝／24h = 312h。Week 13、23、35、48 不預排新課程。

### Week 1–13：工程／必要數學與早期作品

先完成 Python／NumPy／必要數學，再於 Week 9–12 建立 BankGPT v0.1（LLM client、FastAPI、PostgreSQL、tests、Docker）。Week 13 整合／補課。既有 Backend／DB 經驗直接用於作品。

### Week 14–35：模型理解與可重現實驗

保留 ML、PyTorch、Transformer、HF 指定小節與四週 Mini GPT。Week 19 先跟做完整 MLP，Week 22 能獨立組織 training loop，Week 34 完成 Mini GPT。Week 23／35 用於補課並確認既有 API 可重跑。

### Week 36–44：RAG 與 Evaluation

Week 36 建立檢索 baseline，Week 39 同步檢查 RAG 答案與來源。Week 42 的 v0.2 應有可重現 Demo／README、10–20 題 baseline、citation、權限與失敗分析；達標即可開始試投。

Week 43–44 建立至少 20 題 Golden Dataset（含至少 5 題未參與調參的 held-out）、離線回歸 CI 與評估報告，完成 BankGPT v0.3，再補強作品證據。

第一年優先對應 AI Application Engineer／GenAI Engineer；AI Engineer／LLM Engineer 職稱範圍較廣，需逐職缺核對。週數不是投遞門檻或錄取保證；若作品提前達標可以提前投，尚未達標則按驗收調整。

### Week 45–52：工具、安全與部署

Week 45–47 完成 v0.4 的 tool calling、唯讀後端整合與有停止條件的 agent；Week 48 保留整合。

Week 49–52 完成一次雲端部署、監控／安全案例、rollback、最小 UI 與 Portfolio。v1.0 使用既有 API 模型，不以自架模型、微調或 MCP 為必要條件。

### 主線完成後：依目標職缺選進階能力

- 模型客製化職位：SFT／LoRA 或 QLoRA、資料與 base／tuned evaluation。
- 模型部署職位：vLLM、量化、GPU／VRAM、latency／throughput 實驗。
- 應用整合職位：MCP 或單一 Agent framework。
- 部署平台職位：Kubernetes 與更深入的 Cloud／MLOps。

選修另計時數，不預占補課週。保留模型深度的學習方向，同時讓第一年作品的必要完成範圍可控。
