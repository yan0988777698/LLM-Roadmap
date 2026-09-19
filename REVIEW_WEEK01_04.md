# Week 1–4 資料與程式檢查

檢查日期：2026-09-19。學習者已回報完成 Week 4；保留各週完成狀態與實際用時。

## 結論

Week 1–4 的主要練習與資料庫流程可以重跑。已修正環境重建、輸入驗證、NumPy 計算方式與文件一致性的問題，可以接續 Week 5；不需要重排前四週。

本次涵蓋前四週的 README、Python 程式、相依套件設定、SQL／Compose、Docker 筆記、進度與 Git 紀錄，以及已使用的 MML §2.1–2.2 筆記、練習、內積／叉積補充與四張圖。檢查既有數學範例與圖文是否一致，未逐頁審閱整本 MML 教科書。後續課程文件僅核對先備與銜接；職缺文件保留原本有日期的歷史觀察，本次未重新抽樣市場。

## 發現與調整

| 範圍 | 原問題 | 已完成的調整 |
| --- | --- | --- |
| Week 2 帳戶 | 可用負數、NaN 或 Infinity 建立初始餘額；Infinity 存款會污染餘額 | 增加 `__post_init__` 初始值驗證，存提款共用有限正金額驗證，並補上失敗時餘額不變的測試 |
| Week 2 generator 測試 | 原測試確認 iterator 與結果，未驗證何時讀取來源 | 新測試追蹤輸入被消耗的時機，確認建立 generator 時尚未讀取，`next()` 只讀到下一筆合格資料 |
| Week 3 環境 | README 要求安裝的 `requirements.txt` 不存在 | 加入 `numpy==2.5.3`，與本次已安裝、已驗證版本一致 |
| Week 3 矩陣練習 | `Y` 是固定的手算陣列，沒有執行題目要求的矩陣算式 | 保留手算答案為 `expected`，使用 `Y = X @ W + b`，再核對結果；偏移應失敗的案例加入未拋錯時的檢查 |
| Week 4 port | 連線驗證錯把 `5432` 當最大合法 port，拒絕 `15432` | 合法範圍改回 `1–65535`；預設連線仍是 `5432`，不更改現有容器映射 |
| Week 4 CLI | `practice.py create_product ...` 默默忽略參數，容易誤以為有新增商品 | 加入 argparse，支援 `--help` 並拒絕額外位置參數；保留整份 CRUD 驗收用途 |
| Week 4 README | TODO／勾選狀態過時，建議的 `55433` 也曾位於 Windows 保留區間 | 同步完成狀態、4 小時與 `59759e0`，改為檢查可用 port 後用環境變數切換，記錄 `up` 套用流程 |
| 進度與導覽 | 主 README 仍要求先完成 Week 2；Week 4 commit 仍待填 | 同步 Week 1–4 已完成、Week 5 下一步；補入實際 Week 4 commit，移除互相矛盾的狀態文字 |
| 數學說明 | 切片結果缺少就近的原始矩陣；Attention 註解將內積大小等同方向相似度 | 補上 `(2, 3)` 的示範輸入；註明內積同時受方向與長度影響，shape 範例尚未計算完整注意力權重 |

這些程式維護由助手完成，沒有將其算成新增的學習者獨立作答或投入時間。保留原本的 SQL 答案與手算結果。

## 驗證結果

| 檢查 | 結果 |
| --- | --- |
| Week 1 collections、Two Sum 三個既有案例 | 通過 |
| Week 2 pytest | 22 個通過；新增案例先重現 8 個失敗，再完成修正 |
| Week 3 basics／multiply／broadcast、五題練習 | 全部通過 |
| NumPy 相依設定 | pip 離線 dry-run 確認現有環境符合 `requirements.txt`；未另建全新環境下載套件 |
| Week 4 設定／CLI unittest | 4 組通過，涵蓋合法高 port、非法 port、缺少密碼、錯誤位置參數 |
| Week 4 CLI 環境練習 | 預設／自訂值、負價格拒絕與不輸出密碼通過 |
| PostgreSQL 連線 | `week04_bridge`／`week04`，PostgreSQL 17.11 |
| PostgreSQL 隔離驗證 | 暫存表內的初始化、重跑保留修改、價格查詢、CRUD、rollback 及作答檢查通過；正式產品表前後資料列相同 |
| MML §2.1、§2.2 Python 範例 | 通過 |
| 內積／叉積補充 | 文件內數值檢查通過，四張圖的主要標示與範例相符 |
| Python 語法與文件 | 16 個練習／測試 Python 檔案語法通過；本機 Markdown 連結與格式檢查通過 |

主要測試可以在各週練習目錄重跑：

```powershell
# Week 2
.\.venv\Scripts\python.exe -m pytest -q

# Week 3
.\.venv\Scripts\python.exe matrix_bridge.py all
.\.venv\Scripts\python.exe practice.py

# Week 4：設定測試不需啟動 Docker
.\.venv\Scripts\python.exe -m unittest test_config -v

# Week 4：資料庫已啟動且 port 設定一致時
$env:WEEK4_DB_PASSWORD = 'week04_local_only'
.\.venv\Scripts\python.exe db_bridge.py check
.\.venv\Scripts\python.exe practice.py
```

## 接下來的調整

- 接續 Week 5 的 §3.1–3.4：norm、inner product、angle 與 cosine；重用現有矩陣筆記即可。叉積證明屬補充內容，不需要反覆精讀才往下走。
- 用一組新輸入再手算 `X @ W + b`，重新填 `expected`，確認能自己解釋算式與 shape；這可作為下一次開始前的短複習，不新增一整週任務。
- 前四週已記錄 2 + 4 + 4 + 4 = 14 小時；Week 5 已有另列的 8 小時閱讀／練習紀錄。並行活動若有重疊時段，記錄實際時間時不要重複加總。
- 本次修正尚未提交 Git。既有 `59759e0` 是 Week 4 成果，不包含這次檢查的變更。

Week 2 帳戶仍是教學模型：輸入依約使用 `Decimal`，未做任意型別轉換，欄位可直接賦值；目前測試涵蓋建構與存提款方法，不宣稱完整帳務規則。自動檢查證明程式行為，概念理解依學習者的完成回報與筆記維護。

實作查核參考：[NumPy indexing](https://numpy.org/doc/stable/user/basics.indexing.html)、[Decimal.is_finite](https://docs.python.org/3/library/decimal.html#decimal.Decimal.is_finite)、[Python argparse](https://docs.python.org/3/library/argparse.html)、[Psycopg transaction](https://www.psycopg.org/psycopg3/docs/basic/transactions.html)。
