# Progress Tracker

課程調整日期：2026-09-05。週次與必要驗收依 [52_WEEK_PLAN.md](52_WEEK_PLAN.md)。

最近進度更新：2026-09-06。

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
| 1 | Python Syntax for C# Developer | — | ✅ | 501acdc | 2026-08-30 當天完成 |
| 2 | Python Engineering Basics | — | ✅ | 964dceb | 2026-08-31 開始 2026-09-07 完成 |
| 3 | NumPy + Matrix Bridge | §2.2 矩陣運算／shape；可先讀 | ⬜ |  |  |
| 4 | Git / Linux / SQL Bridge | — | ⬜ |  |  |
| 5 | Vector / Matrix / Dot Product | §2.1–2.2 沿用；§3.1–3.4 選定義／例子；§2.4 參考 | 🟨 | [MML 2.1 筆記](notes/math_for_machine_learning/02_linear_algebra/2.1_systems_of_linear_equations.md)、[MML 2.2 筆記](notes/math_for_machine_learning/02_linear_algebra/2.2_matrices.md) | 2026-08-31 開始 |
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

## 學習紀錄

每個學習週使用下方「每週紀錄模板」的全部欄位；同一週分次學習時，更新同一份紀錄並保留各次日期與成果，不以最新一筆覆蓋較早進度。總進度表同步維護整週狀態。

以下 Week 1、Week 2、Week 5 依既有文件、Git 與對話補登。Git 日期只證明當時已有該項進度紀錄；未提供的實際日期、用時、獨立解釋與驗收結果明確標註，不以課表預估補成實際時數。

### Week 1 — Python Syntax（✅ 完成）

實際日期：

- 2026-08-30：當天完成 Week 1。

實際用時（概念／實作與除錯／整理，合計）：

- 概念／實作與除錯／整理／合計：2 hrs。

本週型態（一般／整合補課）：

- 一般；本筆依既有練習 README 與 Git 歷史補登。

學習目標：

- 熟悉 List／Dict／Set／Tuple、comprehension、enumerate／zip。
- 將熟悉的 C# 小題改寫為 Python，能解釋資料結構選擇與時間／空間複雜度。

MML／教材實際使用小節（必讀／參考）：

- MML：無指定章節。
- 實際教材：[Week 1 練習紀錄](exercises/week01_python_syntax/README.md)。

教材閱讀與筆記：

- 已有 Python collections 與 Two Sum 的程式、說明與驗收紀錄，沿用原有成果。

完成：

- [x] 完成 `collections_demo.py` 與 `two_sum.py`。
- [x] 原練習紀錄記載 Two Sum 三個案例通過。
- [x] Week 1 在總進度表標記為 ✅。

知識檢核：

- List／Tuple／Set／Dict 的差異與 comprehension 的用途。
- Two Sum 為何使用 Dict，以及時間／空間複雜度。

實作 / Experiment：

- [week01_python_syntax](exercises/week01_python_syntax/README.md)。
- [collections_demo.py](exercises/week01_python_syntax/collections_demo.py)：collection 操作。
- [two_sum.py](exercises/week01_python_syntax/two_sum.py)：以 Dict 解題。

測試 / 驗收：

- `collections_demo.py` 執行成功，Two Sum 三個測試案例通過。
- Two Sum 時間複雜度 O(n)、空間複雜度 O(n)。

遇到的問題：

- 無。

Git Commit：

- `501acdc`：Python 語法與 Two Sum 練習成果（2026-08-30）。
- `742a817`：將 Week 1 標記完成（2026-08-30）。

尚未理解：

- 無。

未通過驗收／是否影響先備／移入哪個緩衝或順延週：

- 無。

下週第一件事：

- 建立 Week 2 的 Python package 與 pytest 環境。

### Week 2 — Python Engineering Basics（🟨 進行中）

實際日期：

- 2026-08-31：開始 Week 2 與 Week 5；目前進行中。
- 2026-09-07：Week 2 在總進度表標記為 ✅。

實際用時（概念／實作與除錯／整理，合計）：

- 概念／實作與除錯／整理／合計：4hrs。

本週型態（一般／整合補課）：

- 一般；依進度進行。

學習目標：

- 使用 venv／pip、module／package 與 src layout。
- 練習 class／dataclass、typing、exception、generator 與 pytest。

MML／教材實際使用小節（必讀／參考）：

- MML：本週無指定章節。
- 實際教材：[Week 2 Python Engineering 練習](exercises/week02_python_engineering/README.md)，包含專案結構、環境指令、練習順序與完成標準。

教材閱讀與筆記：

- banking package 練習與測試檔案。

完成：

- [x] 建立 .venv 虛擬環境，並安裝 pytest。
- [x] 使用 pytest 通過 banking 內的所有測試案例。

知識檢核：

- package／`__init__.py`、dataclass、type hint 與 runtime validation、generator 的用途。

實作 / Experiment：

- [week02_python_engineering](exercises/week02_python_engineering/README.md)。
- [test_account.py](exercises/week02_python_engineering/tests/test_account.py)：測試案例。
- [test_generators.py](exercises/week02_python_engineering/tests/test_generators.py)：測試案例。

測試 / 驗收：

- 測試案例皆已通過。

