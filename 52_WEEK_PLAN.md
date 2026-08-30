# 52-Week Learning Plan

## 時間預算

每週固定 6 小時。

全年：

```text
6 小時 × 52 週 = 312 小時
```

每週時間配置：

```text
1.5h  理解
3.5h  Coding / Experiment
1.0h  Notes / Explain / Git
```

禁止模式：

```text
6 小時全部看影片
```

前提與範圍：

- 本計畫假設已有一般軟體工程與 C# 開發經驗。
- SQL、Testing、API 與安全會在專案中持續使用，不只出現在單一週。
- 若沒有可用 GPU，Fine-tuning 與 vLLM 實驗改用短期雲端資源或合適的小模型。

建議模式：

```text
Learn
  ↓
Implement
  ↓
Experiment
  ↓
Explain
```

---

## Phase 1 — Python / NumPy / Git / Linux / SQL
### Week 1–4｜24h

#### Week 1 — Python Syntax for C# Developer
學習：
- List / Dict / Set / Tuple
- Function
- Comprehension
- Pythonic iteration

實作：
- 將 2–3 題熟悉的 C# 演算法改寫成 Python。

驗收：
- 不需要查語法即可完成一般 collection 操作。

#### Week 2 — Python Engineering Basics
學習：
- Class
- dataclass
- typing
- module / package
- exception
- iterator / generator
- venv / pip
- pytest

實作：
- 建立一個小型 Python package。
- 為核心函式加入單元測試。

驗收：
- 能理解一般 ML repository 的 Python 專案結構。

#### Week 3 — NumPy
學習：
- ndarray
- shape
- reshape
- slicing
- broadcasting
- matrix multiplication

實作：
- 使用 NumPy 操作 batch × feature matrix。

驗收：
- 看得懂 shape transformation。

#### Week 4 — Git / Linux / SQL Bridge
學習：
- Git branch / commit / merge 基礎
- Linux CLI
- file / process / environment
- pip requirements
- PostgreSQL / relational database 基礎
- SELECT / JOIN / transaction / index 概念
- Parameterized query

實作：
- 建立 Roadmap Git repository。
- 每週學習成果 commit。
- 使用 Python 安全地完成一次 PostgreSQL CRUD 小實驗。

---

## Phase 2 — Math for ML
### Week 5–8｜24h

原則：
只學會直接影響 ML / Transformer 理解的數學。

#### Week 5 — Vector / Matrix / Dot Product
學習：
- Vector
- Matrix
- Dot Product
- Norm

連結：
- Embedding
- Similarity

#### Week 6 — Matrix Multiplication / Linear Transformation
學習：
- Matrix multiplication
- Transpose
- Linear transformation

連結：
```text
Q = XWq
K = XWk
V = XWv
```

驗收：
- 能用 shape 解釋矩陣乘法是否合法。

#### Week 7 — Calculus
學習：
- Derivative
- Partial derivative
- Chain rule
- Gradient

連結：
- Backpropagation

驗收：
- 能解釋 Gradient Descent 更新公式。

#### Week 8 — Probability / Softmax / Cross Entropy
學習：
- Probability
- Expectation
- Variance
- Softmax
- Cross entropy

連結：
- Next-token prediction loss

---

## Phase 3 — ML Fundamentals
### Week 9–12｜24h

#### Week 9 — Train / Validation / Test
學習：
- Dataset split
- Generalization
- Overfitting / Underfitting

#### Week 10 — Linear Regression
實作：
- NumPy Linear Regression
- Loss
- Gradient update

禁止：
- sklearn 一行完成核心演算法。

#### Week 11 — Logistic Regression
實作：
- Sigmoid
- Binary classification
- Loss
- Gradient

#### Week 12 — Training Concepts
學習：
- Batch
- Epoch
- Learning rate
- Regularization
- Evaluation

驗收：
- 能完整描述 training loop。

---

## Phase 4 — Neural Network + PyTorch
### Week 13–18｜36h

#### Week 13 — Tensor
學習：
- torch.Tensor
- dtype
- device
- shape
- tensor operations

#### Week 14 — Neural Network
學習：
- nn.Module
- Linear
- Activation
- Parameters

#### Week 15 — Forward Propagation
實作：
- MLP
- forward()

#### Week 16 — Backpropagation / Autograd
學習：
- Computational graph
- requires_grad
- backward()
- chain rule

實驗：
- 手算 gradient 與 PyTorch gradient 比較。

#### Week 17 — Optimizer
學習：
- SGD
- Adam
- AdamW
- learning rate

#### Week 18 — Complete Training Loop
完成：

```text
Dataset
 ↓
DataLoader
 ↓
Model
 ↓
Forward
 ↓
Loss
 ↓
Backward
 ↓
Optimizer
```

驗收：
- 不看教學即可寫出基本 training loop。

---

## Phase 5 — Transformer
### Week 19–24｜36h

