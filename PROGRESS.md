# Progress Tracker

課程調整日期：2026-09-05。週次與必要驗收依 [52_WEEK_PLAN.md](52_WEEK_PLAN.md)。

最近進度更新：2026-09-19。

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
| 3 | NumPy + Matrix Bridge | §2.2 矩陣運算／shape；可先讀 | ✅ | [Week 3 學習與練習](exercises/week03_numpy_matrix_bridge/README.md) | 2026-09-13 開始；2026-09-19 完成 |
| 4 | Git / Linux / SQL Bridge | — | ✅ | [Week 4 學習與練習](exercises/week04_git_linux_sql_bridge/README.md) | 2026-09-19 當天完成 |
| 5 | Vector / Matrix / Dot Product | §2.1–2.2 沿用；§3.1–3.4 選定義／例子；§2.4 參考 | 🟨 | [MML 2.1 筆記](notes/math_for_machine_learning/02_linear_algebra/2.1_systems_of_linear_equations.md)、[MML 2.2 筆記](notes/math_for_machine_learning/02_linear_algebra/2.2_matrices.md)、[§2.1 NumPy 練習](exercises/math_for_machine_learning/02_linear_algebra/2.1_system_of_linear_equations.py)、[§2.2 NumPy 練習](exercises/math_for_machine_learning/02_linear_algebra/2.2_matrices.py) | 2026-08-31 開始；2026-09-13 §2.1–2.2 練習與自我檢查完成；待 §3.1–3.4 與整週驗收 |
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

- 開始 Week 2 Python Engineering Basics。

### Week 2 — Python Engineering Basics（✅ 完成）

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

- 開始 Week 3 NumPy + Matrix Bridge。

### Week 3 — NumPy + Matrix Bridge（✅ 完成）

實際日期：

- 2026-09-13：開始 Week 3；建立 NumPy 學習指引、示範與獨立練習骨架。
- 2026-09-19：完成 shape／slicing／reshape、矩陣乘法與 broadcasting 練習，記錄投入 4 小時，並以 `27ef8a5` 提交成果。

實際用時（概念／實作與除錯／整理，合計）：

- 合計 4 小時。

本週型態（一般／整合補課）：

- 一般課程。

學習目標：

- 理解 ndarray、shape、slicing、reshape、broadcasting，以及 `*` 與 `@` 的差異。
- 用小矩陣計算 `X @ W + b`，先預測 batch × feature 的輸出 shape，再驗證數值。

MML／教材實際使用小節（必讀／參考）：

- 必讀：[Week 3 學習指引](exercises/week03_numpy_matrix_bridge/README.md)；既有紀錄已勾選完成，搭配其中的 NumPy 官方入門連結查閱。
- 複習：MML §2.2 的矩陣運算與 shape，沿用既有筆記與練習。

教材閱讀與筆記：

- 以 C# 陣列經驗對照 NumPy `ndarray`，觀察 `shape`、`ndim`、`size`、`dtype`。示範的二維資料為 `(2, 3)`、2 維、6 個元素、`float64`。
- 在 `matrix_bridge.py` 留下切片、逐元素乘法、矩陣乘法與 `X @ W + b` 的預期結果註解，再與輸出核對。
- 切片重點：`X[0]` 得到 `(3,)`；`X[:1]` 等同 `X[0:1]`，取第一列並保留第一個軸，得到 `(1, 3)`。`X[:, 0]` 是 `(2,)`；`X[:, :1]` 取所有列、第一欄並保留第二個軸，得到 `(2, 1)`。
- `reshape(3, 2)` 重新安排元素的形狀，不等於交換列欄的 `X.T`；基本切片共享資料，使用 `.copy()` 後修改副本不會改到原矩陣。
- batch 表示一次處理多筆資料：`X` 每列一筆、每欄一個輸入特徵；`W` 將輸入特徵組合成輸出特徵，`b` 對每筆資料加上相同的輸出偏移。
- 跟做範圍為 `matrix_bridge.py` 的 basics／multiply／broadcast；作答成果保存在 `practice.py` 的五個 TODO。既有紀錄標記獨立驗收完成，本次以檔案與重跑結果補充證據。

