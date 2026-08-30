# Taiwan Job Alignment

更新日期：2026-08-30

## 結論

這條 Roadmap 的主方向與目前台灣 AI / LLM 工程職缺相符，但「涵蓋技能主題」不等於已符合職缺的年資、學歷、領域經驗或上線實績要求。

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

從目前搜尋結果可觀察到大量 Application / Integration 類職缺；純 Model Training 類職缺相對集中在較特定的模型、推論與研究團隊。這是定性觀察，不作為精確職缺數量統計。

因此本 Roadmap 採用策略：

1. 保留 Transformer / PyTorch / Mini GPT，建立模型底層理解。
2. 優先把 SQL、API、RAG、Evaluation、Tool Calling、Docker 做到能展示與說明。
3. Fine-tuning、vLLM、GPU optimization 作為第二階段能力。

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

目前金融科技相關職缺已明確出現：

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

> 從第一個 RAG baseline 開始建立 Evaluation；Week 40–42 再擴充成正式評測套件。後續 Agent、Fine-tuning 與 Model Serving 改動都必須可以比較前後效果。

---

## Roadmap 與職缺吻合度

以下只表示「技能主題覆蓋」，不代表錄取機率或完整職務勝任度。由於目前沒有固定樣本數與逐項計分規則，因此不使用 95% 等無法重現的百分比。

| 目標職位 | 技能主題覆蓋 | 仍需依職缺補強 |
|---|---|---|
| AI Application Engineer | 高 | Cloud、Kubernetes、特定 Agent framework、前端或既有系統整合 |
| GenAI Engineer | 高 | Production 經驗、LLMOps、成本與安全治理 |
| LLM Engineer | 中高 | 模型訓練深度、推論效能、GPU 與分散式系統 |
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

### 第一階段
Week 1–30：

建立模型理解。

成果：
- Python
- PyTorch
- Transformer
- Mini GPT

### 第二階段
Week 31–42：

建立可工作的 AI Engineering 能力。

成果：
- FastAPI
- Docker
- SQL / PostgreSQL integration
- RAG
- Vector DB
- RAG baseline evaluation
- Testing / Logging
- BankGPT v0.3

### Week 42 起

開始投：

- AI Engineer
- AI Application Engineer
- GenAI Engineer
- Junior / Mid LLM Engineer

不要等所有 Roadmap 都結束。

### 第三階段
Week 43–52：

增加差異化。

- Tool Calling
- Agent
- MCP
- LoRA / QLoRA
- vLLM
- Cloud / Production basics

讓 BankGPT 成為完整 Portfolio。
