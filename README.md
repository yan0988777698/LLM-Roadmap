# LLM Engineer Roadmap

## 專案目標

以「工作導向」方式，從既有軟體工程能力逐步建立 LLM / AI Engineer 所需能力。

這份 Roadmap 的定位不是只學會呼叫 LLM API，而是同時具備：

- AI / LLM Application Engineering
- Transformer 與模型訓練基礎理解
- RAG / Evaluation / Tool Calling / Agent
- Fine-tuning 與模型部署概念
- Production Engineering
- 可展示的 BankGPT Capstone

## 目前台灣職缺對應

依 2026-08 台灣 AI / LLM 相關職缺的定性觀察；這裡描述技能趨勢，不代表具備技能就符合所有年資、學歷或實務經驗要求：

### 高頻核心能力
- Python
- REST API / FastAPI
- SQL
- Git / Linux
- Docker
- LLM API
- Prompt / Context Engineering
- RAG
- Embedding / Vector DB
- Tool Calling
- Agent
- LLM Evaluation
- Testing / Logging / Observability

### 模型工程進階能力
- PyTorch
- Transformer
- Hugging Face
- LoRA / QLoRA
- vLLM
- Quantization
- GPU inference

### 新興 / 加分能力
- MCP
- MLOps
- CI/CD
- AWS / Azure / GCP
- Kubernetes
- AI Security / Guardrails

詳細分析請看：

[TAIWAN_JOB_ALIGNMENT.md](TAIWAN_JOB_ALIGNMENT.md)

## 學習主線

1. Python / NumPy / Git / Linux / SQL
2. Math for ML
3. ML Fundamentals
4. Neural Network + Backpropagation + PyTorch
5. Transformer / Attention / Tokenizer
6. Hugging Face
7. Mini GPT from Scratch
8. LLM Application Basics + FastAPI + PostgreSQL + Docker
9. Embedding + Vector Search
10. RAG
11. LLM Evaluation
12. Tool Calling
13. Agent
14. MCP
15. Fine-tuning：SFT / PEFT / LoRA / QLoRA
16. Serving：vLLM / Quantization / GPU basics
17. Cloud / Production Engineering
18. BankGPT Capstone

## 時間規劃

固定投入：

- 每週：6 小時
- 一年：52 週
- 總時數：約 312 小時

每週建議時間分配：

- 1.5 小時：理解概念
- 3.5 小時：Coding / Experiment
- 1 小時：整理、解釋、Git Commit

學習循環：

```text
Learn
  ↓
Implement
  ↓
Experiment
  ↓
Explain
```

完整 52 週安排：

[52_WEEK_PLAN.md](52_WEEK_PLAN.md)

主題式能力地圖：

[ROADMAP.md](ROADMAP.md)

## Capstone：BankGPT

BankGPT 不等所有知識學完才開始，而是持續演進。

```text
v0.1  LLM + FastAPI + PostgreSQL + Structured Output
 ↓
v0.2  RAG + Vector DB + Citation
 ↓
v0.3  Evaluation + Golden Dataset
 ↓
v0.4  Tool Calling + Agent
 ↓
v0.5  LoRA / QLoRA
 ↓
v1.0  vLLM + Docker + Demo UI + Production
```

## 預計開始投遞職缺

不必等 Week 52。

約完成 Week 42，具備以下能力後，可開始試投：

- Python
- PyTorch / Transformer 基礎
- Hugging Face
- Mini GPT
- FastAPI
- Docker
- Embedding / Vector Search
- RAG
- LLM Evaluation
- BankGPT v0.3

目標職稱：

- AI Engineer
- AI Application Engineer
- GenAI Engineer
- LLM Engineer

之後持續補強 Agent、Fine-tuning、vLLM，提高職缺覆蓋率與技術上限。

## 專案結構

```text
LLM-Engineer-Roadmap/
├─ README.md
├─ ROADMAP.md
├─ 52_WEEK_PLAN.md
├─ TAIWAN_JOB_ALIGNMENT.md
├─ PROGRESS.md
└─ projects/
   └─ BankGPT.md
```
