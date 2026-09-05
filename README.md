# LLM Engineer Roadmap

課程調整日期：2026-09-05。

## 專案目標

從既有 C#／軟體工程經驗出發，以每週 6 小時建立 AI / LLM Application Engineering 能力，同時保留模型訓練與 Transformer 的底層理解。

第一年必要成果：

- Python／NumPy／SQL／API 工程基礎。
- ML、PyTorch training loop、Transformer 與四週 Mini GPT。
- BankGPT 的 RAG、Evaluation、Tool Calling 與有停止條件的 Agent。
- Testing、Logging、權限邊界、Docker、一次雲端部署與最小 Demo UI。
- 能用程式、評估結果與實驗紀錄解釋設計選擇的 Portfolio。

MCP、Fine-tuning（SFT／PEFT／LoRA／QLoRA）、vLLM、Quantization 與 Kubernetes 保留為進階選修，完成主線後另排。它們不構成第一年完成或 BankGPT v1.0 的條件。

## 如何使用

1. 依 [52_WEEK_PLAN.md](52_WEEK_PLAN.md) 的週次、教材範圍與驗收執行；這是唯一排程依據。
2. 以 [ROADMAP.md](ROADMAP.md) 查先備能力與主線／選修的界線。
3. 在 [PROGRESS.md](PROGRESS.md) 記錄實際時間、成果、未通過項目與延期；讀完教材不直接等於完成。
4. 依 [projects/BankGPT.md](projects/BankGPT.md) 逐版完成專案。

已完成的 Week 1、進行中的 Week 2／Week 5 與 MML 筆記保留。可先完成 Week 2，再把 NumPy 與矩陣筆記交叉練習；不需要等數學整章讀完。

## 學習主線

1. Week 1–4：Python／NumPy／Git／Linux／SQL。
2. Week 5–8：直接支援實作的 Math for ML，以指定例題為主。
3. Week 9–12：BankGPT v0.1，先完成 LLM client、FastAPI、PostgreSQL、Docker 與測試。
4. Week 14–22：ML／PyTorch；Week 19 跟做完整 MLP，Week 22 獨立組織 training loop。
5. Week 24–28：Tokenization／Embedding／Attention／Transformer。
6. Week 29–30：Hugging Face 模型載入、生成與資料處理指定小節。
7. Week 31–34：重用前面元件，完成 Mini GPT。
8. Week 36–42：Embedding／pgvector／文件管線／RAG／baseline evaluation。
9. Week 43–44：Golden Dataset、held-out、正式評估與回歸 workflow。
10. Week 45–47：Tool Calling、安全後端工具與 bounded agent。
11. Week 49–52：部署、監控／安全驗證、rollback、最小 UI 與 Portfolio。

Week 13、23、35、48 為整合／補課週，安排在主要階段之間。

## 時間規劃

- 每週 6 小時，全年 52 週，共 **312 小時**。
- **48 週主線／288 小時 + 4 週緩衝／24 小時**，閱讀、環境設定與除錯都計入。
- 一般週以 1.5h 概念、3.5h Coding／Experiment、1h 整理／解釋為起點；可按主題調整，總時數維持 6h。
- 每週只要求一個主要實驗及必要檢查，持續重用已有程式。
- 超時先記錄缺口並使用緩衝；需要時順延依賴的主題。緩衝耗盡就調整日曆，不以趕完章節取代驗收。
- 選修時數另計，不預占緩衝。

## BankGPT 版本與里程碑

BankGPT 從 Week 9 開始；模型基礎階段保留既有 API 與測試，後續再接 RAG。Mini GPT 是獨立的學習實驗，不要求成為 BankGPT 的回答模型。

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

v1.0 主線使用選定的 API 模型，沿用 PostgreSQL + pgvector。微調與自架模型的實驗可在主線之後另做，不再設為必經的 v0.5。

## 求職與職缺參考

Week 42 的 v0.2 若已具備可重現 Demo、RAG baseline、引用與錯誤分析，可開始試投 AI Application／GenAI 類職缺；Week 44 再以 v0.3 的正式評估報告補強。能力與作品若提前達標，可提前投遞；週數本身不保證準備完成。

第一年優先展示既有 Backend／DB 經驗如何連接 LLM、RAG、測試與部署。更偏模型訓練或推論效能的職缺，再另排微調、serving 與 GPU 相關實驗。

[TAIWAN_JOB_ALIGNMENT.md](TAIWAN_JOB_ALIGNMENT.md) 保留 2026-08 的定性職缺觀察與資料限制；其中求職里程碑已同步此版課程。歷史觀察不等同當下職缺統計，也不代表年資／學歷／上線實績已符合要求。

## 教材使用原則

- MML 依週計畫選定義、例題與更新式；進階證明與矩陣分解按需補。
- PyTorch 使用官方 Learn the Basics，先跑通流程，再拆解與重建。
- CS336 使用明確選定的主題，Mini GPT 不要求完整 Assignment 1。
- Hugging Face 兩週只完成指定小節，Trainer／SFT 移至選修。
- RAG／Agent／部署以官方文件支援 BankGPT，先限制為一個模型、DB、parser 與部署環境。

教材連結與每週閱讀邊界集中於 [52_WEEK_PLAN.md](52_WEEK_PLAN.md)，避免跨文件維護不同清單。

## 專案結構

```text
LLM-Engineer-Roadmap/
├─ README.md
├─ ROADMAP.md
├─ 52_WEEK_PLAN.md
├─ TAIWAN_JOB_ALIGNMENT.md
├─ PROGRESS.md
├─ book/
├─ notes/
├─ exercises/
└─ projects/
   └─ BankGPT.md
```
