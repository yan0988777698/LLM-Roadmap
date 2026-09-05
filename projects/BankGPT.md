# BankGPT

課程調整日期：2026-09-05。版本週次以 [52_WEEK_PLAN.md](../52_WEEK_PLAN.md) 為準。

## 專案目的與範圍

建立能展示 Backend Engineering、RAG、Evaluation、Tool Calling／Agent 與部署能力的 Portfolio。Week 9 開始小型應用，後續逐版加入能力。

主線限制：

- 一個 API 模型供應商；模型 client 與後端測試以 fake client 隔離。
- PostgreSQL + pgvector、一種文件 parser、5–10 份小型公開／合成文件起步。
- Hybrid search／reranker 先實作一種；根據 baseline 決定是否保留。
- 一種雲端部署方式、一頁最小 UI（預設 Gradio）。
- Mini GPT 為獨立學習實驗，不要求作為 BankGPT 的回答模型。
- MCP／微調／vLLM 不構成 v1.0 的必要依賴；原先必經的 v0.5 微調改為主線後的獨立選修實驗。

## 資料與安全前提

- 只使用公開、授權或自行產生的合成資料，不使用真實客戶、帳戶或交易資料。
- Secrets、API key 與連線字串放環境變數或 secret store，不放 repository／log／瀏覽器端。
- 文件保留 source／version／chunk ID 與來源位置；請求與工具保留身分、權限結果與 audit trace。
- 角色與權限由伺服器依驗證身分判定，不接受使用者或模型自行聲稱的權限。
- Demo 預設且僅提供唯讀工具。要求改變資料或有金融影響的操作停止並要求明確確認；這類操作不在 Demo 中執行。
- API key 驗證是本 Demo 的最小 authentication；真實企業身分整合依需求另做。

## Architecture

```text
User
  ↓
Minimal UI / API client
  ↓
BankGPT API (FastAPI: authentication + validation)
  ├─ LLM client → one API model
  ├─ RAG
  │   ├─ Document parsing / cleaning / chunking / versioning
  │   ├─ Embedding
  │   ├─ PostgreSQL + pgvector + access filter
  │   └─ Context / citation / one retrieval improvement
  ├─ Tool layer
  │   ├─ Deterministic calculator
  │   ├─ Read-only SQL or internal API
  │   └─ Validation / limits / audit
  ├─ Evaluation
  │   ├─ Development set + held-out set
  │   ├─ Retrieval / answer / refusal checks
  │   └─ Latency / token usage / cost
  └─ Production
      ├─ Docker / one deployment environment
      ├─ Logging / monitoring / secrets
      └─ CI / manually triggered release / rollback
```

## Version Plan

### v0.1 — Week 9–12

目標：可測試與啟動的基本 LLM Application。每週只加入一層，Week 13 保留整合時間。

- [ ] Week 9：CLI client、prompt、structured output、5 題案例；至少一次真實模型呼叫。
- [ ] Week 9：timeout、輸出長度／成本預算、usage、secrets 設定。
- [ ] Week 10：FastAPI、Pydantic request／response validation、fake client API tests。
- [ ] Week 10：輸入不合法、格式不符、模型 timeout 等錯誤處理。
- [ ] Week 11：SQLAlchemy／PostgreSQL 合成產品資料整合、parameterized query。
- [ ] Week 11：request ID、latency、model／usage logging。
- [ ] Week 12：Dockerfile、.env.example、health endpoint、API key 驗證。
- [ ] Week 12：README 啟動／停止步驟、curl／API docs 本機 Demo。

驗收：依文件可啟動並跑完案例；離線 API 測試與 DB 測試可重跑；無效 key 的業務請求被拒絕。

模型基礎階段保留 v0.1，Week 23／35 以既有 smoke test 檢查環境；不在這段加入新應用需求。

### v0.2 — Week 36–42

目標：可引用、可拒答、可追蹤來源與更新的文件問答。

- [ ] Week 36：NumPy Top-K、10 題 question／expected source、Recall@K baseline。
- [ ] Week 37：pgvector persistence、metadata、伺服器驗證的兩個合成角色與 access filter。
- [ ] Week 38：一種文件格式的解析、清理、chunking、來源位置。
- [ ] Week 38：source／version／chunk ID、去重、可重跑 ingestion。
- [ ] Week 38：文件更新／刪除後舊 chunks 不再出現在檢索結果。
- [ ] Week 39：第一個完整 RAG、citation、資料不足／無權限時拒答。
- [ ] Week 39：10–20 題 baseline，包含 expected answer／source 與拒答案例；同週核對 retrieval、答案來源支持與 citation。
- [ ] Week 40：一項 chunk size 或 Top-K 比較，request／retrieval trace、latency／usage／成本。
- [ ] Week 41：hybrid search 或 reranker 一種改善的比較；無改善時保留 baseline 並解釋。
- [ ] Week 42：RAG 整合驗收、最小 API Demo、架構草圖與一頁 README。

驗收：能由 trace 判斷 retrieval 或 generation 出錯；權限過濾在內容進入 LLM 前生效。達標後可開始試投應用職缺，作品內容以已完成能力為準。

### v0.3 — Week 43–44

目標：在既有 baseline 上建立可重跑的正式評估。