完成：

- [x] 建立學習指引、可執行示範與 TODO 練習骨架。
- [x] 建立本週 `.venv` 並安裝 NumPy 2.5.3；示範與練習檢查已由助手驗證。
- [x] 完成 shape／slicing／reshape 練習。
- [x] 手算並以 NumPy 驗證 `X @ W + b`。
- [x] 解釋 `*` 與 `@`，找出並修正 broadcasting 錯誤。
- [x] 完成獨立驗收與實際用時紀錄。

知識檢核：

- `(3,)` 與 `(1, 3)` 的差別、切片是否保留維度。
- 矩陣乘法的內側維度與 broadcasting 從右側對齊的規則。
- 程式可以執行時，偏移仍可能加在錯誤的軸上。
- `*` 是對應位置逐元素相乘；`@` 在本週二維矩陣情境中，是左矩陣的一列與右矩陣的一欄相乘加總。
- `(4, 3) @ (3, 2) + (2,)` 的輸出為 `(4, 2)`：4 筆資料各得到 2 個輸出。batch 大小改變時，輸出列數跟著改變；輸入特徵仍須與 `W` 的第一軸相容。
- 對 `(4, 2)` 加 `(3,)`，最右側軸的 2 與 3 不相同，也沒有任一方為 1，因此不相容；每個輸出欄位各加 10、20 時，偏移應為 `(2,)`。
- 對示範的 `(2, 2)` 輸出，加 `(2,)` 是每個欄位一個偏移；加 `feature_bias.reshape(2, 1)` 則是每筆資料一個偏移。兩者都能執行，但意義不同。

實作 / Experiment：

- [matrix_bridge.py](exercises/week03_numpy_matrix_bridge/matrix_bridge.py)：跟做 basics、multiply、broadcast；示範 `X @ W + b` 的結果為 `[[14, 25], [20, 31]]`，shape 為 `(2, 2)`。
- [practice.py](exercises/week03_numpy_matrix_bridge/practice.py)：五個 TODO 已作答。預測 shape 為 `(4, 2)`；以 `X[:1, :]` 保留第一筆資料的二維形狀；以 `b.reshape(1, 2)` 建立偏移列。
- 練習填入的手算結果為 `[[3, 6], [2, 8], [6, 1], [4, 3]]`，與 `X @ W + b` 核對一致；將不相容的三元素偏移修正為 `[10, 20]`，並註明最後一軸不相容。

測試 / 驗收：

- 學習完成紀錄（2026-09-19）：README 與本節已勾選跟做、獨立練習與整週驗收完成，投入 4 小時；目前檔案中的五個 TODO 均已有答案。
- 本次重跑：`.\.venv\Scripts\python.exe matrix_bridge.py all` 完成。
- 本次重跑：`.\.venv\Scripts\python.exe practice.py` 完成。

遇到的問題：

- 切片觀念：曾對 `X[:1]` 與 `X[:, :1]` 的取值方向，以及結果為何保留二維感到疑惑。比較時要先確定原始矩陣，並分清「取出的數值」與「shape」。以下使用示範中的 2 列、3 欄資料：

| 寫法 | 取法 | 結果 | shape |
| --- | --- | --- | --- |
| `X[0]` | 用整數索引取第一列 | `[1, 2, 3]` | `(3,)` |
| `X[:1]` | 用切片取第一列，等同 `X[0:1, :]` | `[[1, 2, 3]]` | `(1, 3)` |
| `X[:, 0]` | 取所有列，用整數索引取第一欄 | `[1, 4]` | `(2,)` |
| `X[:, :1]` | 取所有列，用切片取第一欄 | `[[1], [4]]` | `(2, 1)` |

