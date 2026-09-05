# 52-Week Learning Plan

調整日期：2026-09-05。以本檔為週次與必要驗收的唯一排程依據；[ROADMAP.md](ROADMAP.md) 是能力地圖，[PROGRESS.md](PROGRESS.md) 記錄實際進度。

## 時間預算與範圍

- 前提：已有一般軟體工程與 C# 開發經驗，Python／ML 依入門程度安排。
- 每週 6 小時 × 52 週 = **312 小時**，包含閱讀、環境設定、除錯、實驗與筆記。
- **48 週主線＝288 小時；4 週整合／補課＝24 小時**。緩衝為 Week 13、23、35、48，不預排新課程。
- 第一年成果：可測試與部署的 BankGPT、模型訓練與 Transformer 基礎、四週 Mini GPT。
- MCP、LoRA／QLoRA、vLLM、Kubernetes、完整 CS336 作業屬進階選修，沒有第一年強制完成週次，也不是 BankGPT v1.0 的依賴。
- 模型學習以 CPU 可跑的小實驗為起點；BankGPT 主線選一個 API 模型。API 費用另記，GPU 並非主線必備。
- 本計畫限制在公開／授權／合成資料的 Portfolio Demo。安全與測試從第一個 API 持續加入。

### 每週工作方式

一般週以 1.5h 概念、3.5h 實作／除錯、1h 整理／解釋為起點。數學週可改為 2h 概念、3h 手算／NumPy 驗證、1h 整理；總投入仍為 6h。不同主題並行時共用這 6h，不各自再加一份預算。

1. 先回想上週重點 10–15 分鐘，計入概念時間。
2. 只讀當週實驗需要的小節，讀完立即做數值例子或修改程式。
3. 每週完成一個主要實驗與其必要檢查，後續沿用同一程式，不強迫新建專案。
4. 筆記只記概念、實驗結果與尚未理解之處；不用重寫整章教材。訓練／生成實驗保留設定與 seed，API 實驗保留模型與 prompt 版本。
5. 可查 API 簽名；驗收重點是能自己組織流程、解釋與除錯。應區分跟做完成與獨立完成。

### 落後時如何調整

- 必學是本週「驗收」；參考章節與延伸題不構成過關條件。
- 超出 6h 就記錄實際進度，移入下一個緩衝週；不要靠固定加班維持表面進度。
- 影響後續先備知識的缺口，先用一週補齊並將依賴它的週次順延至緩衝，不硬接新主題。
- 緩衝未用滿時，做重建、重跑與文件整理，不自動補入選修。
- 四週緩衝仍不足時，按缺口延長日曆時程並更新進度表；312h 是規劃預算，不是學會所有主題的保證。

## 全年安排

| 階段 | Week | 時數 |
|---|---:|---:|
| 工程基礎 | 1–4 | 24h |
| Math for ML | 5–8 | 24h |
| BankGPT v0.1 / API Engineering | 9–12 | 24h |
| Buffer A | 13 | 6h |
| ML Fundamentals | 14–17 | 24h |
| Neural Network + PyTorch | 18–22 | 30h |
| Buffer B | 23 | 6h |
| Transformer | 24–28 | 30h |
| Hugging Face | 29–30 | 12h |
| Mini GPT from Scratch | 31–34 | 24h |
| Buffer C | 35 | 6h |
| Embedding / RAG / BankGPT v0.2 | 36–42 | 42h |
| Evaluation / BankGPT v0.3 | 43–44 | 12h |
| Tool Calling / Agent / BankGPT v0.4 | 45–47 | 18h |
| Buffer D | 48 | 6h |
| Production / Deployment / UI | 49–51 | 18h |
| Portfolio / BankGPT v1.0 | 52 | 6h |
| **總計** | **52** | **312h** |

## 每週計畫

### 工程基礎｜Week 1–4｜24h

#### Week 1 — Python Syntax for C# Developer

- **學習：** Python collections、comprehension、enumerate／zip。
- **教材範圍：** Python 官方教學中資料結構與控制流程的小節；沿用現有 Week 1 練習。
- **實作：** 將 2–3 題熟悉的 C# 小題改寫為 Python，保留現有 collections_demo 與 Two Sum 成果。
- **驗收：** 能選擇 List／Tuple／Set／Dict，解釋操作與時間複雜度；可查 API 名稱。

#### Week 2 — Python Engineering Basics

- **學習：** venv／pip、module／package、class／dataclass、typing、exception、generator、pytest。
- **教材範圍：** 沿用 exercises/week02_python_engineering/README.md；一次只查當下使用的語法。
- **實作：** 完成現有 banking package 的 TODO 與測試，不額外建立第二個練習專案。
- **驗收：** 測試通過；能解釋 package、type hint 與 runtime validation 的差別，以及 generator 的用途。

#### Week 3 — NumPy + Matrix Bridge