- [ ] 至少 20 題 Golden Dataset；50 題為後續擴充目標，不是本階段門檻。
- [ ] 每題標記 expected answer／source、拒答或權限要求，包含 edge／adversarial case。
- [ ] 從新增題預留至少 5 題 held-out，不參與調參；其餘為開發集，已調參的 baseline 不改標為未見題。
- [ ] Recall@K、answer correctness、來源支持（faithfulness／groundedness 的專案定義）、拒答表現；Recall@K 只算有預期且可存取來源的題，無答案／無權限另驗收。
- [ ] Latency、token usage、依註明日期的供應商價格計算成本。
- [ ] 人工核對答案；LLM judge 若使用需抽查，不作唯一依據。
- [ ] 模型／prompt／文件／實驗設定版本、failure analysis 與評估報告。
- [ ] 離線 regression CI；付費或 GPU 評測以手動命令／workflow 執行。

驗收：同一設定可重跑，報告區分開發集與 held-out；若根據 held-out 改設定，補新的保留題。這份小題庫用於學習與回歸，不能推論所有真實問題的成功率。

Week 42 已開始試投者，於此時補上 v0.3 報告；不把投遞進度綁定選修。

### v0.4 — Week 45–47

目標：以可控、可測的唯讀工具完成一個任務。

- [ ] Week 45：tool schema／result、calculate_interest()、get_product_information()。
- [ ] Week 45：輸入驗證、確定性計算測試；將工具結果回傳模型。
- [ ] Week 46：SQL 或 internal API 先擇一串接，使用唯讀 credential。
- [ ] Week 46：table／operation allowlist、parameterized query、timeout／row limit／audit。
- [ ] Week 46：查詢由程式依驗證參數組合，不直接執行任意模型生成 SQL。
- [ ] Week 47：agent state／tool selection、最多 3 次工具步驟、retry／token budget。
- [ ] Week 47：成功、工具失敗、無結果、循環超限與越權案例。
- [ ] Week 47：human handoff；對要求寫入或有金融影響的操作停止並要求明確確認，Demo 不執行。
- [ ] 在既有評估資料之外加入 tool／agent 必要回歸案例。

驗收：能解釋權限、停止條件與失敗處理。Week 48 用於補評估／agent 整合，不預排 MCP。

### v1.0 — Week 49–52

目標：完成可重現的 Portfolio / Production Demo，整合前面已做的能力。

- [ ] Week 49：AWS／Azure／GCP 擇一完成一次部署，確認 PostgreSQL／pgvector 可用。
- [ ] Week 49：secrets、DB 網路邊界、health check、用量預算與停止／清理資源步驟。
- [ ] Week 50：logging／monitoring；用 trace 追蹤正常、timeout、無效身分與惡意文件指令案例。
- [ ] Week 50：authentication／authorization 回歸；驗證 prompt 不能改寫工具或文件權限。
- [ ] Week 51：沿用 CI，人工觸發的部署流程、版本標記與一次 rollback 演練。
- [ ] Week 51：一頁最小 Demo UI，顯示答案／citation，支援成功與拒答案例。
- [ ] Week 52：整合既有 Architecture Diagram、Benchmark／Evaluation Report 與 README。
- [ ] Week 52：Demo 錄影或操作步驟、Resume bullets、已知限制與成本說明。

驗收：依 README 能重現，作品敘述與實際完成能力一致；不宣稱全面防止 prompt injection。v1.0 使用既有 API 模型即可完成。

## 進階選修

完成主線後依需求另排，時數估計見 [52_WEEK_PLAN.md](../52_WEEK_PLAN.md)。不預占緩衝，選修成果不必一律合入主專案。

| 實驗 | 範圍與驗收 |
|---|---|
| MCP | 用一個既有唯讀 tool 串 client／server，理解 tool／resource／prompt、consent 與資料邊界 |
| SFT / LoRA 或 QLoRA | 針對行為／格式／任務適應；先確認模型／資料授權、PII、GPU／VRAM／預算，準備 train／validation／test，以相同測試比較 base／tuned 品質與成本 |
| vLLM / Quantization | 先查當時 OS／硬體／模型格式支援；Linux 或合適雲端環境上固定 prompt／output length，比較兩種設定的 latency／throughput／VRAM，理解 KV cache／batching |
| Kubernetes / Framework | 已有部署或手寫 baseline 後，再比較新增工具的管理成本與實際收益 |

需要更新、引用或存取控制的文件知識，優先由 RAG 處理。選修的 GPU 或模型實驗費用另記，不計作免費資源。

## Portfolio 驗收

主線面試應能回答：

1. 一段文字如何成為 token、logits 與下一 token 機率？Mini GPT 的 mask／labels 如何驗證？
2. 為什麼 BankGPT 選 RAG？什麼需求才考慮 Fine-tuning？
3. Chunk size／Top-K／檢索改善的決定，有什麼實驗證據？
4. 如何區分 retrieval 與 generation 錯誤，處理無答案或無權限問題？
5. 文件更新／刪除如何避免舊內容被引用？
6. 評估集怎麼建立、如何保留 held-out、如何避免把調參結果當測試結果？
7. Tool calling 如何驗證參數、限制查詢、停止循環並保留 audit？
8. Secrets、使用者身分與文件權限如何傳遞？惡意文件指令的測試涵蓋哪些情境？
9. 系統如何 logging、monitoring、部署與 rollback？延遲與成本是多少？
10. 哪些功能仍未實作、哪些成果只是小規模實驗？

完成選修後再增加 LoRA 更新了哪些參數、base／tuned 比較、vLLM／量化效果等問題；不將未做的實驗寫成已具備的專案能力。