- 二維索引寫成 `X[列, 欄]`：逗號前控制列，逗號後控制欄。單獨的 `:` 表示該軸全部；`:1` 等同 `0:1`，包含起點 0、不包含終點 1，因此只取索引 0，不是取索引 1。
- 整數索引 `0` 會移除對應的軸；切片 `:1` 會保留該軸，只將長度變成 1。因此 `X[0]` 與 `X[:1]` 取出的數值相同，shape 卻不同。
- shape 表示每個軸的長度，不是資料值：`(3,)` 是一維、3 個元素；`(1, 3)` 是二維、1 列 3 欄；`(2, 1)` 是二維、2 列 1 欄。一維陣列沒有額外的列／欄軸。
- 上表依據示範的 `X.shape == (2, 3)`。練習檔中的 `X.shape == (4, 3)`，所以 `X[:, 0]` 會是 `(4,)`，`X[:, :1]` 會是 `(4, 1)`；切片規則相同，結果長度隨原始資料改變。

Git Commit：

- `a71bf96`（2026-09-13）：建立 Week 3 NumPy 矩陣示範與練習。
- `27ef8a5`（2026-09-19）：更新進度與 NumPy 練習作答，記錄本週完成。

尚未理解：

- 無。

未通過驗收／是否影響先備／移入哪個緩衝或順延週：

- 無。

下週第一件事：

- 開始 Week 4 Git／Linux／SQL Bridge。

### Week 4 — Git / Linux / SQL Bridge（✅ 完成）

實際日期：

- 2026-09-19：開始 Week 4；建立 CLI／環境變數練習、PostgreSQL CRUD／transaction 示範與四個 SQL TODO。
- 2026-09-19：學習者回報 `cli_env.py` 完成；接續 Linux shell 基礎操作，再進入資料庫連線與查詢。
- 2026-09-19：排除 PostgreSQL 主機 port 問題，完成四個 CRUD TODO；助手執行目前的 `practice.py`，全部檢查通過。補充 Docker 常用語法筆記，總表已標記本週當天完成。

實際用時（概念／實作與除錯／整理，合計）：

- 4hrs。

本週型態（一般／整合補課）：

- 一般；沿用 repository 與既有 C#／SQL 經驗，補 Python driver、CLI 與環境設定。

學習目標：

- 從命令列參數與環境變數啟動程式，說明工作目錄與基本 shell 指令。
- 在一張合成產品表完成 PostgreSQL 參數化 CRUD，驗證 transaction 的提交與回復。
- 說明 Git commit／branch，以及 JOIN／index 的用途。

MML／教材實際使用小節（必讀／參考）：

- 本週無新增 MML 章節。
- 必讀：[Week 4 學習指引](exercises/week04_git_linux_sql_bridge/README.md)，依序完成「今天先做」、資料庫示範與獨立練習。
- 參考：指引內連結的 Psycopg、PostgreSQL、Git 官方指定說明；Linux／SQL 只補目前缺口。

教材閱讀與筆記：

- 使用 [Week 4 學習指引](exercises/week04_git_linux_sql_bridge/README.md)，將既有 SQL 經驗接到 Python 的 Psycopg driver、參數 tuple 與查詢結果處理。
- [Docker Compose 與 Shell 筆記](notes/week04/docker_compose_shell.md)：整理 PowerShell／Linux shell 的差別，補充容器啟停、狀態、日誌、port 映射、`psql`、volume，以及一般 Docker 與 Compose 指令對照。
- 本次問答涵蓋 Docker Desktop／Engine 的角色、資料庫何時建立、PostgreSQL 預設 port、停止與重建容器的差別，以及 YAML 和 Python 連線設定如何保持一致。
- 跟做／協助範圍：環境建立與排錯由助手協助；INSERT 寫法經助手檢視，並提供括號串接字串的範例。學習者已填入四個 CRUD SQL；助手未代填本次其餘三個 TODO。不看範例重寫與口頭解釋的結果尚未記錄。

