# Roadmap

課程調整日期：2026-09-05。本檔是主題式能力地圖；週次與時數以 [52_WEEK_PLAN.md](52_WEEK_PLAN.md) 為準。

## 範圍與學習深度

- **主線實作：** 能執行、修改、解釋並用測試或實驗驗證。
- **概念理解：** 能說明用途、限制與何時需要，不要求從零重做完整演算法或平台。
- **進階選修：** 主線完成後另排，不是 BankGPT v1.0 或第一年完成的必要條件。

年度預算為 48 週主線／288h 加 4 週緩衝／24h，共 312h。Week 13、23、35、48 用於補課與整合。教材只讀當週必要片段，已讀筆記與程式持續重用。

## 1. 工程基礎｜Week 1–4

主線實作：

- Python collections、functions、class／dataclass、typing、exception、iterator／generator。
- venv／pip、module／package、pytest。
- NumPy ndarray、shape、broadcasting、矩陣乘法。
- Python 與 PostgreSQL 的 parameterized query、基本 CRUD。
- Git commit 從第一週開始；既有 Git／Linux／SQL 經驗以診斷與補缺為主。

概念理解：branch／merge、process／environment、JOIN、transaction、index。

驗收：能閱讀與修改小型 Python package，重跑測試，用 NumPy 解釋 XW 的 shape，安全存取合成資料。

## 2. Math for ML｜Week 5–8，後續按需複習

主線實作：

- Vector、matrix、dot product、norm、cosine similarity。
- Transpose、matrix multiplication、linear transformation。
- Derivative、partial derivative、chain rule、gradient、一次 gradient descent 更新。
- 離散機率、條件機率、exp／log、Softmax 與 cross entropy 的數值例子。
- 期望／變異數的基本意義。

MML 的精確必讀範圍在週計畫與進度表。§2.1–2.2 已完成內容沿用；§2.4–2.6 依例題需要參考。§5.3–5.5、一般向量空間證明、Gaussian 推導、eigenvalue／eigenvector、SVD 均可延後，遇到模型或選修需要時再補。

驗收：能用手算與 NumPy／有限差分互相驗證。數學與程式可交叉學習，不以讀完整章為前進條件。

## 3. 第一個 LLM Application｜Week 9–12

先備：Python package／tests、基本 SQL；不要求先完成模型訓練。

主線實作：

- 一個模型 client、prompt、context／output length 上限與 structured output。
- Timeout／錯誤處理、API key／環境設定、usage／成本紀錄。
- FastAPI endpoint、Pydantic request／response validation、fake client API tests。
- 一張合成產品表的 SQLAlchemy／PostgreSQL integration。
- Request ID／logging、最小 authentication、Docker、health check、README／本機 Demo。

概念理解：temperature／top-p、sync／async 的使用邊界；不要求複雜併發或完整身分平台。

成果：BankGPT v0.1。後面做 ML／Transformer 時保留此 API，緩衝週重跑 smoke test。

## 4. ML Fundamentals｜Week 14–17

主線實作：

- Train／validation／test split、baseline、避免 data leakage。
- NumPy linear regression／logistic regression 的 loss 與 gradient update。
- Batch／epoch、learning rate、overfitting／regularization。
- 分類 threshold、confusion matrix、precision／recall。
- 固定 split／seed、一次只改一項條件的實驗與曲線。

驗收：能解釋完整 training loop；validation 用於選設定，test 保留作最後檢查。

## 5. Neural Network + PyTorch｜Week 18–22

先備：NumPy shape、loss、gradient 與基本 training loop。

主線實作：

- Tensor、dtype／device、Dataset／DataLoader。
- nn.Module、Linear／activation、forward／loss／backward／optimizer。
- Week 19 先依範例跑通完整 MLP，之後用同一程式拆解與修改。
- 手算 gradient 與 autograd 比較，理解 zero_grad()。
- SGD／AdamW 實驗，理解 learning rate／weight decay 的用途。
- train()／eval()、no_grad()、model save／load、設定／seed 紀錄。

