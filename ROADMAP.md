# Roadmap

## Phase 1 — 工程與 ML 基礎

### 1. Python
必學：
- Python syntax
- List / Dict / Set / Tuple
- Function / Class
- Iterator / Generator
- Exception handling
- Virtual environment
- typing / dataclass
- pytest 基礎
- NumPy
- Git
- Linux CLI 基礎
- SQL / PostgreSQL 基礎
- Parameterized query / transaction / index 概念

完成標準：
- 能閱讀一般 Python ML 程式碼
- 能使用 NumPy 操作 Tensor-like 資料
- 能建立虛擬環境與 requirements
- 能使用 pytest 驗證核心邏輯
- 能完成基本 SQL 查詢並安全地由 Python 存取 PostgreSQL

---

### 2. Math for ML
必學：
- Linear Algebra
  - Vector
  - Matrix
  - Matrix multiplication
  - Dot product
  - Transpose
  - Linear transformation
  - Eigenvalue / Eigenvector 基礎
- Calculus
  - Derivative
  - Partial derivative
  - Chain rule
  - Gradient
- Probability / Statistics
  - Probability
  - Conditional probability
  - Expectation
  - Variance
  - Distribution
  - Maximum likelihood
  - Cross entropy

原則：
不要等數學全部學完才進下一階段，應與 PyTorch / Neural Network 並行。

---

### 3. ML Fundamentals
必學：
- Train / Validation / Test
- Linear Regression
- Logistic Regression
- Loss Function
- Gradient Descent
- Overfitting / Underfitting
- Regularization
- Batch / Epoch
- Learning Rate

實作：
- NumPy Linear Regression
- NumPy Logistic Regression

---

## Phase 2 — Deep Learning 與 Transformer

### 4. Neural Network + Backpropagation + PyTorch
必學：
- Tensor
- nn.Module
- Linear
- Activation
- Dataset / DataLoader
- Forward
- Loss
- Backward
- Optimizer
- AdamW
- Backpropagation
- Chain Rule

實作：
- MLP classifier
- 自己寫 training loop

---

### 5. Transformer / Attention / Tokenizer
必學：
- Tokenization
- Embedding
- Positional Embedding
- Q / K / V
- Scaled Dot Product Attention
- Causal Mask
- Multi-Head Attention
- Feed Forward
- Residual Connection
- LayerNorm
- Decoder-only Transformer

完成標準：
能回答「GPT 為什麼可以預測下一個 token」。

---

### 6. Hugging Face 基礎
必學：
- transformers
- datasets
- tokenizers
- AutoTokenizer
- AutoModelForCausalLM
- generate
- Trainer 基礎

---

### 7. Mini GPT from Scratch
目標：
自己使用 PyTorch 實作小型 decoder-only Transformer。

專案成果至少包含：
- tokenizer
- attention
- transformer block
- GPT model
- training loop
- generation
- validation loss
- parameter count
- README
- 實驗紀錄

不追求大型模型，重點是理解完整模型生命週期。

---

## Phase 3 — LLM Application Engineering

### 8. LLM 使用
必學：
- Prompting
- Sampling
  - Temperature
  - Top-k
  - Top-p
- Structured Output
- Local model
- API model
- Context window

---

### 9. Embedding + Vector Search
必學：
- Embedding
- Cosine similarity
- Vector index / similarity-search library：FAISS
- Vector database：Qdrant / Milvus 擇一
- Relational database extension：pgvector
- Metadata filtering

---

### 10. RAG
必學：
- Document ingestion
- PDF / HTML / structured document parsing 基礎
- Chunking
- Chunk overlap
- Retrieval
- Top-K
- Hybrid Search
- Reranker
- Context construction
- Citation
- Document-level access control

---

### 11. LLM Evaluation
第一個 RAG baseline 完成時就建立小型評測集；本階段再擴充為正式 evaluation suite，並持續貫穿後續。

必學：
- Retrieval evaluation
- Answer correctness
- Faithfulness
- Groundedness
- Latency
- Cost
- Regression test
- Golden dataset
- Failure taxonomy / error analysis

原則：
Evaluation 不是最後才做，而是每新增能力就同步建立測試。

---

### 12. Tool Calling
必學：
- Structured function call
- Tool schema
- Backend execution
- Tool result 回傳 LLM
- Error handling
- Permission boundary
- Schema validation
- Allowlist / read-only credential / audit log
- 高風險操作的 Human approval

---