完成：

- [x] 建立學習指引、可執行示範、四個 SQL TODO 與驗收檢查。
- [x] 建立本週 `.venv`（Python 3.13.12／Psycopg 3.3.6）與本機 PostgreSQL 17.11；助手已驗證環境。
- [x] 完成 `cli_env.py` 的 CLI／環境變數練習（學習者回報完成；實際用時與獨立完成範圍待補）。
- [x] 填完四個參數化 CRUD TODO，保留下方檢查；目前程式已實際通過全部檢查。
- [x] 完成 Docker port 排錯，確認 Windows 上的 Python 可以連線 PostgreSQL。
- [x] 補充 Docker 常用指令與本次排錯筆記。
- [x] 補記 Linux shell 操作與工作目錄／相對路徑的個人解釋。
- [x] 補記含引號輸入、SQL 參數、transaction rollback、commit／branch、JOIN／index 的個人解釋。

知識檢核：

- 環境變數與命令列參數如何進入 Python；新終端機與子程序的差別。
- `%s` 與參數 tuple 分開傳入；單元素 tuple 的逗號、WHERE 條件與 rowcount。
- DB transaction 中一個操作失敗時，先前成功的操作也要撤銷。
- Git commit、Git branch 與資料庫 commit 各自的用途。

實作 / Experiment：

- [cli_env.py](exercises/week04_git_linux_sql_bridge/cli_env.py)：2026-09-19 完成。
- [db_bridge.py](exercises/week04_git_linux_sql_bridge/db_bridge.py)：作為 check、init、list、crud、rollback 示範，2026-09-19 完成。
- [practice.py](exercises/week04_git_linux_sql_bridge/practice.py)：完成 INSERT 三欄並回傳 id、依名稱 SELECT、依 id UPDATE stock、依 id DELETE；SQL 使用 `%s` 佔位符與 tuple 分開傳值，2026-09-19 完成。

測試 / 驗收：

- 教材驗證（2026-09-19）：CLI 預設值／自訂值、負數參數、不同工作目錄、不輸出密碼與缺少設定提示通過。
- PostgreSQL 教材驗證：連線、初始化／重跑保留資料、價格查詢、CRUD、引號輸入、負庫存 rollback 與回復後查詢通過；這是前面的環境與示範驗證。
- 作答檢查涵蓋：新增欄位值正確、含引號名稱、查無資料回傳 `None`、注入樣式文字當成資料、指定 id 更新、負庫存拒絕與回復後可查詢、重複刪除回傳 0，以及保留其他產品。
- CRUD 程式驗收已通過；Linux 操作、完整 transaction 示範的個人解釋，以及 Git／JOIN／index 概念的獨立回答尚未逐項記錄。

遇到的問題：

- Docker Desktop 與 Engine：先啟動 Docker Desktop 管理的引擎，CLI 才能操作本機容器；視窗不必留在前景。
- Windows Port 保留範圍為 `55354–55453`，db port 改以 `127.0.0.1:5432` 運作且 Python 連線成功。
- Python 顯示 `Cannot connect`：修改 YAML 後用 `up -d --wait` 套用，`stop`／`start` 或 `restart` 不會套用新 port。
- TODO 2 提示：INSERT 已通過，程式接著執行尚未作答的 SELECT；並非新增 SQL 出錯。補完其餘 TODO 後，整份檢查通過。

Git Commit：

- 本週 commit hash 待補；目前最新 commit 為 `27ef8a5`（Week 3）。整理本週檔案與筆記後，檢查 `git diff`／暫存內容，再提交並記錄 hash。

尚未理解：

- 無。

未通過驗收／是否影響先備／移入哪個緩衝或順延週：

- 無。

下週第一件事：

