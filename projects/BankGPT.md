# BankGPT

## 專案目的

建立一個具有企業系統工程特性的 LLM Portfolio。

核心不是做單純 Chatbot，而是展示：

```text
Backend Engineering
+
RAG
+
Evaluation
+
Tool Calling / Agent
+
Model Customization
+
Production Deployment
```

## 資料與安全前提

- Portfolio 只使用公開、授權或自行產生的合成資料，不使用真實客戶、帳戶或交易資料。
- Secrets、API key 與連線字串只放在環境變數或 secret store，不寫入 repository。
- 文件與工具操作都必須保留來源、使用者身分、權限判斷與 audit trace。
- 所有可能改變資料或產生金融影響的操作都需要明確確認；Demo 預設只提供唯讀能力。

## Architecture

```text
User
  ↓
Frontend
  ↓
BankGPT API (FastAPI)
  │
  ├─ LLM
  │
  ├─ RAG
  │   ├─ Document Pipeline
  │   ├─ Embedding
  │   ├─ Vector DB
  │   └─ Reranker
  │
  ├─ Tool Layer
  │   ├─ SQL
  │   ├─ Internal API
  │   └─ Calculator
  │
  ├─ Evaluation
  │   ├─ Golden Dataset
  │   ├─ Retrieval Metrics
  │   └─ Answer Metrics
  │
  └─ Production
      ├─ Logging
      ├─ Monitoring
      ├─ Security
      └─ CI/CD
```

---

## Version Plan

### v0.1 — Week 31–32
目標：
基本 LLM Application。

- [ ] FastAPI
- [ ] LLM API / Local Model
- [ ] System Prompt
- [ ] Structured Output
- [ ] Error Handling
- [ ] PostgreSQL / SQLAlchemy integration
- [ ] Request validation / API tests
- [ ] Secrets / environment configuration
- [ ] Dockerfile

---

### v0.2 — Week 35–39
目標：
可追溯來源的企業文件問答。

- [ ] Document ingestion
- [ ] Chunking
- [ ] Embedding
- [ ] Vector DB
- [ ] Metadata filtering
- [ ] Retrieval
- [ ] Hybrid Search
- [ ] Reranker
- [ ] Citation
- [ ] Document-level access filter
- [ ] 10–20 題 baseline questions / expected sources
- [ ] Retrieval trace / request logging

---

### v0.3 — Week 40–42
目標：
可以量化 RAG 品質。

- [ ] 將 baseline 擴充為 20–50 題 Golden Dataset
- [ ] Retrieval Recall
- [ ] Answer Correctness
- [ ] Faithfulness
- [ ] Groundedness
- [ ] Latency
- [ ] Chunk Size Experiment
- [ ] Top-K Experiment
- [ ] Reranker Experiment
- [ ] Regression Test
- [ ] CI-safe evaluation workflow

完成後開始投遞 AI / GenAI / LLM Application 職缺。

---

### v0.4 — Week 43–45
目標：
從「回答問題」升級為「執行企業任務」。

- [ ] Tool schema
- [ ] calculate_interest()
- [ ] get_product_information()
- [ ] SQL query tool
- [ ] Internal API tool
- [ ] Permission boundary
- [ ] Read-only credential
- [ ] Table / operation allowlist
- [ ] Parameterized query
- [ ] Timeout / row limit / audit log
- [ ] Agent state
- [ ] Retry
- [ ] Human-in-the-loop
- [ ] High-risk action approval gate

---

### MCP Experiment — Week 46

MCP 暫不作為 BankGPT 核心依賴。

只完成概念驗證：

- [ ] MCP Client
- [ ] MCP Server
- [ ] Tool
- [ ] Resource
- [ ] Prompt
- [ ] User consent / data boundary

---

### v0.5 — Week 47–48
目標：
完成一次模型客製化實驗。

- [ ] Domain dataset
- [ ] SFT
- [ ] PEFT
- [ ] LoRA / QLoRA
- [ ] Base vs Tuned Evaluation
- [ ] Model / dataset license and PII check
- [ ] GPU / VRAM / cost record

注意：

```text
企業最新知識 → 優先 RAG
模型行為 / 格式 / 任務適應 → Fine-tuning
```

---

### v1.0 — Week 49–52
目標：
達到 Portfolio / Production Demo 水準。

- [ ] vLLM
- [ ] OpenAI-compatible serving
- [ ] Linux / cloud execution environment
- [ ] Quantization
- [ ] KV Cache understanding
- [ ] Batching understanding
- [ ] Docker
- [ ] Logging
- [ ] Monitoring
- [ ] Authentication / Authorization
- [ ] Prompt Injection Defense
- [ ] CI/CD
- [ ] Secrets management
- [ ] Health check / rollback exercise
- [ ] Architecture Diagram
- [ ] Benchmark
- [ ] Evaluation Report
- [ ] Minimal Demo UI（Streamlit / Gradio / React 擇一）
- [ ] Demo
- [ ] Resume bullets

---

## Portfolio 驗收

面試時應能回答：

1. 為什麼這個問題使用 RAG，而不是 Fine-tuning？
2. Chunk Size 如何決定？
3. Top-K 改變會發生什麼？
4. 如何判斷錯誤來自 Retrieval 還是 Generation？
5. 如何量化回答品質？
6. Agent 有哪些權限風險？
7. Tool Calling 如何做 validation？
8. LoRA 改變了什麼？
9. vLLM 解決什麼問題？
10. 系統如何 logging、monitoring、rollback？
11. SQL Tool 如何限制權限、查詢範圍與資料量？
12. 如何避免將真實金融資料、PII 或 secrets 放進模型與 repository？
