# Week 04 — Git / Linux / SQL Bridge

本週把既有 C#／SQL 經驗接到 Python：從命令列與環境變數取得設定，用 PostgreSQL 的一張合成產品表完成 CRUD，理解參數化查詢與 transaction。範圍依 [52 週計畫](../../52_WEEK_PLAN.md)，學習結果記在 [PROGRESS.md](../../PROGRESS.md)。

2026-09-19 完成紀錄：已建立本目錄 `.venv`（Python 3.13.12／Psycopg 3.3.6）與本機 PostgreSQL 17.11；四個 CRUD TODO 已作答並通過檢查。實際投入 4 小時，成果提交為 `59759e0`，詳細過程見 [PROGRESS.md](../../PROGRESS.md)。

## 今天先做：30–45 分鐘

在 repository 根目錄 `LLM-Engineer-Roadmap` 開啟 PowerShell，依序執行：

```powershell
git status --short
git branch --show-current
git log -3 --oneline
cd exercises/week04_git_linux_sql_bridge
python cli_env.py --min-price 100
$env:WEEK4_MODE = 'practice'
python cli_env.py --min-price 200
```

這段只需 Python，尚不需要安裝 driver 或啟動資料庫。開啟 [cli_env.py](cli_env.py)，逐行對照：

1. 預測第一次的 `WEEK4_MODE` 和價格；未設定時，mode 使用預設的 `development`。
2. 第二次會顯示 `practice`、`200`：前者來自環境變數，後者來自命令列參數。
3. 執行 `python cli_env.py --help`，再試 `--min-price -1`，觀察參數檢查。
4. 比較輸出的工作目錄與程式目錄。在上一層執行同一個檔案時，工作目錄會改變，程式位置不變。
5. 記下一句解釋：「命令列參數是本次執行帶入的值；環境變數是程式從啟動它的環境讀取的設定。」

PowerShell 的 `$env:WEEK4_MODE` 設定保留在目前視窗，之後啟動的子程序會繼承；重新開啟的終端機不會自動取得這次設定。練習完可執行 `Remove-Item Env:WEEK4_MODE`。

## 檔案與本週安排

| 檔案 | 用途 |
| --- | --- |
| [cli_env.py](cli_env.py) | 先練習 CLI、工作目錄、環境變數 |
| [compose.yaml](compose.yaml) | 啟動本機 PostgreSQL；沿用它即可 |
| [requirements.txt](requirements.txt) | Python PostgreSQL driver：Psycopg 3 |
| [schema.sql](schema.sql) | 一張 `week04_products` 合成產品表 |
| [db_bridge.py](db_bridge.py) | 可跟做的連線、CRUD、rollback 示範 |
| [practice.py](practice.py) | 四個 SQL TODO 與可重跑的資料庫檢查 |
| [test_config.py](test_config.py) | 不需啟動資料庫的 port／設定／命令列回歸檢查 |
| [Docker Compose 與 Shell 筆記](../../notes/week04/docker_compose_shell.md) | 啟動／進入容器的指令拆解、環境辨認與本次錯誤原因 |

| 項目 | 預估 | 成果 |
| --- | ---: | --- |
| Git／CLI／環境變數與概念對照 | 1.5h | 能解釋程式如何取得設定、commit／branch 的用途 |
| PostgreSQL 示範與獨立 CRUD | 3.5h | driver 連線、四個 TODO、參數查詢與 rollback |
| 整理、驗收與 commit | 1h | 用時、結果、疑問與一個明確的 Git commit |

合計每週 6h，與其他週並行時共用時數。這是預估，不是已投入用時。JOIN、index 本週只確認概念；Docker 先作為啟動 PostgreSQL 的工具，容器原理依原計畫後續再學。

## 建立 Python 與 PostgreSQL 環境

以下指令都在本練習目錄執行。若 `.venv` 已建立且可 `import psycopg`，可直接跳到設定環境變數。

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