- **學習：** ndarray、shape、slicing、reshape、broadcasting、element-wise 與 matrix multiplication。
- **教材範圍：** NumPy 官方入門；MML §2.2 只對照矩陣運算與 shape，可與現有筆記交叉閱讀。
- **實作：** 用小矩陣計算 XW + b，先手算輸出 shape，再以 NumPy 驗證。
- **驗收：** 能區分 * 與 @，預測 batch × feature 的輸出 shape，找出一個 broadcasting 錯誤。

#### Week 4 — Git / Linux / SQL Bridge

- **學習：** 複習 Git、CLI、環境變數；Python DB driver 與 parameterized query。
- **教材範圍：** Git／Linux／SQL 僅補 C# 經驗尚未涵蓋的部分；JOIN、transaction、index 先確認概念。
- **實作：** 沿用現有 repository；用一張合成產品表完成 PostgreSQL CRUD。Git commit 從第一週持續做。
- **驗收：** 可從環境設定啟動程式並安全查詢；能說明 commit／branch 與 transaction。影響後續 DB 整合的環境缺口先補齊，並依緩衝規則順延。

### Math for ML｜Week 5–8｜24h

#### Week 5 — Vector / Matrix / Dot Product

- **學習：** Vector、dot product、norm、cosine similarity；重用已完成的矩陣筆記。
- **教材範圍：** MML §2.1–2.2 已讀內容直接沿用；§3.1–3.4 只讀 norm／inner product／angle 的定義與簡單例子；§2.4 作參考。
- **實作：** 手算兩個向量的內積與 norm，再用 NumPy 驗證相似度。
- **驗收：** 能解釋內積與 cosine 的差別；辨識零向量不能直接做 cosine normalization。

#### Week 6 — Matrix Multiplication / Linear Transformation

- **學習：** Transpose、XW、線性組合與線性轉換。
- **教材範圍：** MML §2.2 複習；§2.7 只讀線性映射與矩陣表示的例子。§2.5–2.6 僅在遇到不懂的 basis／rank 時查閱。
- **實作：** 畫一個二維縮放或旋轉例子；用 NumPy 計算 batch 輸入的 XW。
- **驗收：** 能由輸入／權重 shape 推出輸出，說明權重如何改變表示；不要求一般向量空間證明。

#### Week 7 — Calculus / Gradient

- **學習：** Derivative、partial derivative、chain rule、gradient；exp／log 的基本導數。
- **教材範圍：** MML §5.1–5.2 選簡單多項式與 chain rule；§7.1 選 gradient descent 更新式。§5.3–5.5 延後。
- **實作：** 手算一個二變數 loss 的梯度，用有限差分檢查，再執行一次梯度更新。
- **驗收：** 能解釋更新方向、learning rate 與梯度；計算結果與有限差分在合理容差內接近。

#### Week 8 — Probability / Softmax / Cross Entropy

- **學習：** 離散機率、條件機率、期望；exp／log、Softmax、negative log-likelihood。
- **教材範圍：** MML §6.1–6.4 只選離散機率、條件機率與期望／變異數的例子；Gaussian 推導延後。Softmax／Cross Entropy 使用補充公式與數值例子。
- **實作：** 以三個 logits 寫出穩定的 Softmax（先減最大值）與單一正確類別的 cross entropy。
- **驗收：** 機率和為 1；提高正確類別機率時 loss 降低；能解釋 -log p(target)。

### BankGPT v0.1 / API Engineering｜Week 9–12｜24h

#### Week 9 — BankGPT: LLM Client + Structured Output

- **學習：** Prompt、context window、sampling 概念、輸出 schema、API key／成本預算。
- **教材範圍：** 選定一個模型供應商的官方 quickstart、結構化輸出與 usage 文件；只使用一個模型。
- **實作：** 建立 CLI：輸入合成產品問題，輸出固定 schema；保存 5 題案例與一次實際模型呼叫結果。
- **驗收：** 能處理格式不符與呼叫失敗；設定 timeout／輸出長度上限，記錄 token usage；secrets 不入庫。

#### Week 10 — BankGPT: FastAPI + API Tests

- **學習：** Request／response model、Pydantic validation、錯誤處理、sync 與 async 的使用邊界。
- **教材範圍：** 教材 F：First Steps、Request Body、Response Model、Handling Errors、Testing；async 只查目前 client 的呼叫方式。
- **實作：** 把 Week 9 client 包成一個 endpoint；用 fake client 測成功、無效輸入與 timeout。
- **驗收：** 離線 API 測試可重跑；endpoint 的輸入與輸出符合 schema；同步呼叫不直接阻塞 async endpoint。

#### Week 11 — BankGPT: PostgreSQL Integration

- **學習：** SQLAlchemy 最小 session／transaction、資料存取層、request ID 與結構化 logging。
- **教材範圍：** 沿用 Week 4 DB；只查 SQLAlchemy 官方入門中的連線、session、select 與 transaction。
- **實作：** 以一張合成產品表串接 API；記錄 request ID、latency、模型與 usage，不記錄 secrets。
- **驗收：** DB integration test 可使用測試資料重跑；查詢使用參數，錯誤可由 request ID 追蹤。