- 接續已開始的 Week 5 數學單元；沿用已完成的向量／矩陣練習。

### Week 5 — Vector / Matrix / Dot Product（🟨 進行中）

實際日期：

- 2026-08-31：開始 Week 5，與 Week 2 並行；目前進行中。
- 2026-09-01：MML.pdf §2.1 線性方程組已讀完（書本頁碼 19 - 21）；[2.1_systems_of_linear_equations.md](notes/math_for_machine_learning/02_linear_algebra/2.1_systems_of_linear_equations.md) 閱讀完成
- 2026-09-06：MML.pdf §2.2 Matrices 已讀完（書本頁碼 22 - 26）。
- 2026-09-07：[2.2_matrices.md](notes/math_for_machine_learning/02_linear_algebra/2.2_matrices.md) 閱讀完成
- 2026-09-13：[2.1_system_of_linear_equations.py](exercises/math_for_machine_learning/02_linear_algebra/2.1_system_of_linear_equations.py) 練習完成。
- 2026-09-13：[2.2_matrices.py](exercises/math_for_machine_learning/02_linear_algebra/2.2_matrices.py) 練習完成。

實際用時（概念／實作與除錯／整理，合計）：

- 概念／實作與除錯／整理／合計：MML.pdf §2.1 2+1+1=4hrs ；MML.pdf §2.2 2+1+1=4hrs。

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

- [x] §2.1 閱讀、筆記、NumPy 練習與自我檢查完成。
- [x] §2.2 閱讀、筆記、NumPy 練習與自我檢查完成。
- [ ] §3.1–3.4：norm／inner product／distance／angle 的指定定義與例子。
- [ ] Dot product／norm／cosine 手算與 NumPy 比對，以及整週驗收。
- Week 5 保持 🟨：內積／norm／cosine 的實作與整週驗收尚未記錄完成。

知識檢核：

- 矩陣乘法 shape、轉置乘積的反序、逆轉置公式，以及 Ax 作為欄向量線性組合。

實作 / Experiment：

- [2.1_system_of_linear_equations.py](exercises/math_for_machine_learning/02_linear_algebra/2.1_system_of_linear_equations.py)：以矩陣秩判斷無解／唯一解／無限多解，使用 `np.linalg.solve` 求解並比對 `Ax = b`。
- [2.2_matrices.py](exercises/math_for_machine_learning/02_linear_algebra/2.2_matrices.py)：矩陣乘法與 shape、轉置乘積、單位矩陣、線性方程組求解，以及 Q／K 注意力分數矩陣的 shape 練習。

測試 / 驗收：

- §2.1 自我檢查：完成。
- §2.2 自我檢查：完成。
- Dot product／norm／cosine 手算與 NumPy 比對：待完成。
- 整週驗收：需能解釋內積與 cosine 的差別、零向量不能直接進行 cosine normalization。

遇到的問題：

- 暫無。

Git Commit：

- `c7f3730`：§2.1 筆記與 Week 5 進行中紀錄（2026-09-01）。
- `964dceb`：§2.2 筆記（2026-09-07）。

尚未理解：

- 逆轉置等概念已討論，是否能獨立重建推導尚待自我檢查。
- §3.1–3.4 的指定內容與實作尚未記錄完成；不將尚未學習等同驗收失敗。

未通過驗收／是否影響先備／移入哪個緩衝或順延週：

- §2.1–2.2 閱讀、筆記、NumPy 練習與自我檢查完成；§3.1–3.4、dot product／norm／cosine 實作與整週獨立解釋仍待完成，未記錄為測試失敗。
- 若 shape／內積／norm 缺口影響 Week 6 或後續 NumPy 練習，先補先備，必要時使用 Week 13 緩衝並順延；目前尚無確定延期紀錄。

下週第一件事：

- 閱讀 §3.1 的 norm，接續 §3.2–3.4 的 inner product／distance／angle 指定定義與例子。
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
