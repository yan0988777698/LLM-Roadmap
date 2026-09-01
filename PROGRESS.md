# Progress Tracker

狀態：

- ⬜ 未開始
- 🟨 進行中
- ✅ 完成
- ⏸ 暫停 / 延後

## 年度總進度

MML 代表《Mathematics for Machine Learning》。章節欄中的「複習」表示重用先前讀過的數學，不需要重新精讀；「外部教材」表示本書未直接涵蓋該主題。讀完章節只算學習投入，仍須完成該週實作與驗收才能標記為 ✅。

| Week | 主題 | MML 搭配章節 | 狀態 | 成果 / Commit | 備註 |
| ---: | --- | --- | --- | --- | --- |
| 1 | Python collections / syntax | — | ✅ | 501acdc | 無 |
| 2 | Python engineering basics / pytest | — | 🟨 | | |
| 3 | NumPy | — | ⬜ | | |
| 4 | Git / Linux / SQL Bridge | — | ⬜ | | |
| 5 | Vector / Matrix / Dot Product | §2.1–2.2、§2.4、§3.1–3.4 | 🟨 | [MML 2.1 筆記](notes/math_for_machine_learning/02_linear_algebra/2.1_systems_of_linear_equations.md) | 已完成線性方程組；Vector、Dot Product、Norm 尚待驗收 |
| 6 | Matrix Multiplication / Linear Transformation | §2.2、§2.5–2.7；§2.3、§3.8 選讀 | ⬜ | | |
| 7 | Calculus / Gradient | §5.1–5.6、§7.1 | ⬜ | | |
| 8 | Probability / Softmax / Cross Entropy | §6.1–6.5；Softmax / Cross Entropy 需外部教材 | ⬜ | | |
| 9 | Train / Validation / Test | §8.1–8.2、§8.6 | ⬜ | | |
| 10 | NumPy Linear Regression | §9.1–9.2；§3.8、§9.4 選讀 | ⬜ | | |
| 11 | NumPy Logistic Regression | §8.2–8.4 共通概念；Logistic Regression 需外部教材 | ⬜ | | |
| 12 | ML Training Concepts | §7.1、§8.1–8.3、§8.6；Batch / Epoch 等需外部教材 | ⬜ | | |
| 13 | PyTorch Tensor | §2.2 複習 | ⬜ | | |
| 14 | Neural Network | §2.7、§5.6 複習；神經網路需外部教材 | ⬜ | | |
| 15 | Forward Propagation | §2.7、§5.6 複習；網路實作需外部教材 | ⬜ | | |
| 16 | Backpropagation / Autograd | §5.2–5.6 | ⬜ | | |
| 17 | Optimizer / AdamW | §7.1；Adam / AdamW 需外部教材 | ⬜ | | |
| 18 | Complete PyTorch Training Loop | §5.6、§7.1、§8.2 複習；PyTorch 需外部教材 | ⬜ | | |
| 19 | Tokenization | —；需外部教材 | ⬜ | | |
| 20 | Embedding / Positional Embedding | §2.4、§3.1–3.4 複習；Embedding 需外部教材 | ⬜ | | |
| 21 | Q / K / V | §2.2、§2.7 複習；Attention 需外部教材 | ⬜ | | |
| 22 | Self Attention | §2.2、§3.2、§3.4 複習；Attention 需外部教材 | ⬜ | | |
| 23 | Multi-Head Attention | §2.2、§2.7 複習；Attention 需外部教材 | ⬜ | | |
| 24 | Transformer Block | §2.2、§2.7、§5.6 複習；Transformer 需外部教材 | ⬜ | | |
| 25 | Hugging Face Transformers | —；需外部教材 | ⬜ | | |
| 26 | Hugging Face Datasets / Trainer | —；需外部教材 | ⬜ | | |
| 27 | Mini GPT: Dataset / Embedding | §2.4、§3.2 複習；GPT 實作需外部教材 | ⬜ | | |
| 28 | Mini GPT: Attention / Block | §2.2、§3.2、§3.4 複習；GPT 實作需外部教材 | ⬜ | | |
| 29 | Mini GPT: Model / Training | §5.6、§7.1、§8.2 複習；GPT 實作需外部教材 | ⬜ | | |
| 30 | Mini GPT: Generation / README | —；需外部教材 | ⬜ | | |
| 31 | BankGPT v0.1 / LLM Basics | —；需外部教材 | ⬜ | | |
| 32 | FastAPI + PostgreSQL + Docker | —；需外部教材 | ⬜ | | |
| 33 | Embedding / Cosine Similarity | §3.1–3.4 複習 | ⬜ | | |
| 34 | Vector Database | §3.1–3.4 複習；Vector DB 需外部教材 | ⬜ | | |
| 35 | Basic RAG + Evaluation Baseline | §3.1–3.4 複習；RAG 需外部教材 | ⬜ | | |
| 36 | Chunking | —；需外部教材 | ⬜ | | |
| 37 | Vector DB / Metadata | —；需外部教材 | ⬜ | | |
| 38 | Hybrid Search / Reranker | —；需外部教材 | ⬜ | | |
| 39 | Citation / RAG Debug / Logging | —；需外部教材 | ⬜ | | |
| 40 | Golden Dataset | —；需外部教材 | ⬜ | | |
| 41 | LLM Evaluation Metrics | §6.4 複習；LLM 評估需外部教材 | ⬜ | | |
| 42 | RAG Regression Test + Job Checkpoint | §6.4、§8.6 複習；RAG 評估需外部教材 | ⬜ | | |
| 43 | Tool Calling | —；需外部教材 | ⬜ | | |
| 44 | Safe Backend Tool Integration | —；需外部教材 | ⬜ | | |
| 45 | Agent | —；需外部教材 | ⬜ | | |
| 46 | MCP | —；需外部教材 | ⬜ | | |
| 47 | LoRA / QLoRA Theory | §2.5–2.7、§4.5–4.6 | ⬜ | | |
| 48 | Fine-tuning Experiment | §4.6、§5.6、§7.1 複習；Fine-tuning 需外部教材 | ⬜ | | |
| 49 | vLLM / Linux Serving | —；需外部教材 | ⬜ | | |
| 50 | Inference Optimization | —；需外部教材 | ⬜ | | |
| 51 | Cloud / Production Engineering | —；需外部教材 | ⬜ | | |
| 52 | Demo UI / Portfolio / Resume / BankGPT v1.0 | —；需外部教材 | ⬜ | | |