遇到的問題：

- 無。

Git Commit：

- `c7f3730`：新增練習骨架與更新進度（2026-09-01）。
- `964dceb`：紀錄為已完成（2026-09-07）。

尚未理解：

- 無。

未通過驗收／是否影響先備／移入哪個緩衝或順延週：

- 驗收狀態尚未回報；無。

下週第一件事：

- 本週驗收後接 Week 3 NumPy，搭配 §2.2 矩陣例子。

### Week 5 — Vector / Matrix / Dot Product（🟨 進行中）

實際日期：

- 2026-08-31：開始 Week 5，與 Week 2 並行；目前進行中。
- 2026-09-01：MML.pdf §2.1 線性方程組已讀完（書本頁碼 19 - 21）；[2.1_systems_of_linear_equations.md](notes\math_for_machine_learning\02_linear_algebra\2.1_systems_of_linear_equations.md) 閱讀完成
- 2026-09-06：MML.pdf §2.2 Matrices 已讀完（書本頁碼 22 - 26）。
- 2026-09-07：[2.2_matrices.md](notes\math_for_machine_learning\02_linear_algebra\2.2_matrices.md) 閱讀完成

實際用時（概念／實作與除錯／整理，合計）：

- 概念／實作與除錯／整理／合計：MML.pdf §2.1 2hrs ；MML.pdf §2.2 2hrs。

本週型態（一般／整合補課）：

- 一般；持續更新中。

學習目標：

- 理解向量、矩陣、dot product、norm 與 cosine similarity。
- 能手算並用 NumPy 驗證，解釋內積與 cosine 的差別，以及零向量的限制。

MML／教材實際使用小節（必讀／參考）：

- 已讀：MML §2.1–2.2。
- 下一段必讀：§3.1–3.4 中 norm／inner product／distance／angle 的指定定義與例子。
- 參考：§2.4；按書順序的 §2.3 可補充選讀，不是本週前進門檻。

教材閱讀與筆記：

- [§2.1 線性方程組筆記](notes/math_for_machine_learning/02_linear_algebra/2.1_systems_of_linear_equations.md)。
- [§2.2 矩陣筆記](notes/math_for_machine_learning/02_linear_algebra/2.2_matrices.md)。

完成：

- [x] §2.1 閱讀完成；筆記完成。
- [x] §2.2 閱讀完成；筆記完成。
- Week 5 保持 🟨：內積／norm／cosine 的實作與整週驗收尚未記錄完成。
- Week 5 保持 🟨：§2.1 §2.2 numpy練習尚未記錄完成。

知識檢核：

- 矩陣乘法 shape、轉置乘積的反序、逆轉置公式，以及 Ax 作為欄向量線性組合。

實作 / Experiment：

- [2.1_systems_for_linear_equations.py](exercises/math_for_machine_learning/02_linear_algebra/2.1_system_of_linear_equations.py) NumPy 練習。
- [2.2_matrices.py](exercises/math_for_machine_learning/02_linear_algebra/2.2_matrices.py) NumPy 練習。
- 使用者自行手算或執行 NumPy 的結果：尚未回報。

測試 / 驗收：

- §2.2 自我檢查：尚未回報結果。
- Dot product／norm／cosine 手算與 NumPy 比對：待完成。
- 整週驗收：需能解釋內積與 cosine 的差別、零向量不能直接進行 cosine normalization。

遇到的問題：

- 曾詢問逆轉置公式的符號意義，以及取反矩陣和轉置為何可以交換順序；已在對話中解釋。
- 另有 PDF 頁碼定位需求，已確認 PDF 第 32 頁對應書本頁碼 26。

Git Commit：

- `c7f3730`：§2.1 筆記與 Week 5 進行中紀錄（2026-09-01）。
- `964dceb`：§2.2 筆記（2026-09-07）。

尚未理解：

- 逆轉置等概念已討論，是否能獨立重建推導尚待自我檢查。
- §3.1–3.4 的指定內容與實作尚未記錄完成；不將尚未學習等同驗收失敗。

未通過驗收／是否影響先備／移入哪個緩衝或順延週：

- 閱讀完成；本週實作與獨立解釋尚未完成驗收，也未記錄為測試失敗。
- 若 shape／內積／norm 缺口影響 Week 6 或後續 NumPy 練習，先補先備，必要時使用 Week 13 緩衝並順延；目前尚無確定延期紀錄。

下週第一件事：

- 先花約 15–20 分鐘自我檢查 §2.2，再讀 §3.1 的 norm，接續 §3.2–3.4 的指定定義與例子。
- 用兩個小向量手算 dot product、norm、cosine，再以 NumPy 驗證；程式線沿用 Week 2 → Week 3 的安排。

## 規劃變更紀錄

### 2026-09-05｜課程與時程調整

- 完成 52 週課程 review 與排程調整，保留每週 6h／全年 312h，加入四週整合／補課。
- BankGPT 提前至 Week 9–12；MCP、微調、vLLM、Kubernetes 改為進階選修，MML 改為指定定義與例題。
- 同步六份規劃文件與既有進度；commit：`a7b9f59`。
- 本項是規劃變更，不計為新增課程完成或實作驗收；不套入學習週的完成狀態。

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

知識檢核：

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