#### Week 12 — BankGPT v0.1: Docker + Local Demo

- **學習：** Dockerfile、環境設定、health endpoint、最小 API key authentication。
- **教材範圍：** 教材 F 的 Docker 部署章節；以既有 PostgreSQL 配置為基礎。
- **實作：** 容器化 API，提供 .env.example、啟動／停止命令與 curl／API docs Demo；加入無效 key 的測試。
- **驗收：** 依 README 可啟動 v0.1、查健康狀態並完成 5 題案例；不帶有效 key 的業務請求會被拒絕。

### Buffer A｜Week 13｜6h

#### Week 13 — Buffer A: Foundation + API Integration

- **學習：** 本週不新增必學主題。
- **教材範圍：** 只回查 Week 1–12 未通過的驗收。
- **實作：** 補 Python／數學／DB／Docker 缺口，重跑 BankGPT v0.1；更新實際用時與待辦。
- **驗收：** Week 1–12 的必要驗收完成，或明確記錄延期與重排；不得把未完成工作標成完成。

### ML Fundamentals｜Week 14–17｜24h

#### Week 14 — ML: Dataset Split + Baseline

- **學習：** Train／validation／test、generalization、data leakage、最簡單的預測 baseline。
- **教材範圍：** MML §8.1–8.2 的資料／模型概念與 §8.6 的模型選擇；只選相關段落。
- **實作：** 固定 seed 切分小型數值資料；建立常數或多數類別 baseline；畫資料與預測。
- **驗收：** 能說明 validation 用於調參，test 保留作最後檢查；任何前處理只從 train 擬合。

#### Week 15 — ML: NumPy Linear Regression

- **學習：** MSE、線性模型、gradient descent。
- **教材範圍：** MML §9.1–9.2 只選線性模型與最小平方；Bayesian inference、完整解析解推導延後。
- **實作：** 用 NumPy 寫 loss 與梯度更新，沿用 Week 14 split；不以 sklearn 取代核心演算法。
- **驗收：** loss 在合理設定下降，能解釋每個陣列的 shape，並與 baseline 比較 validation 結果。

#### Week 16 — ML: NumPy Logistic Regression

- **學習：** Sigmoid、binary cross entropy、分類 threshold、precision／recall。
- **教材範圍：** 複習 Week 8；使用 sigmoid 與 binary cross entropy 的公式／數值例子，MML 不作完整 logistic regression 教材。
- **實作：** 實作小型二元分類器；比較兩個 threshold 的混淆矩陣，處理 log 的數值穩定性。
- **驗收：** 能連接 logits → probability → loss，解釋 false positive／false negative。

#### Week 17 — ML: Training Experiment

- **學習：** Batch、epoch、learning rate、overfitting、regularization。
- **教材範圍：** MML §7.1、§8.6 只複習更新與模型選擇；不新增整章閱讀。
- **實作：** 沿用回歸或分類程式，只改 learning rate 或 regularization 一項；保存 train／validation 曲線。
- **驗收：** 能描述完整 training loop、辨認過擬合，選定設定後才檢查 test。

### Neural Network + PyTorch｜Week 18–22｜30h

#### Week 18 — PyTorch: Tensor + DataLoader

- **學習：** Tensor、dtype、device、Dataset／DataLoader、batch shape。
- **教材範圍：** 教材 P：Tensors、Datasets & DataLoaders；沿用 NumPy 的資料與數學。
- **實作：** 把 Week 16 資料轉成 Tensor 與 DataLoader；用 CPU 跑通，標示每一批的 shape。
- **驗收：** 可取出 batch，說明 dtype／device；不依賴 GPU 才能完成。

#### Week 19 — PyTorch: First Complete MLP

- **學習：** nn.Module、Linear、activation、forward、loss、backward、optimizer 的整體角色。
- **教材範圍：** 教材 P：Quickstart、Build the Neural Network；先跟著範例完成全流程，再於後兩週拆解。
- **實作：** 在同一支程式訓練小型 MLP；包含 train()、eval() 與 no_grad() 的驗證流程。
- **驗收：** 能跑完 train／validation，說明主要步驟；本週允許依範例完成，不要求立即獨立重寫。

#### Week 20 — PyTorch: Backpropagation / Autograd

- **學習：** Computational graph、requires_grad、chain rule、梯度累積。
- **教材範圍：** 教材 P：Automatic Differentiation；MML §5.2 與 §5.6 只讀一個小型計算圖的 chain rule。
- **實作：** 手算小型 scalar graph 或線性層 loss 的梯度，與 autograd 比較；觀察未清除梯度的結果。
- **驗收：** 能解釋 backward()、zero_grad() 與梯度累積；比較值在設定容差內相符。

#### Week 21 — PyTorch: Optimizer Experiment