#### Week 19 — Tokenization
學習：
- Token
- Vocabulary
- BPE 概念
- Token ID

#### Week 20 — Embedding
學習：
- Token embedding
- Positional embedding
- Shape

#### Week 21 — Q / K / V
理解：

```text
Q = XWq
K = XWk
V = XWv
```

驗收：
- 用矩陣 shape 解釋每一步。

#### Week 22 — Self Attention
理解：

```text
softmax(QKᵀ / sqrt(dk))V
```

實作：
- Single-head Self Attention。

實驗：
- 移除 scaling 觀察數值差異。

#### Week 23 — Multi-Head Attention
學習：
- Head
- concat
- projection

實作：
- Multi-head Attention。

#### Week 24 — Transformer Block
整合：
- Causal Mask
- Attention
- Residual
- LayerNorm
- Feed Forward

驗收：
- 能白板解釋 Decoder-only Transformer。

---

## Phase 6 — Hugging Face
### Week 25–26｜12h

#### Week 25
學習：
- transformers
- AutoTokenizer
- AutoModelForCausalLM
- generate

#### Week 26
學習：
- datasets
- tokenizer pipeline
- model input / output
- Trainer / TrainingArguments 基礎

驗收：
- 能自行載入一個小型 pretrained model 並完成 inference。

---

## Phase 7 — Mini GPT from Scratch
### Week 27–30｜24h

限制：
最多四週，不追求大型模型。

#### Week 27
- Tokenizer
- Dataset
- Embedding

#### Week 28
- Attention
- Transformer Block

#### Week 29
- GPT Model
- Training Loop
- Cross Entropy

#### Week 30
- Generate
- Validation Loss
- Parameter Count
- README
- 實驗結果

驗收：
能回答：

> 一段文字輸入 GPT 後，如何一路變成下一個 token 的機率分布？

---

## Phase 8 — BankGPT v0.1 / FastAPI / PostgreSQL / Docker
### Week 31–32｜12h

#### Week 31 — LLM Application Basics
學習：
- System Prompt
- Temperature
- Top-p
- Context Window
- Structured Output

實作：
- BankGPT v0.1 基本聊天。

#### Week 32 — FastAPI + Docker
學習：
- FastAPI endpoint
- Async endpoint 基礎
- Pydantic v2 validation
- SQLAlchemy / PostgreSQL integration
- Dockerfile
- pytest / API test
- Secrets / environment variables

完成：

```text
User
 ↓
FastAPI
 ↓
LLM
 ↓
Structured Output
```

---

## Phase 9 — Embedding / Vector Search
### Week 33–34｜12h

#### Week 33
學習：
- Embedding
- Cosine similarity
- FAISS 作為本機 similarity-search library 的定位

實作：
- 不用 Vector DB，先自己算 Top-K similarity。

#### Week 34
學習：
- Vector DB
- Metadata
- Filter

建議：
- Qdrant（vector database）或 pgvector（PostgreSQL extension）擇一。

---

## Phase 10 — RAG
### Week 35–39｜30h

#### Week 35 — Basic RAG
完成：

```text
Document
 ↓
Chunk
 ↓
Embedding
 ↓
Retrieve
 ↓
Prompt
 ↓
LLM
```

BankGPT → v0.2。

同週建立：
- 10–20 題 baseline questions / expected sources。
- 最小 Retrieval Recall 與 citation 檢查。
- 文件來源與存取權限欄位。

#### Week 36 — Chunking
比較：
- chunk size
- chunk overlap
- baseline retrieval 指標

#### Week 37 — Vector DB
完成：
- persistence
- metadata
- filtering
- document-level access filter

#### Week 38 — Advanced Retrieval
學習：
- Hybrid Search
- Reranker
- 與 Week 35 baseline 比較

#### Week 39 — Citation / Debug
完成：
- Source citation
- Retrieval trace
- Failure analysis
- Request / retrieval logging

驗收：
- 能找出「是 retrieval 錯還是 generation 錯」。

---

## Phase 11 — LLM Evaluation
### Week 40–42｜18h

#### Week 40 — Golden Dataset
將 Week 35 baseline 擴充為：
- 20–50 個 Question / Expected Answer
- Expected Source
- Edge case / adversarial case

#### Week 41 — Metrics
評估：
- Retrieval Recall
- Answer Correctness
- Faithfulness
- Groundedness
- Latency

#### Week 42 — Experiment
比較：

```text
Chunk 256 vs 512
Top-K 3 vs 5
Reranker On vs Off
```

完成：
- 可重複執行的 regression test。
- 在 CI 中執行不需要外部付費模型的測試；付費或 GPU 評測保留為手動 workflow。

BankGPT → v0.3。

### 求職 Checkpoint

從 Week 42 起開始試投：

- AI Engineer
- AI Application Engineer
- GenAI Engineer
- LLM Engineer

不要等 Week 52。

---

