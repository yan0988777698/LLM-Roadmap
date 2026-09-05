# Progress Tracker

課程調整日期：2026-09-05。週次與必要驗收依 [52_WEEK_PLAN.md](52_WEEK_PLAN.md)。

## 狀態與時間

- ⬜ 未開始
- 🟨 進行中
- ✅ 完成
- ⏸ 暫停 / 延後

每週 6h，全年 48 週主線／288h + 4 週緩衝／24h = 312h。Week 13、23、35、48 為整合／補課週，選修不預占緩衝。

保留調整前已記錄的 Week 1 commit、Week 2 進行中狀態，以及 Week 5 的 MML §2.1–2.2 筆記與進度。Week 1–8 主題大致沿用；Week 9 起依新版重排，尚未開始的主題沒有標成完成。Week 5 原有 §2.4 待驗收紀錄保留作歷史註記，但此節在新版屬參考，不再阻擋該週完成。

Week 編號代表學習單元的預定週，不強迫對應固定日期。請在每週紀錄填實際日期與用時；同時學 Python／數學時共用 6h 預算。超時先補先備缺口、使用緩衝並順延依賴主題，不刪掉尚未完成的驗收。

## 年度總進度

MML 代表《Mathematics for Machine Learning》。章節欄只指定應用所需的定義、例題或參考；「複習」不需重新精讀。「外部補充」表示本書未直接涵蓋該主題。讀完教材是投入，完成本週實作／驗收才可標記 ✅。

| Week | 主題 | MML／教材範圍 | 狀態 | 成果 / Commit | 備註 |
| ---: | --- | --- | --- | --- | --- |
| 1 | Python Syntax for C# Developer | — | ✅ | 501acdc | 無 |
| 2 | Python Engineering Basics | — | 🟨 |  |  |
| 3 | NumPy + Matrix Bridge | §2.2 矩陣運算／shape；可先讀 | ⬜ |  |  |
| 4 | Git / Linux / SQL Bridge | — | ⬜ |  |  |
| 5 | Vector / Matrix / Dot Product | §2.1–2.2 沿用；§3.1–3.4 選定義／例子；§2.4 參考 | 🟨 | [MML 2.1 筆記](notes/math_for_machine_learning/02_linear_algebra/2.1_systems_of_linear_equations.md)、[MML 2.2 筆記](notes/math_for_machine_learning/02_linear_algebra/2.2_matrices.md) | 已完成 §2.1–2.2；§2.4、Dot Product、Norm 尚待驗收；調整後 §2.4 改為參考，原待驗收紀錄保留 |
| 6 | Matrix Multiplication / Linear Transformation | §2.2 複習；§2.7 選例子；§2.5–2.6 參考 | ⬜ |  |  |
| 7 | Calculus / Gradient | §5.1–5.2 選例題；§7.1 選更新式 | ⬜ |  |  |
| 8 | Probability / Softmax / Cross Entropy | §6.1–6.4 選離散例子；Softmax／CE 外部補充 | ⬜ |  |  |
| 9 | BankGPT: LLM Client + Structured Output | — | ⬜ |  |  |
| 10 | BankGPT: FastAPI + API Tests | — | ⬜ |  |  |
| 11 | BankGPT: PostgreSQL Integration | — | ⬜ |  |  |
| 12 | BankGPT v0.1: Docker + Local Demo | — | ⬜ |  |  |
| 13 | Buffer A: Foundation + API Integration | 按缺口複習 | ⬜ |  | 整合／補課，不新增必學 |
| 14 | ML: Dataset Split + Baseline | §8.1–8.2、§8.6 選資料切分／模型選擇 | ⬜ |  |  |
| 15 | ML: NumPy Linear Regression | §9.1–9.2 選線性模型／最小平方 | ⬜ |  |  |
| 16 | ML: NumPy Logistic Regression | Week 8 複習；Logistic Regression 外部補充 | ⬜ |  |  |
| 17 | ML: Training Experiment | §7.1、§8.6 複習 | ⬜ |  |  |
| 18 | PyTorch: Tensor + DataLoader | §2.2 複習 | ⬜ |  |  |
| 19 | PyTorch: First Complete MLP | §2.7 例子複習 | ⬜ |  |  |
| 20 | PyTorch: Backpropagation / Autograd | §5.2 複習；§5.6 選小型計算圖 | ⬜ |  |  |
| 21 | PyTorch: Optimizer Experiment | §7.1 複習 | ⬜ |  |  |
| 22 | PyTorch: Independent Loop + Checkpoint | §5.6、§7.1 按需複習 | ⬜ |  |  |
| 23 | Buffer B: ML / PyTorch Review | 按缺口複習 | ⬜ |  | 整合／補課，不新增必學 |
| 24 | Transformer: Tokenization + Next Token | Week 8 的條件機率複習 | ⬜ |  |  |
| 25 | Transformer: Token / Position Embedding | §2.2、§3.1–3.4 按需複習 | ⬜ |  |  |
| 26 | Transformer: Q / K / V + Single-Head Attention | §2.2、§3.2 複習；Week 8 Softmax | ⬜ |  |  |
| 27 | Transformer: Multi-Head Attention | §2.2 複習 | ⬜ |  |  |
| 28 | Transformer: Decoder Block | §2.2、§2.7 按需複習 | ⬜ |  |  |
| 29 | Hugging Face: Load + Generate | —；H 指定小節 | ⬜ |  |  |
| 30 | Hugging Face: Dataset + Batch Inputs | —；H 指定小節 | ⬜ |  |  |
| 31 | Mini GPT: Data + Model Assembly | Week 24–28 程式／筆記複習 | ⬜ |  |  |
| 32 | Mini GPT: Train + Validate | §5.6、§7.1 按需複習 | ⬜ |  |  |
| 33 | Mini GPT: Generate + Experiment | Week 8／24 複習 | ⬜ |  |  |
| 34 | Mini GPT: Explain + Report | 按缺口複習 | ⬜ |  |  |
| 35 | Buffer C: Model Integration + BankGPT Restart | 按缺口複習 | ⬜ |  | 整合／補課，不新增必學 |
| 36 | Retrieval: Embedding + Baseline | §3.1–3.4 的 norm／cosine 複習 | ⬜ |  |  |
| 37 | Retrieval: pgvector + Access Filter | Week 5 複習；V 指定段落 | ⬜ |  |  |
| 38 | RAG: Document Ingestion + Versioning | —；單一 parser 官方入門 | ⬜ |  |  |
| 39 | RAG: Answer + Citation + Evaluation | —；沿用 Week 36 baseline | ⬜ |  |  |
| 40 | RAG: Chunking + Retrieval Trace | —；沿用評估集 | ⬜ |  |  |
| 41 | RAG: One Retrieval Improvement | —；單一檢索改善 | ⬜ |  |  |
| 42 | BankGPT v0.2: RAG Integration | —；既有程式／案例 | ⬜ |  |  |
| 43 | Evaluation: Golden Dataset + Held-Out Set | §8.6 模型選擇複習 | ⬜ |  |  |
| 44 | BankGPT v0.3: Regression + Report | Week 14／43 複習 | ⬜ |  |  |
| 45 | Tool Calling: Validated Functions | — | ⬜ |  |  |
| 46 | Tools: Safe Backend Integration | — | ⬜ |  |  |
| 47 | BankGPT v0.4: Bounded Agent | — | ⬜ |  |  |
| 48 | Buffer D: Evaluation + Agent Integration | 按缺口複習 | ⬜ |  | 整合／補課，不新增必學 |
| 49 | Production: One Cloud Deployment | — | ⬜ |  |  |
| 50 | Production: Observability + Security Checks | — | ⬜ |  |  |
| 51 | Production: Release + Minimal UI | — | ⬜ |  |  |
| 52 | BankGPT v1.0: Portfolio + Resume | — | ⬜ |  |  |