- **學習：** SGD、Adam／AdamW 的用途、learning rate、weight decay。
- **教材範圍：** 教材 P：Optimization；MML §7.1 複習。只理解 AdamW 的功能，不要求推導全部更新式。
- **實作：** 沿用 Week 19 MLP，固定 split／seed／訓練步數，比較 SGD 與 AdamW 或兩個 learning rate。
- **驗收：** 能以曲線解釋收斂差異，記錄條件；不把單次結果當成通用結論。

#### Week 22 — PyTorch: Independent Loop + Checkpoint

- **學習：** 整合 Dataset → forward → loss → backward → update → validation；save／load。
- **教材範圍：** 教材 P：Save and Load；其餘只回查已學內容。
- **實作：** 從空白檔案重建小型 training loop；儲存並載入模型權重，保存設定、seed 與評估結果。
- **驗收：** 可查 API 簽名但能自行組織流程；載入前後 eval 預測在容差內一致，能區分 eval() 與 no_grad()。

### Buffer B｜Week 23｜6h

#### Week 23 — Buffer B: ML / PyTorch Review

- **學習：** 本週不新增必學主題。
- **教材範圍：** 只回查 Week 14–22 未通過的驗收。
- **實作：** 補 training loop／梯度缺口；用少量時間重跑既有 BankGPT smoke test，確認環境仍可用。
- **驗收：** 能獨立寫基本 training loop，並指出目前最容易出錯的 shape／gradient 問題。

### Transformer｜Week 24–28｜30h

#### Week 24 — Transformer: Tokenization + Next Token

- **學習：** Token、vocabulary、token ID、BPE 概念、序列與 next-token labels。
- **教材範圍：** 教材 C 的 Overview／Tokenization 僅取 token 表示與 BPE 概念；自行實作只要求 character tokenizer。
- **實作：** 建立小字元詞表、encode／decode；寫出 x=tokens[:-1] 與 y=tokens[1:] 的例子。
- **驗收：** 可 round-trip 編解碼，說明 label shift；用同一份 tokenizer 作後續 Mini GPT 基礎。

#### Week 25 — Transformer: Token / Position Embedding

- **學習：** Token embedding、position embedding、batch／sequence／hidden dimensions。
- **教材範圍：** 教材 C 的 Architectures 僅取 embedding／position 表示；重用矩陣與索引概念。
- **實作：** 建立 token 與 learned positional embeddings，合成 [B,T,D] 輸入。
- **驗收：** 能解釋位置資訊與 shape；區分 token embedding 與後面用於檢索的句子／文件 embedding。

#### Week 26 — Transformer: Q / K / V + Single-Head Attention

- **學習：** Q=XWq、K=XWk、V=XWv、scaled dot-product attention、causal mask。
- **教材範圍：** 教材 C 的 Architectures 僅取 Q/K/V、scaling 與 causal attention；不讀替代架構／MoE。
- **實作：** 實作單頭 attention；用小輸入檢查矩陣 shape、softmax 軸與 future-token mask。
- **驗收：** 能解釋 softmax(QKᵀ/√dk)V；改變未來位置不應改變先前位置的輸出。

#### Week 27 — Transformer: Multi-Head Attention

- **學習：** Split heads、transpose、concat、output projection。
- **教材範圍：** 沿用 Week 26；只查多頭 reshape／projection 的必要說明。
- **實作：** 將單頭擴展成多頭；為 [B,H,T,Dh] 的轉換加入 shape 檢查。
- **驗收：** 可解釋 head 維度與 D=H×Dh；合併後回到 [B,T,D] 且通過 causal 檢查。

#### Week 28 — Transformer: Decoder Block

- **學習：** Residual、LayerNorm、feed-forward、decoder-only block。
- **教材範圍：** 教材 C 的 Architectures 選 block 元件；本計畫採簡單 LayerNorm／learned position 架構，不要求完整複製 CS336 架構。
- **實作：** 組合已完成元件；先以數值例子理解 residual 與 normalization，再接成 block。
- **驗收：** 能畫出 decoder-only 資料流程，說明每個元件與輸出 shape；保留可重用的 block。

### Hugging Face｜Week 29–30｜12h

#### Week 29 — Hugging Face: Load + Generate

- **學習：** AutoTokenizer、AutoModelForCausalLM、generate、模型與 tokenizer 配對。
- **教材範圍：** 教材 H：Chapter 2 的 Models／Tokenizers，搭配 Text generation 的最小推論例子；chat template 僅在選擇 chat model 時讀。
- **實作：** 選一個能在現有環境推論的小模型，固定模型 revision，完成輸入→token IDs→生成→decode。
- **驗收：** 可解釋輸入／輸出與 generation 設定；記錄環境與模型，不要求接管 BankGPT 的 API 模型。

#### Week 30 — Hugging Face: Dataset + Batch Inputs