## 重要 Checkpoint

### Week 18

應能：

- 不看教學寫基本 PyTorch training loop。

### Week 24

應能：

- 白板解釋 Decoder-only Transformer。

### Week 30

應有：

- Mini GPT from Scratch repository / module。

### Week 39

應有：

- BankGPT v0.2 RAG。
- 10–20 題 baseline、Expected Source 與 retrieval trace。

### Week 42

應有：

- BankGPT v0.3 Evaluation。
- 可重複執行的 regression test。
- 開始試投 AI / GenAI / LLM Application 職缺。

### Week 45

應有：

- BankGPT v0.4 Tool Calling / Agent。
- Read-only / allowlist / audit / approval 安全邊界。

### Week 48

應有：

- BankGPT v0.5 Fine-tuning experiment。

### Week 52

應有：

- BankGPT v1.0。
- Architecture Diagram。
- Evaluation Report。
- Minimal Demo UI。
- Demo。
- 可直接放履歷的 GitHub README。

## 每週紀錄模板

### Week XX

學習目標：

-

MML 搭配章節：

-

教材閱讀與筆記：

-

完成：

-

我現在能不看資料解釋：

-

實作 / Experiment：

-

測試 / 驗收：

-

遇到的問題：

-

Git Commit：

-

尚未理解：

-

下週第一件事：

-