## 重要 Checkpoint

| 時點 | 成果 |
|---|---|
| Week 12 | BankGPT v0.1：LLM client、FastAPI、PostgreSQL、tests、Docker、本機 Demo |
| Week 22 | 可獨立組織 PyTorch training／validation loop，保存與載入模型 |
| Week 28 | 可組裝與解釋 decoder-only Transformer block |
| Week 34 | Mini GPT、生成實驗與可重跑 README |
| Week 42 | BankGPT v0.2：RAG、citation、權限、10–20 題 baseline；達標可開始試投 |
| Week 44 | BankGPT v0.3：至少 20 題評估集、held-out、regression workflow |
| Week 47 | BankGPT v0.4：安全唯讀 tools、有停止條件的 agent |
| Week 52 | BankGPT v1.0：部署、最小 UI、評估報告、Demo 與履歷材料 |

Week 19 跟做完整 MLP 與 Week 22 獨立組織流程是不同層次的驗收。四個緩衝週只需記錄補課／重跑結果，不要求新功能。求職依作品是否達標，Week 42 可開始試投，Week 44 補 v0.3 報告。

## 進階選修追蹤

另排時間，不計入 312h。開始前填實際安排，不以預定週數推定已完成。

| 選修 | 狀態 | 預估另排 | 實際日期／用時 | 成果／證據 |
|---|---|---|---|---|
| MCP | ⏸ | 1–2 週／6–12h | | |
| SFT / LoRA 或 QLoRA | ⏸ | 3–4 週／18–24h | | |
| vLLM / Quantization | ⏸ | 2–3 週／12–18h | | |
| Kubernetes | ⏸ | 1–2 週／6–12h | | |
| Retrieval / Agent framework | ⏸ | 1–2 週／6–12h | | |

## 每週紀錄模板

### Week XX

實際日期：

-

實際用時（概念／實作與除錯／整理，合計）：

-

本週型態（一般／整合補課）：

-

學習目標：

-

MML／教材實際使用小節（必讀／參考）：

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

未通過驗收／是否影響先備／移入哪個緩衝或順延週：

-

下週第一件事：

-