### 13. Agent
必學：
- Agent loop
- Planning
- Tool selection
- State
- Memory
- Retry
- Human-in-the-loop

框架可後學：
- LangGraph 等

---

### 14. MCP
必學：
- MCP 基本概念
- Tool / Resource / Prompt
- Client / Server
- 權限與安全邊界
- User consent / data boundary

原則：
先理解 Tool Calling，再學 Agent，最後再學 MCP。

---

## Phase 4 — Model Customization

### 15. Fine-tuning
必學：
- SFT
- PEFT
- LoRA
- QLoRA
- Dataset preparation
- Train / Validation split
- Base vs Fine-tuned evaluation

選擇原則：
- RAG：通常適合外部、需更新、需引用或受權限控管的知識。
- Fine-tuning：通常適合穩定任務的行為、風格、格式或任務適應。
- 兩者可以併用，應以相同 evaluation dataset 比較成效、成本與風險。

---

## Phase 5 — Serving 與 Production

### 16. Serving
必學：
- FastAPI
- Docker
- Linux serving environment
- AWS / Azure / GCP 擇一的部署基礎
- Kubernetes 基本物件與部署概念
- GPU basics
- CUDA 基礎概念
- vLLM
- Quantization
- FP16 / BF16 / INT8 / INT4
- KV Cache
- Batching
- Latency / Throughput

注意：
Docker 應提早使用；vLLM 則屬於較後期的 LLM serving 技能。

環境限制：
- vLLM 的完整 NVIDIA GPU 執行環境以 Linux 為主。
- 實作前先確認 OS、GPU、VRAM、模型大小與量化格式；Windows 使用者應預先準備 Linux 或雲端環境。

---

### 17. Production
Production 能力應從第一個 API 版本逐步加入，這一階段負責整合與補強，而不是第一次接觸。

必學：
- Testing
- Logging
- Monitoring
- Observability
- Security
- Guardrails
- Authentication / Authorization
- CI/CD
- Data / model versioning
- Secrets management
- Cost / token usage tracking

---

## Phase 6 — Capstone

### 18. BankGPT
不要等前 17 階段全部完成才開始。

版本演進：

#### v0.1
- 基本聊天
- Structured Output
- Backend API
- PostgreSQL integration
- Request validation / pytest
- Secrets 不寫入 repository

#### v0.2
- RAG
- Vector DB
- Citation
- Source access control
- Baseline evaluation

#### v0.3
- Evaluation
- Golden dataset
- Regression test

#### v0.4
- Tool Calling
- SQL / API tools
- Agent workflow
- Read-only / allowlist / audit / Human approval

#### v0.5
- Domain SFT
- LoRA / QLoRA
- Base vs Fine-tuned evaluation

#### v1.0
- FastAPI
- Docker
- vLLM
- Linux / cloud deployment
- Minimal demo UI
- Logging
- Monitoring
- Security
- CI/CD

---

## 最終求職定位

主要目標：
- AI Engineer
- LLM Engineer
- GenAI Engineer

進階方向：
- ML Engineer
- LLM Inference Engineer
- AI Research Engineer

核心差異化：
「具備企業 Backend / DB 工程能力，同時懂 Transformer、RAG、Fine-tuning 與 LLM serving。」


## 2026 台灣職缺導向調整

依目前台灣 AI / LLM 職缺，學習優先順序做以下調整：

1. Docker 不等到 Serving 才第一次接觸，於 BankGPT v0.1 階段提前使用。
2. Evaluation 與 RAG 綁定：Week 35 建立 baseline，Week 40–42 擴充正式評測，之後持續回歸測試。
3. Tool Calling 優先於 Agent；Agent 優先於 MCP。
4. RAG 優先於 LoRA / QLoRA。
5. Fine-tuning 是模型客製化能力，不是處理企業最新知識的第一選擇。
6. vLLM 放在後期，因為它屬於模型 Serving / Inference Engineering。
7. Mini GPT 保留，但限制在四週內，避免影響工作導向技能進度。
8. Week 42 起即可開始試投，不必等到一年全部完成。
9. SQL、Testing、Logging 與安全邊界提前融入 BankGPT，不等到最後的 Production 階段。
10. Cloud / Kubernetes 只要求完成一次小型部署與理解核心概念，不以第一年成為平台維運專家為目標。

完整每週安排請看：

[52_WEEK_PLAN.md](52_WEEK_PLAN.md)

台灣職缺技能對照請看：

[TAIWAN_JOB_ALIGNMENT.md](TAIWAN_JOB_ALIGNMENT.md)