- **學習：** 載入本機資料、map、padding／truncation、attention mask。
- **教材範圍：** 教材 H：Chapter 5 的 What if my dataset isn't on the Hub?／Time to slice and dice，Chapter 2 的 Handling multiple sequences；只完成下列操作。
- **實作：** 載入小型 JSON／CSV，做一個 tokenizer map，組出不同長度句子的 batch 並檢查 mask。
- **驗收：** 能解釋 padding mask 與 causal mask 的差別；Trainer／TrainingArguments 移至微調選修。

### Mini GPT from Scratch｜Week 31–34｜24h

#### Week 31 — Mini GPT: Data + Model Assembly

- **學習：** 重用 tokenizer、embedding、attention、decoder block；output head 與 cross entropy。
- **教材範圍：** 教材 C 的 Assignment 1 只對照 data／model／loss 概念；使用本計畫既有元件，不要求完整作業。
- **實作：** 以少量公開或合成文字、固定短 context 組成小型 GPT；先完成一批 forward／loss。
- **驗收：** logits 為 [B,T,V]，labels 與下一 token 對齊，模型參數可計數。

#### Week 32 — Mini GPT: Train + Validate

- **學習：** 重用 PyTorch loop；序列切分、tiny-batch overfit、validation loss。
- **教材範圍：** 沿用 Week 22；不新增 optimizer／tokenizer 的從零實作要求。
- **實作：** 先 overfit 一個小 batch，再於不重疊的 train／validation 文字區段訓練；保存 checkpoint。
- **驗收：** loss 有下降，能排查 label shift／mask 錯誤；記錄 seed、資料版本與模型設定。

#### Week 33 — Mini GPT: Generate + Experiment

- **學習：** Autoregressive generation、context 截斷、temperature 與 greedy sampling。
- **教材範圍：** 只回查生成需要的概念；不新增 beam search 或加速系統。
- **實作：** 從 checkpoint 生成文字；固定 prompt 比較 greedy 與一種 temperature 設定。
- **驗收：** 能逐步解釋下一 token 的取得方式，處理 context 長度；不以生成流暢度作唯一驗收。

#### Week 34 — Mini GPT: Explain + Report

- **學習：** 整合模型理解、可重現性與失敗分析。
- **教材範圍：** 不新增課程章節；最多四週完成 Mini GPT 的主線。
- **實作：** 整理參數量、validation loss、生成例子、啟動指令與一個實驗結論；重跑最小測試。
- **驗收：** 能由文字一路解釋到下一 token 機率；交付可重跑 module／README，不要求大型模型品質。

### Buffer C｜Week 35｜6h

#### Week 35 — Buffer C: Model Integration + BankGPT Restart

- **學習：** 本週不新增必學主題。
- **教材範圍：** 只回查 Week 24–34 缺口與 BankGPT v0.1 啟動紀錄。
- **實作：** 補 Mini GPT 問題，重啟 BankGPT v0.1，確認後續 RAG 的模型 client／DB／測試可用。
- **驗收：** 模型基礎與應用環境通過既有驗收；列出 RAG 的單一文件來源與資料範圍。

### Embedding / RAG / BankGPT v0.2｜Week 36–42｜42h

#### Week 36 — Retrieval: Embedding + Baseline

- **學習：** 句子／文件 embedding、cosine、Top-K；先理解精確搜尋。
- **教材範圍：** 複習 Week 5；選定 embedding 模型官方最小用法。FAISS 僅了解是搜尋 library，主線不另裝第二套索引。
- **實作：** 先用約 10 份短文字手算／NumPy 排序，建立 10 題 question／expected source 與 Recall@K。
- **驗收：** 可重跑檢索 baseline，說明 cosine 與 token embedding 的用途差異；不需要先訓練 embedding 模型。

#### Week 37 — Retrieval: pgvector + Access Filter

- **學習：** 向量儲存、metadata、來源 ID、document-level access filter。
- **教材範圍：** 教材 V 只讀 extension 啟用、vector 欄位、cosine 查詢與 filter；小資料先用精確搜尋，ANN index 延後。
- **實作：** 沿用 PostgreSQL，寫入 Week 36 向量；以伺服器端設定的兩個合成角色測試文件可見範圍。
- **驗收：** 重啟後資料仍在；未授權文件在送入 LLM 前即被排除，不能信任使用者自行傳入的角色。

#### Week 38 — RAG: Document Ingestion + Versioning

- **學習：** 一種真實格式的解析、清理、chunk、source／version／chunk ID、去重與更新。
- **教材範圍：** 選可抽文字 PDF 或 HTML 其中一種，使用對應 parser 官方入門；不含 OCR／複雜表格。
- **實作：** 處理 5–10 份小型公開／合成文件；保留來源位置，建立可重跑 ingestion，更新／刪除一份測試文件。
- **驗收：** 重跑不重複新增；更新後舊 chunks 不再被搜到，刪除後檢索無殘留，來源位置可追溯。