## Phase 12 — Tool Calling + Agent
### Week 43–45｜18h

#### Week 43 — Tool Calling
學習：
- Tool schema
- Structured function call
- Tool result

建立：
- calculate_interest()
- get_product_information()
- Tool input validation

#### Week 44 — Backend Tool Integration
串接：
- SQL
- Internal API
- Error handling
- Permission boundary
- Read-only credential
- Table / operation allowlist
- Parameterized query
- Timeout / row limit / audit log

#### Week 45 — Agent
學習：
- Agent loop
- State
- Tool selection
- Retry
- Human-in-the-loop
- 高風險操作 approval gate

BankGPT → v0.4。

---

## Phase 13 — MCP
### Week 46｜6h

#### Week 46 — MCP Experiment

只要求理解並完成小型實驗：

- MCP Client
- MCP Server
- Tool
- Resource
- Prompt

不要投入過多時間。

---

## Phase 14 — Fine-tuning
### Week 47–48｜12h

執行前先確認：
- Base model license
- Dataset license / PII
- GPU / VRAM 或雲端預算
- 可重現的 Base Model evaluation

#### Week 47
學習：
- Pretraining vs SFT
- PEFT
- LoRA
- QLoRA

#### Week 48
實作：
- 對小模型做一次 domain SFT。
- 比較 Base Model vs Fine-tuned Model。

BankGPT → v0.5。

---

## Phase 15 — Model Serving
### Week 49–50｜12h

#### Week 49 — vLLM
學習：
- Local model serving
- OpenAI-compatible API
- batching

環境：
- 使用 Linux 或雲端 Linux 環境。
- 先記錄 GPU、VRAM、模型大小、dtype 與量化格式。

#### Week 50 — Inference Optimization
理解：
- FP32
- FP16
- BF16
- INT8
- INT4
- Quantization
- KV Cache
- Latency
- Throughput

實驗：
- 固定 prompt / output length，比較至少兩種 serving 設定。
- 記錄 latency、throughput、VRAM 與失敗條件。

不要求：
- 自己寫 CUDA kernel。

---

## Phase 16 — Production + Portfolio
### Week 51–52｜12h

#### Week 51 — Production
補強：
- Testing
- Logging
- Monitoring
- Security
- Authentication / Authorization
- Prompt Injection
- CI/CD
- Secrets management
- AWS / Azure / GCP 擇一完成小型部署
- Kubernetes Deployment / Service / ConfigMap / Secret 概念

範圍：
- 只要求完成一次部署、健康檢查與 rollback 演練。
- 不要求第一年成為 Kubernetes 平台維運專家。

#### Week 52 — Portfolio
完成：
- README
- Architecture Diagram
- Minimal Demo UI（Streamlit / Gradio / React 擇一）
- Demo
- Benchmark
- Evaluation Report
- Resume bullets

BankGPT → v1.0。

---

## 全年時數

| 階段 | Week | 時數 |
|---|---:|---:|
| Python / NumPy / Git / Linux / SQL | 1–4 | 24h |
| Math for ML | 5–8 | 24h |
| ML Fundamentals | 9–12 | 24h |
| Neural Network + PyTorch | 13–18 | 36h |
| Transformer | 19–24 | 36h |
| Hugging Face | 25–26 | 12h |
| Mini GPT | 27–30 | 24h |
| LLM + FastAPI + PostgreSQL + Docker | 31–32 | 12h |
| Embedding / Vector Search | 33–34 | 12h |
| RAG | 35–39 | 30h |
| Evaluation | 40–42 | 18h |
| Tool Calling / Agent | 43–45 | 18h |
| MCP | 46 | 6h |
| LoRA / QLoRA | 47–48 | 12h |
| vLLM / Serving | 49–50 | 12h |
| Production / Portfolio | 51–52 | 12h |
| **總計** | **52** | **312h** |

---

## 主教材策略

不要同時開太多教材。

### PyTorch
主教材：
- PyTorch Official Tutorials

### Transformer / Mini GPT
主教材：
- Stanford CS336 指定章節與 Assignment 1 相關內容
- 搭配自行實作，不要求在 6h / week 內完成整門 5-unit 課程

### LLM Ecosystem
主教材：
- Hugging Face LLM Course

### RAG / Agent / Serving
策略：
- 以官方文件 + BankGPT 實作為主。
- 遇到問題再查特定文章或課程。

---

## 每週完成定義

每週至少留下：

```text
1 個 Git Commit
+
1 份學習筆記
+
1 個可執行實驗
+
1 個自動或可重複執行的檢查
+
1 個「不看資料解釋」結果
```

若無法解釋，就不算真的完成。

---

## 學習紀錄模板

每週結束填寫：

```text
Week：
本週主題：

我現在能解釋：
-

我完成的程式：
-

我做過的實驗：
-

最重要的錯誤 / Debug：
-

Git Commit：
-

尚未理解：
-

下週第一件事：
-
```