驗收：Week 22 可查 API 名稱但能獨立組織 training／validation loop，載入權重後重現 eval 結果。

## 6. Transformer｜Week 24–28

主線實作：

- Character tokenizer、encode／decode、next-token label shift。
- Token／learned positional embedding。
- Q／K／V、scaled dot-product attention、causal mask。
- Multi-head reshape／concat／projection。
- Residual、LayerNorm、feed-forward 與 decoder-only block。

概念理解：BPE 的目的與基本過程。完整 BPE trainer、RoPE／RMSNorm 等架構變體、MoE 延後。

驗收：能畫出文字到 logits／下一 token 機率的流程，檢查 [B,T,D]／[B,H,T,Dh] shape 與不能偷看未來 token 的性質。

## 7. Hugging Face｜Week 29–30

主線實作：

- AutoTokenizer、AutoModelForCausalLM、generate、decode。
- 固定模型 revision，記錄環境與生成設定；chat model 才補 chat template。
- 載入本機 JSON／CSV、Dataset.map、padding／truncation、attention mask。

驗收：能載入小型 pretrained model 完成 inference，解釋 batch mask 與 causal mask 的差異。

Trainer／TrainingArguments 與完整 fine-tuning 流程移至選修；不要求兩週讀完整門 HF Course。

## 8. Mini GPT from Scratch｜Week 31–34

先備：PyTorch loop 與可重用的 Transformer 元件。

主線實作：

- 重用 Week 24–28 的 tokenizer／embedding／attention／block。
- 加上 output head、cross entropy、訓練與 validation。
- 檢查 label shift，先 overfit tiny batch，再用不重疊資料切分訓練。
- Checkpoint、autoregressive generation、temperature／greedy 比較。
- Parameter count、validation loss、生成例子、README 與實驗報告。

範圍：少量文字、短 context、小模型，維持四週。不要求重做所有元件、完整 CS336 Assignment 1 或大型模型品質。Mini GPT 與 BankGPT 的回答模型分開。

## 9. Embedding / Document Pipeline / RAG｜Week 36–42

先備：BankGPT v0.1 可重跑、NumPy／cosine 與模型使用基礎。

主線實作：

- 句子／文件 embedding、先用 NumPy 做精確 Top-K。
- PostgreSQL + pgvector；先做精確搜尋、persistence、metadata／access filter。
- 一種文件格式的 parsing、清理、chunking、來源位置、版本／去重／更新／刪除。
- Retrieve → context → answer、citation、資料不足時拒答。
- Week 36 建立檢索 baseline；Week 39 第一個完整 RAG 同週建立答案／citation／拒答檢查。
- 比較 chunk size 或 Top-K；hybrid search／reranker 只選一種改善實作。
- Request／retrieval trace、模型／prompt／文件版本、latency／token usage／成本。
- 伺服器驗證身分與角色，在內容進入 LLM 前排除未授權文件。

概念理解：token embedding 與 retrieval embedding 的差別；FAISS 是 similarity-search library，pgvector 是 PostgreSQL extension。Qdrant／Milvus、ANN 調校、OCR／複雜表格、第二種檢索改善列為延伸。

驗收：可回答也可拒答；文件更新／刪除不留下舊片段；能找出 retrieval 或 generation 的錯誤。完成 BankGPT v0.2 與 10–20 題 baseline。

## 10. Evaluation｜Week 43–44，從 baseline 持續累積

主線實作：

- 擴充到至少 20 題，含 expected answer／source、無答案、權限與 adversarial cases。
- 從新增題保留至少 5 題未參與調參的 held-out；其餘作開發／調參使用，已用於調參的 baseline 不改標為未見題。
- Recall@K、answer correctness、來源支持／faithfulness、拒答、latency／成本；Recall@K 只算有預期且可存取來源的題，無答案／無權限題另檢查拒答與越權。
- 定義 rubric；faithfulness／groundedness 若在此專案同義，避免重複計分。
- 人工核對，LLM judge 僅作輔助；離線 regression CI 與付費／GPU 評測分離。
- 記錄 model／prompt／資料／設定版本與失敗分類；以相同案例比較每次能力改動。