#### Week 39 — RAG: Answer + Citation + Evaluation

- **學習：** Retrieve → context → answer、citation、資料不足時拒答、retrieval／generation 分開評估。
- **教材範圍：** 沿用 BankGPT client；只查 context 建構與目前模型輸出 schema 的必要文件。
- **實作：** 接通第一版 RAG，將 baseline 擴充到 10–20 題，加入無答案／無權限案例及 expected answer。
- **驗收：** 同週檢查 Recall@K、答案是否有來源支持、citation 是否對應實際片段；保留失敗案例與成本／延遲。

#### Week 40 — RAG: Chunking + Retrieval Trace

- **學習：** Chunk size／overlap／Top-K、request／retrieval trace、token usage 與成本計算。
- **教材範圍：** 以現有程式與評估集為主，不新增框架。
- **實作：** 固定其他條件，只比較兩種 chunk size 或 Top-K；記錄來源、片段 ID、模型／prompt 版本。
- **驗收：** 以 baseline 報告差異，能判斷 retrieval 錯或 generation 錯；依當時供應商價格註記日期與成本估算。

#### Week 41 — RAG: One Retrieval Improvement

- **學習：** 理解 keyword／hybrid search 與 reranker 的角色；只選一種改善實作。
- **教材範圍：** 只讀所選方案的官方入門；若選 keyword／hybrid，需處理中文斷詞或明訂測試語料限制。
- **實作：** 根據 Week 40 失敗案例，實作 hybrid search 或 reranker 其中一種，與 baseline 比較。
- **驗收：** 能說明品質與延遲／成本的取捨；沒有改善也可通過，但需提出證據並保留 baseline。

#### Week 42 — BankGPT v0.2: RAG Integration

- **學習：** Citation、更新／刪除、access filter、拒答與 logging 的整合。
- **教材範圍：** 不新增檢索技術；整理 Week 36–41 產出。
- **實作：** 重跑 RAG baseline，補最小 API Demo、架構草圖與一頁 README；逐項檢查來源與權限。
- **驗收：** 交付 v0.2：可啟動、可引用、可拒答、可追蹤錯誤，並有 baseline 報告；達標可開始試投應用職缺。

### Evaluation / BankGPT v0.3｜Week 43–44｜12h

#### Week 43 — Evaluation: Golden Dataset + Held-Out Set

- **學習：** 評分規則、answer correctness、faithfulness／groundedness、資料洩漏。
- **教材範圍：** 複習 Week 14 的 validation／test；定義本專案 rubric，避免把意義重疊的指標重複計分。
- **實作：** 將 baseline 擴充到至少 20 題；從新增題預留至少 5 題未用於調參的 held-out 題目，標記答案／來源／拒答／權限類別。
- **驗收：** 開發集與 held-out 分開；品質由人工逐題核對，LLM judge 若使用需抽查且不作唯一依據。Recall@K 只算有預期且可存取來源的題，無答案／無權限題另檢查拒答與越權。

#### Week 44 — BankGPT v0.3: Regression + Report

- **學習：** 可重複評估、離線 CI 與付費／GPU 評估分離。
- **教材範圍：** 沿用 pytest；CI 只選既有 repository 平台的一個基本 workflow。
- **實作：** 以開發集選定設定後跑 held-out；輸出 Recall@K、correctness、來源支持、拒答、latency／成本；建立離線回歸 workflow。
- **驗收：** CI 不呼叫付費模型；真實模型評估保留手動命令與結果；v0.3 報告可重跑。若依 held-out 改版，須補新保留題。

### Tool Calling / Agent / BankGPT v0.4｜Week 45–47｜18h

#### Week 45 — Tool Calling: Validated Functions

- **學習：** Tool schema、tool call／result、輸入驗證與確定性工具。
- **教材範圍：** 選定模型供應商的 tool calling 官方最小範例；不新增 agent framework。
- **實作：** 建立 calculate_interest() 與 get_product_information() 的合成案例；將結果回傳模型。
- **驗收：** 錯誤參數會被拒絕；計算有獨立測試，模型不自行替代工具算術；工具能力限於展示用途。

#### Week 46 — Tools: Safe Backend Integration

- **學習：** Read-only credential、allowlist、parameterized query、timeout／row limit／audit。
- **教材範圍：** 沿用 Week 11 資料層；SQL 與 internal API 先擇一接到 tool。
- **實作：** 讓模型提供經驗證的產品查詢參數，由程式組固定查詢；測越權／無結果／timeout。
- **驗收：** 工具只能讀取允許的資料；禁止任意模型生成 SQL 直接執行，保留使用者與操作 trace。

#### Week 47 — BankGPT v0.4: Bounded Agent

- **學習：** Agent loop、state、tool selection、retry、停止條件與 human handoff。
- **教材範圍：** 沿用 tool calling，先手寫最小 loop；framework／長期 memory／多 agent 延後。
- **實作：** 讓一個唯讀任務最多執行 3 次工具步驟；限制 timeout／retry／token budget，對超限或不支援操作轉交使用者。
- **驗收：** 測成功、工具失敗、循環超限與越權；要求寫入或有金融影響的操作停止並要求明確確認，Demo 不執行這類操作。