使用虛擬環境內 Python 的完整相對路徑，不必先執行 Activate。`psycopg[binary]` 包含預編譯的 driver 與所需 client library。[Psycopg 安裝說明](https://www.psycopg.org/psycopg3/docs/basic/install.html)

開啟已安裝的 Docker Desktop，等引擎就緒。在同一個 PowerShell 視窗設定：

```powershell
$env:WEEK4_DB_PASSWORD = 'week04_local_only'
docker compose up -d --wait
.\.venv\Scripts\python.exe db_bridge.py check
.\.venv\Scripts\python.exe db_bridge.py init
.\.venv\Scripts\python.exe db_bridge.py list --min-price 100
```

這是本機合成資料課程的示範密碼。程式只連 `127.0.0.1`、資料庫 `week04_bridge`、帳號 `week04`，預設連接埠 `5432`。Compose 將同一個環境變數交給容器初始化資料庫；Python 透過 `os.environ` 讀取它。設定方式參考 [Compose 環境變數文件](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/)。

第一次初始化有三筆產品：Notebook（80 元）、Keyboard（1200 元）、O'Reilly SQL Guide（650 元）。`list --min-price 100` 應依價格順序列出後兩筆。重跑 `init` 保留既有資料，不覆蓋同名產品的修改。

```powershell
docker compose ps
docker compose stop
```

`stop` 只停止本週服務並保留資料；下次用相同密碼重新 `up -d --wait`。每次開新終端機要重新設定環境變數。資料存在本週的 named volume 中；修改密碼環境變數不會替既有資料庫改密碼。[PostgreSQL 官方映像說明](https://hub.docker.com/_/postgres)

## 讀懂一個查詢

```python
min_price = 100
rows = conn.execute(
    "SELECT name, price_twd FROM week04_products WHERE price_twd >= %s",
    (min_price,),
).fetchall()
```

| 片段 | 意義 | C# 經驗對照 |
| --- | --- | --- |
| `psycopg.connect(...)` | 建立 PostgreSQL 連線 | `NpgsqlConnection` |
| `conn.execute(sql, parameters)` | SQL 與資料分開傳入 | command 的參數集合 |
| `%s` | Psycopg 的資料值佔位符，文字與整數都可用 | SQL parameter |
| `(min_price,)` | 只有一個元素的 tuple；逗號不可省略 | 一個參數的集合 |
| `.fetchone()`／`.fetchall()` | 取一列／全部結果列 | reader 讀取資料 |

不要替 `%s` 加引號，也不要用 f-string、`+` 或 Python `%` 運算把輸入拼進 SQL。參數化讓 `O'Reilly` 的引號仍是資料，也讓 `"' OR '1'='1"` 只成為要搜尋的完整名稱。此處參數只能代表資料值，不能拿來替換表名。[Psycopg 參數文件](https://www.psycopg.org/psycopg3/docs/basic/params.html)

## 跟做 CRUD 與 transaction

先閱讀 `db_bridge.py` 的 `create_product`、`find_product`、`update_stock`、`delete_product`，預測每一步會留下什麼資料，再執行：

```powershell
.\.venv\Scripts\python.exe db_bridge.py crud
.\.venv\Scripts\python.exe db_bridge.py rollback
```

`crud` 新增一筆名稱帶有引號的臨時示範產品，查詢、改庫存、刪除剛新增的那筆，並檢查其他文字不會變成 SQL 條件。

`rollback` 在同一個 transaction 中先新增產品，再故意把庫存設成 `-1`。資料庫的 `CHECK (stock >= 0)` 會拒絕更新；程式確認前面的新增也一起撤銷，而且連線仍可查詢。

```python
with conn.transaction():
    # 這裡的 SQL 是同一組交易。
    # 正常離開時 commit；例外傳出此區塊時 rollback。
    ...
```

本示範連線設為 `autocommit=True`，讓區塊外的單一 SQL 自動提交；需要一組操作一起成功或失敗時，明確使用 `conn.transaction()`。捕捉資料庫錯誤放在 transaction 區塊外。[Psycopg 交易管理](https://www.psycopg.org/psycopg3/docs/basic/transactions.html)、[PostgreSQL transaction 教學](https://www.postgresql.org/docs/current/tutorial-transactions.html)

## 獨立完成四個 TODO

開啟 [practice.py](practice.py)，依序把四個函式裡的 `query = None` 與 `parameters = None` 改成自己的答案，保留下方檢查：

1. INSERT 三個欄位並 `RETURNING id`。
2. 依名稱精確 SELECT 四個欄位，找不到時回傳 `None`。
3. 依 id UPDATE stock，回傳影響的筆數。
4. 依 id DELETE，回傳影響的筆數。

```powershell
.\.venv\Scripts\python.exe practice.py
```

目前檔案已有完整作答；最初的骨架會顯示 `TODO 1` 並以非零狀態結束。檢查會涵蓋引號、查無資料、負庫存、重複刪除，以及更新／刪除不能改到其他產品。練習使用連線專用的 temporary table，結束時回復，不修改示範表的產品。

`practice.py` 只執行整份驗收，不接受 `create_product 杯子 50 3` 等位置參數；多打參數會顯示用法並結束，不會新增商品。可用 `--help` 查看用途。

設定與命令列的回歸檢查不需要 Docker，使用標準函式庫 `unittest`：

```powershell
.\.venv\Scripts\python.exe -m unittest test_config -v
```

不要用匯入示範函式取代自己填 SQL。若有參考範例，把該部分記為跟做，再不看範例重寫一次確認理解。

## CLI／Linux 最小對照

| 工作 | PowerShell | Linux shell |
| --- | --- | --- |
| 查看所在目錄 | `Get-Location` | `pwd` |
| 列出檔案 | `Get-ChildItem` | `ls` |
| 切換目錄 | `Set-Location 路徑`／`cd 路徑` | `cd 路徑` |
| 讀文字檔 | `Get-Content 檔名` | `cat 檔名` |
| 設定環境變數 | `$env:WEEK4_MODE = 'practice'` | `export WEEK4_MODE=practice` |

資料庫啟動後，可以進同一個 Linux 容器試這些命令：

```powershell
docker compose exec db sh
```

接下來才是 Linux shell 指令：

```sh
pwd
ls
export WEEK4_MODE=practice
printenv WEEK4_MODE
exit
```

容器 shell 的設定只作用在那個 shell 與之後的子程序，不會回頭改變 Windows 的環境變數。

## Git 與 SQL 概念驗收

Git commit 是暫存區內容的一次版本快照；branch 是指向某條開發線最新 commit 的可移動名稱。建立 branch 本身不會保存未提交內容。資料庫 transaction 的 commit 則是提交資料變更，與 Git commit 是不同系統的操作。

在 repository 根目錄進行這週的 Git 練習：

```powershell
git status --short
git switch -c week04-git-sql
git diff
```

若該 branch 已存在，用 `git switch week04-git-sql`。完成練習與學習紀錄後，明確加入本週檔案，檢查暫存內容，再提交：

```powershell
git add exercises/week04_git_linux_sql_bridge notes/week04 PROGRESS.md
git diff --cached
git commit -m "Complete week 4 Git and PostgreSQL practice"
```

`git diff` 不會顯示尚未追蹤的新檔內容；加入暫存後用 `git diff --cached` 查看。`.venv` 已被 repository 的 `.gitignore` 排除。[Git 官方教學](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)

JOIN 的用途是依關聯條件合併資料，例如產品與分類；本週維持一張產品表，只需能說明 INNER JOIN 與 LEFT JOIN 的差別。Index 可以協助查詢，但需要空間與維護成本；表很小時不保證使用 index 更快。本週也不新增索引調校任務。[PostgreSQL JOIN](https://www.postgresql.org/docs/current/tutorial-join.html)、[Index 概念](https://www.postgresql.org/docs/current/indexes-intro.html)

## 常見問題

- Docker 顯示找不到 pipe／daemon：先確認 Docker Desktop 的 Linux engine 已啟動，再 `docker compose up -d --wait`。
- `Set WEEK4_DB_PASSWORD`：在執行 Python 的同一個終端機設定密碼；Compose 與 Python 都需要它。
- 主機 port 被占用或 Windows 拒絕綁定：目前預設為 `5432`；可確認 `15432` 可用後，在同一個 PowerShell 設定 `$env:WEEK4_DB_PORT = '15432'`，再 `docker compose up -d --wait`，Python 也會使用相同 port。修改 YAML 預設值時，Python 預設值也要同步；`stop`／`start` 不會套用新映射。
- 本次 Windows 曾保留 `55354–55453`，所以 `55432`、`55433` 都不能用；不要只將 port 加 1。查詢保留範圍與連線占用的方法見 [Docker 筆記](../../notes/week04/docker_compose_shell.md)。
- 帳密錯誤：使用建立這個 volume 時的密碼，環境變數改值不會自動更新資料庫帳密。
- `Run db_bridge.py init first`：先建立本週資料表。
- 找不到 `psycopg`：用本目錄 `.venv` 裡的 Python 安裝 requirements，執行時也用同一個 Python。

## 完成標準與學習筆記

- [x] 能用 CLI 參數與環境變數啟動程式，說明兩者差別。
- [x] 能解釋工作目錄、相對路徑與基本 Linux shell 指令。
- [x] PostgreSQL 連線成功，完成四個參數化 CRUD TODO。
- [x] 含引號的產品名稱可以正確儲存與查詢。
- [x] 故意失敗的 transaction 會撤銷同組新增，並可繼續查詢。
- [x] 能說明 Git commit／branch、DB transaction，以及 JOIN／index 的用途。
- [x] 完成一個本週 commit，並記下實際用時、跟做／獨立完成範圍。

實際日期與用時：2026-09-19，合計 4 小時。完成狀態依學習者回報及 PROGRESS 紀錄同步；程式檢查由助手重跑確認。環境與 INSERT 寫法曾由助手協助，四題作答與跟做範圍見進度紀錄；目前未回報未理解項目。版本為 Python 3.13.12／Psycopg 3.3.6／PostgreSQL 17.11。