驗收：BankGPT v0.3 有可重跑的評估報告。held-out 題目若被用來改版，就不再視為未見測試，需補新保留題。小型題庫用於學習與回歸，不聲稱代表所有實際使用情境。

## 11. Tool Calling / Agent｜Week 45–47

主線實作：

- Tool schema、validated input、backend execution、tool result 回傳。
- calculate_interest() 與 get_product_information() 的合成案例。
- SQL／internal API 先選一種整合；read-only、allowlist、parameterized query、timeout／row limit／audit。
- 一個有 state 與停止條件的 agent loop，最多 3 次工具步驟，限制 retry／token budget。
- 測成功、工具失敗、無結果、循環超限、越權與 human handoff。

Demo 限唯讀操作；對要求寫入或有金融影響的操作停止並要求明確確認，不在此 Demo 執行。任意模型產生 SQL 直接執行不屬於主線能力。

成果：BankGPT v0.4。LangGraph 等框架、planning 的進階策略、長期 memory、多 agent、MCP 移至選修。

## 12. Production / Portfolio｜Week 49–52

先備：可重跑的 RAG／tool regression、Docker 與既有 secrets／auth／logging。

主線實作：

- AWS／Azure／GCP 擇一、單一容器服務或 VM，確認 PostgreSQL／pgvector 可用。
- Secrets、DB 網路邊界、health check、用量／停止資源流程。
- 基本 monitoring、request／tool trace、安全案例與權限回歸。
- 人工觸發的部署 workflow、版本標記與 rollback 演練。
- 一頁最小 UI（預設 Gradio），只呼叫既有 API。
- Week 52 整理既有架構圖、報告、Demo／README、履歷 bullets。

v1.0 的定位是可重現的 Portfolio / Production Demo，驗收以已測能力與限制為準。API 模型即可完成；vLLM／Kubernetes 不構成必要依賴。

## 13. 進階選修｜主線完成後另排

| 方向 | 內容 | 先備／完成條件 |
|---|---|---|
| MCP | Client／server、tool／resource／prompt、consent | 已懂 tool calling；以一個既有唯讀 tool 完成實驗 |
| Fine-tuning | Pretraining vs SFT、PEFT、LoRA／QLoRA、dataset preparation | 已有 PyTorch／HF 與 base evaluation；確認授權、PII、GPU／VRAM／預算，切 train／validation／test，做 base vs tuned 比較 |
| Model serving | vLLM、compatible API、Linux、FP16／BF16／INT8／INT4、quantization、KV cache／batching | 先查當時 OS／硬體與模型格式支援；固定 prompt／output length 比較 latency／throughput／VRAM |
| Deployment | Kubernetes Deployment／Service／ConfigMap／Secret | 已完成一次部署與 rollback，再學平台物件 |
| Application framework | 第二種 retrieval 改善、LangGraph 等單一框架 | 有原始 baseline，以相同案例比較新增複雜度與收益 |
| Research / Systems | 深入 probability／optimization、CUDA／Triton、distributed training、資料管線、論文重現 | 依目標職位另訂計畫，不納入第一年 312h |

Fine-tuning 優先用於穩定任務的行為／格式適應；文件知識的更新、引用與存取控制先用 RAG。選修不必全部做，也不必全部合入 BankGPT。

## 求職定位與檢查點

主要作品定位：以 Backend／DB 工程經驗串接 LLM、RAG、評估與部署的 AI Application／GenAI Engineer。

- Week 42：v0.2 + baseline + Demo／README 達標，可開始試投。
- Week 44：v0.3 補上正式評估與 held-out 結果。
- Week 47：v0.4 展示安全工具與 agent。
- Week 52：v1.0 完成部署、UI 與 Portfolio。

PyTorch、Transformer 與 Mini GPT 提供模型理解證據；更偏模型訓練／推論的職位需依要求補選修深度。求職依實際能力與作品，不以週數保證達標。

台灣職缺的歷史定性觀察與限制請看 [TAIWAN_JOB_ALIGNMENT.md](TAIWAN_JOB_ALIGNMENT.md)。