### Buffer D｜Week 48｜6h

#### Week 48 — Buffer D: Evaluation + Agent Integration

- **學習：** 本週不新增必學主題。
- **教材範圍：** 只回查 RAG、evaluation、tools／agent 的未通過項目。
- **實作：** 補 v0.3／v0.4 缺口並重跑回歸測試；整理剩餘部署風險與求職回饋。
- **驗收：** 核心案例通過、失敗限制有文件；只有完成這些後才進入部署，緩衝不用來預排選修。

### Production / Deployment / UI｜Week 49–51｜18h

#### Week 49 — Production: One Cloud Deployment

- **學習：** 一種部署環境、secrets、API／DB 網路邊界、health check。
- **教材範圍：** AWS／Azure／GCP 擇一，使用單一容器服務或小型 VM 的官方入門；先確認支援既有 PostgreSQL／pgvector。
- **實作：** 部署現有 API 與既定 DB，保留 API key／文件權限限制；設定用量預算與停止／清理步驟。
- **驗收：** 可從部署環境完成一次授權請求；資料庫不對外任意開放，health check 可用，能停止資源。

#### Week 50 — Production: Observability + Security Checks

- **學習：** Monitoring、request／tool trace、authentication／authorization、prompt injection 的權限邊界。
- **教材範圍：** 沿用既有 logging／測試；只使用一套簡單 log 或平台 monitoring。
- **實作：** 以正常、逾時、無效身分、惡意文件指令四種案例測部署；確認 secrets 不入 log、檢索與工具權限不能被 prompt 改寫。
- **驗收：** 能由 trace 找出失敗；記錄延遲／用量。僅聲稱已測案例與已實作邊界，不宣稱完全防止 prompt injection。

#### Week 51 — Production: Release + Minimal UI

- **學習：** 部署 workflow、版本標記、rollback、最小 Demo UI。
- **教材範圍：** 延伸 Week 44 CI 與 Week 49 部署命令；UI 選一個已選框架的官方最小範例，預設 Gradio。
- **實作：** 保留人工觸發部署，演練回到前一版；加一頁輸入／回答／citation UI，呼叫既有 API 並在伺服器端保管 key。
- **驗收：** 可部署與 rollback；UI 可完成一個成功與一個拒答案例；不新增產品功能或多頁前端。

### Portfolio / BankGPT v1.0｜Week 52｜6h

#### Week 52 — BankGPT v1.0: Portfolio + Resume

- **學習：** 整理與展示全年既有成果。
- **教材範圍：** 不新增教材／技術；沿用 Week 34、42、44、49–51 的報告、圖與 Demo。
- **實作：** 完成 README、架構圖、評估／benchmark 摘要、Demo 錄影或操作步驟、履歷 bullets。
- **驗收：** 依文件能重現作品；可說明設計、證據、限制與成本。v1.0 不依賴 MCP、Fine-tuning 或 vLLM。


## 教材索引與深度限制

教材是實作的支援。指定章節只取上述操作與例子；若一個小節包含額外任務，超出當週驗收的部分延後。

| 代號 | 主教材 | 必讀／使用範圍 | 參考／延後 |
|---|---|---|---|
| M | [Mathematics for Machine Learning](https://mml-book.github.io/)；本地 book/MATHEMATICS FOR MACHINE LEARNING.pdf | Week 5–8 的定義、例題與更新式；Week 14–22 遇到需要再複習 | 一般向量空間證明、完整矩陣微分、Gaussian 推導、eigendecomposition／SVD 不作前進門檻 |
| P | [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | Week 18：Tensors／Datasets；19：[Quickstart](https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html)／Build Model；20：Autograd；21：Optimization；22：Save／Load | 不擴展到 CV、RL、分散式訓練或編譯最佳化 |
| C | [Stanford CS336 官方課程](https://cs336.stanford.edu/) | 2026 課表中的 Overview／Tokenization 與 Architectures 指定主題；Assignment 1 僅對照 model／loss／training 的需求 | 不要求整門課、完整 Assignment 1、BPE trainer、自己寫 optimizer、Triton／分散式訓練 |
| H | [Hugging Face Chapter 2](https://huggingface.co/learn/llm-course/chapter2/1)、[Chapter 5](https://huggingface.co/learn/llm-course/chapter5/1)、[Text generation](https://huggingface.co/docs/transformers/en/llm_tutorial) | Week 29：Models／Tokenizers／最小生成；30：本機資料載入／map／多序列 padding 與 mask | Trainer／TrainingArguments、完整 NLP tasks、模型發布與 SFT 延後 |
| F | [FastAPI 官方教學](https://fastapi.tiangolo.com/tutorial/) | First Steps、Request Body、Response Model、Handling Errors、Testing；Docker 與驗證按週需求查閱 | OAuth 完整身分系統、大型專案模板、複雜前端延後 |
| V | [pgvector 官方文件](https://github.com/pgvector/pgvector) | 啟用、vector 欄位、cosine 查詢、filter、更新／刪除 | ANN index 調校、Qdrant／Milvus 比較、同時維護多個 DB 延後 |

Hugging Face 官方將每章設計為約 6–8 小時，所以本計畫的兩週只完成指定小節與實驗。[課程時間說明](https://huggingface.co/learn/llm-course/chapter1/1)

CS336 官方列有 Python、PyTorch、ML 與數學先備要求，且實作負荷高；本計畫使用其選定內容作參考。Mini GPT 的驗收以本檔為準。[課程先備要求與作業](https://cs336.stanford.edu/)

### 技術選擇上限

- 一個模型供應商／一個 API 模型，單一 Python 環境與版本紀錄。
- PostgreSQL + pgvector；不平行學第二套向量資料庫。
- 一種文件 parser；先處理小型可抽文字文件，不含 OCR。
- Hybrid search／reranker 先實作一種；有證據再擴充。
- 一種雲端部署環境、一頁最小 UI，主線預設 Gradio。
- BankGPT 與 Mini GPT 是不同實驗目的；不要求把自己訓練的 Mini GPT 接成 BankGPT 回答模型。

## 里程碑與求職

| 時點 | 必要成果 |
|---|---|
| Week 12 | BankGPT v0.1：LLM client、FastAPI、PostgreSQL、tests、Docker、本機 Demo |
| Week 19 | 跟著範例跑通第一個完整 MLP |
| Week 22 | 能獨立組織 PyTorch training／validation loop，保存與載入模型 |
| Week 28 | 能解釋並組裝 decoder-only Transformer block |
| Week 34 | 四週 Mini GPT 與實驗報告 |
| Week 42 | BankGPT v0.2：RAG、citation、權限、10–20 題 baseline；達標可開始試投 |
| Week 44 | BankGPT v0.3：至少 20 題評估集、held-out、回歸 workflow、評估報告 |
| Week 47 | BankGPT v0.4：安全唯讀工具與有停止條件的 agent |
| Week 52 | BankGPT v1.0：部署、最小 UI、可重現文件、Demo 與履歷材料 |

求職依作品與目標職缺要求判斷，不以週數保證準備完成。Week 42 已有 baseline 的 v0.2 可試投 AI Application／GenAI 職缺；Week 44 用 v0.3 報告補強。若同等成果提前完成，可以提前投遞；進度延後則按驗收調整。

## 進階選修：主線完成後另排

以下是新增時間的規劃估計，不計入 312h，不預先占用四週緩衝。依求職方向一次只選一項；環境／資料整理超出估計時另記。

| 選修 | 先備條件 | 建議另排時間 | 完成範圍 |
|---|---|---:|---|
| MCP | 完成 Week 45–47 tools／agent | 1–2 週／6–12h | 用一個既有唯讀 tool 完成 client／server 實驗，理解 resource／prompt 與 consent 邊界 |
| SFT / PEFT / LoRA 或 QLoRA | PyTorch、HF、可重現的 base evaluation | 3–4 週／18–24h | 確認模型／資料授權、PII、GPU／VRAM／預算；準備小型任務資料並切 train／validation／test，比較 base／tuned 的品質與成本 |
| vLLM / Quantization | 模型推論、Docker、Linux／雲端環境 | 2–3 週／12–18h | 確認 OS／GPU／VRAM／模型格式，理解 KV cache／batching；固定 prompt 與 output length 比較兩種 serving 設定 |
| Kubernetes | 已完成容器部署與 rollback | 1–2 週／6–12h | Deployment／Service／ConfigMap／Secret 概念與小型部署；不擴成平台維運專案 |
| Retrieval / Agent framework | 已有可測的手寫 baseline | 1–2 週／6–12h | 將一個現有流程移入一個框架，以相同案例比較可讀性、trace、品質與限制 |

Fine-tuning 用於行為／格式／任務適應；需更新、引用與權限控管的文件知識先用 RAG。是否採用選修成果，依相同評估資料決定，不要求一律合入 BankGPT。

## 每週完成定義

一般週至少留下：

- 一個可執行實驗或既有功能的具體增量。
- 一個有意義的自動測試、數值檢查或可重複手動檢查。
- 簡短筆記：能解釋的概念、結果、限制、下週第一件事。
- 一次 Git commit；有 API／資料／模型改動時記錄版本與執行條件。

緩衝週交付缺口處理與重跑紀錄即可，不強迫新增實驗。閱讀完成不等於能力完成，尚未通過驗收保持進行中。

每週紀錄使用 [PROGRESS.md](PROGRESS.md) 的模板；已完成的 Python 練習與 MML 筆記繼續沿用。
