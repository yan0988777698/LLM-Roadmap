# Week 04 — Docker Compose 指令與 Shell 環境

筆記日期：2026-09-19。對應 [第四週練習](../../exercises/week04_git_linux_sql_bridge/README.md)。

這次使用 Docker 啟動 PostgreSQL，並進入同一個容器練習 Linux 命令列。兩個指令分別負責：

```text
docker compose up -d --wait  → 啟動服務，在背景執行，等待就緒
docker compose exec db sh    → 在 db 容器內開啟互動式 shell
```

## 1. `docker compose up -d --wait`

在 Windows 的 PowerShell、第四週練習目錄執行：

```powershell
docker compose up -d --wait
```

| 部分 | 意思 |
| --- | --- |
| `docker compose` | 依照 `compose.yaml` 管理專案的服務 |
| `up` | 建立並啟動需要的容器 |
| `-d` | detached mode：讓容器在背景執行，終端機可以繼續輸入指令 |
| `--wait` | 等服務進入執行中或通過健康檢查，才結束等待 |

本週的 [compose.yaml](../../exercises/week04_git_linux_sql_bridge/compose.yaml) 設有 PostgreSQL 健康檢查，因此這裡會等待資料庫通過檢查。這一步啟動資料庫服務；產品表另外由 `db_bridge.py init` 建立。[Docker Compose up 官方文件](https://docs.docker.com/reference/cli/docker/compose/up/)

## 2. `docker compose exec db sh`

服務啟動後，在同一個 PowerShell 執行：

```powershell
docker compose exec db sh
```

| 部分 | 意思 |
| --- | --- |
| `exec` | 在已執行的容器內啟動一個程式 |
| `db` | 要操作的 Compose 服務名稱 |
| `sh` | 要啟動的 shell 程式，用來接收並執行命令 |

`db` 來自設定檔的服務名稱：

```yaml
services:
  db:
    image: postgres:17-alpine
```

`db` 是 Compose 服務名稱，這個服務內的 PostgreSQL 資料庫名稱則是 `week04_bridge`。`sh` 開啟的是 Linux 命令列，可以執行 `pwd`、`ls`、`export` 等命令。[Docker Compose exec 官方文件](https://docs.docker.com/reference/cli/docker/compose/exec/)

## 3. 先看提示字元，確認自己在哪裡

| 本次練習的提示字元範例 | 所在環境 | 設定環境變數的語法 |
| --- | --- | --- |
| `PS C:\...>` | Windows PowerShell | `$env:WEEK4_MODE = 'practice'` |
| `/ #` | 容器內的 Linux shell | `export WEEK4_MODE=practice` |

提示字元只用來辨認環境，不要一起貼進指令。容器內切換資料夾後，提示字元中的路徑也可能改變。

本次遇到的錯誤是在 Linux shell 中輸入 PowerShell 語法：

```text
/ # $env:WEEK4_DB_PASSWORD = 'week04_local_only'
/bin/sh: :WEEK4_DB_PASSWORD: not found
```

原因是 `sh` 不認得 PowerShell 的 `$env:變數名稱 = 值` 寫法。這個錯誤發生在命令解讀階段，並不是 PostgreSQL 判定密碼錯誤。

若要替 Windows 上的 Python 程式設定連線密碼，先在容器 shell 輸入 `exit`，回到 PowerShell 後再設定 `$env:WEEK4_DB_PASSWORD`。在容器內使用 `export` 設定變數，不會回頭改變 Windows PowerShell 的環境。

## 4. 完整操作順序

先開啟 Docker Desktop。從 repository 根目錄 `LLM-Engineer-Roadmap` 的 PowerShell 執行：

```powershell
cd exercises/week04_git_linux_sql_bridge
$env:WEEK4_DB_PASSWORD = 'week04_local_only'
docker compose up -d --wait
docker compose exec db sh
```

密碼是本機合成資料練習使用的示範值。終端機已在第四週目錄時，不必再執行上面的 `cd`。

看到容器的提示字元後，接著執行 Linux 指令：

```sh
pwd                         # 顯示目前目錄
ls                          # 列出目前目錄內容
cd /tmp                     # 切換到 /tmp
pwd                         # 應顯示 /tmp
cat /etc/os-release         # 查看容器的 Linux 版本資訊
export WEEK4_MODE=practice   # 設定目前 shell 的環境變數
printenv WEEK4_MODE          # 應顯示 practice
exit                        # 離開 shell，回到 PowerShell
```

`export` 的設定供這個 shell 與之後啟動的子程序使用；離開後，再開一個新的 shell，不會自動保留這次設定。

回到 PowerShell 後，確認 Windows 上的 Python 可以連線：

```powershell
.\.venv\Scripts\python.exe db_bridge.py check
```

成功時會顯示資料庫 `week04_bridge`、使用者 `week04` 與 PostgreSQL 版本。

## 5. 離開 shell 與停止資料庫是不同操作

| 操作 | 執行位置 | 影響 |
| --- | --- | --- |
| `exit` | 容器的互動式 shell | 關閉這次 `sh`，回到 PowerShell；PostgreSQL 繼續運作 |
| `docker compose ps` | 第四週目錄的 PowerShell | 查看本週容器的狀態 |
| `docker compose stop` | 第四週目錄的 PowerShell | 停止本週服務，保留資料 |

`exec db sh` 開啟的 shell 是容器內額外啟動的程式。離開它不等於停止整個容器。若開了新的 PowerShell 視窗，執行本週 Compose 指令前，仍要重新設定 `WEEK4_DB_PASSWORD`。

## 6. 常用指令速查

以下 Compose 指令在 `exercises/week04_git_linux_sql_bridge` 目錄的 PowerShell 執行。先啟動 Docker Desktop，並設定本週的示範密碼：

```powershell
$env:WEEK4_DB_PASSWORD = 'week04_local_only'
```

| 需求 | 指令 | 說明 |
| --- | --- | --- |
| 確認 Docker 引擎連線 | `docker version` | 正常時有 Client 與 Server 資訊；Server 連線錯誤時檢查 Docker Desktop |
| 查看 Compose 版本 | `docker compose version` | 確認 Compose 工具可用 |
| 啟動並等待就緒 | `docker compose up -d --wait` | 第一次建立容器；設定有變更時會視需要重建 |
| 查看本專案容器 | `docker compose ps -a` | 包含停止的容器，查看狀態與 port |
| 停止 PostgreSQL | `docker compose stop db` | 正常停止，保留容器與本週資料 |
| 啟動已停止的容器 | `docker compose start db` | 沿用既有容器設定 |
| 重新啟動 | `docker compose restart db` | 重啟既有容器，不套用 YAML 設定變更 |
| 查看最近 50 行日誌 | `docker compose logs --tail 50 db` | 啟動或連線出問題時先看這裡 |
| 持續追蹤日誌 | `docker compose logs -f --tail 50 db` | 按 Ctrl+C 結束追蹤，資料庫仍繼續執行 |
| 進入 Linux shell | `docker compose exec db sh` | 輸入 `exit` 返回 PowerShell |
| 查看實際對外 port | `docker compose port db 5432` | 查詢容器內 `5432` 對應到主機的哪個位址與 port |
| 檢查 Compose 設定 | `docker compose config --quiet` | 驗證設定，不輸出完整內容；成功時通常沒有輸出 |
| 查看用法 | `docker compose --help` | 也可用 `docker compose up --help` 查看單一指令 |

`db` 是服務名稱。`stop`、`start`、`restart`、`logs` 等指令省略服務名稱時，會作用於本 Compose 專案的所有服務。[Compose 指令總覽](https://docs.docker.com/reference/cli/docker/compose/)、[日誌選項](https://docs.docker.com/reference/cli/docker/compose/logs/)

## 7. `up`、`start`、`restart`、`pause`、`down` 怎麼選

| 情境 | 指令 | 容器與資料的變化 |
| --- | --- | --- |
| 今天練習結束 | `docker compose stop db` | 停止容器，保留資料 |
| 下次繼續，設定沒變 | `docker compose start db` | 啟動原本的容器 |
| 修改 YAML 的 port 或環境設定 | `docker compose up -d --wait` | 偵測變更並視需要重建容器，保留掛載的 volume |
| 設定沒變，只想重啟服務 | `docker compose restart db` | 使用原本的容器設定重啟 |
| 短暫凍結程序 | `docker compose pause db` | 凍結執行中的程序；暫停期間不能正常處理查詢 |
| 解除凍結 | `docker compose unpause db` | 恢復程序執行 |
| 移除本專案容器與網路 | `docker compose down` | 本週 named volume 預設保留；下次用 `up` 重建 |

平常說「暫停學習、先關資料庫」用 `stop` 就好。`pause` 是凍結程序，不是正常關閉資料庫。

**改 port 後，`stop` 再 `start` 或直接 `restart` 都不會套用新設定；要執行 `up -d --wait`。** 不必先執行 `down`。[Compose 啟動說明](https://docs.docker.com/compose/support-and-feedback/faq/)、[restart 的設定限制](https://docs.docker.com/reference/cli/docker/compose/restart/)

`docker compose down -v` 會連本專案宣告的 named volume 一起刪除，包含本週資料庫資料；只有刻意清空重做時才使用。這份筆記中的資料保留說明以本週已有 `week04_data` volume 為前提。[down 與 volumes 選項](https://docs.docker.com/reference/cli/docker/compose/down/)

## 8. Port 對應與修改後的驗證

本專案目前 YAML 的預設值是：

```yaml
ports:
  - "127.0.0.1:${WEEK4_DB_PORT:-5432}:5432"
```

格式是「主機 IP：主機 port：容器 port」。沒有設定 `WEEK4_DB_PORT` 時，這個例子代表：

```text
Windows 的 Python → 127.0.0.1:5432 → 容器內 PostgreSQL:5432
```

如果主機的 `5432` 無法使用，可在同一個 PowerShell 設定其他可用 port，例如 `15432`：

```powershell
$env:WEEK4_DB_PORT = '15432'
$env:WEEK4_DB_PASSWORD = 'week04_local_only'
docker compose up -d --wait
docker compose port db 5432
.\.venv\Scripts\python.exe db_bridge.py check
```

此時映射應為 `127.0.0.1:15432`，容器內仍是 `5432`。Compose 和本專案 Python 都會讀取 `WEEK4_DB_PORT`，因此要在同一個 PowerShell 執行。

如果想直接修改預設值，要同步修改 `compose.yaml` 的 `${WEEK4_DB_PORT:-5432}`，以及 `db_bridge.py` 的 `os.environ.get("WEEK4_DB_PORT", "5432")`。已設定的環境變數會優先於預設值；想改回使用預設值，可以先移除目前視窗的設定：

```powershell
Remove-Item Env:WEEK4_DB_PORT -ErrorAction SilentlyContinue
```

Compose 可以讀 `.env` 做變數替換，但本專案 Python 的 `os.environ` 不會自動載入 `.env`。只改 YAML 或只新增 `.env`，不代表 Python 的連線設定也跟著改變。[Compose 變數替換文件](https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/)

本次排錯時，Windows 的 `55354–55453` 是保留範圍，因此 `55432` 和 `55433` 都無法使用；這是當時的檢查結果，保留範圍可能改變。再次遇到 bind／port 錯誤時，可在 PowerShell 查詢：

```powershell
# 檢查指定 port 是否已有 TCP 連線或監聽
Get-NetTCPConnection -LocalPort 55432 -ErrorAction SilentlyContinue

# 查看 Windows 的 TCP 保留範圍
netsh interface ipv4 show excludedportrange protocol=tcp
```

## 9. 直接進入 PostgreSQL 查資料

在 PowerShell 執行以下指令，直接開啟容器內的 PostgreSQL 用戶端 `psql`：

```powershell
docker compose exec db psql -U week04 -d week04_bridge
```

`-U` 指定資料庫帳號，`-d` 指定資料庫名稱；此處的 `-d` 與 `docker compose up -d` 的意義不同。

進入 `psql` 後，才輸入以下命令：

```sql
\conninfo
\dt
SELECT id, name, price_twd, stock FROM week04_products ORDER BY id;
\q
```

`\conninfo` 顯示連線資訊，`\dt` 列出資料表，`\q` 離開 `psql`。SQL 敘述以分號結束，這些反斜線命令不需要分號。若尚未建立產品表，先回 PowerShell 執行 `.\.venv\Scripts\python.exe db_bridge.py init`。[psql 指令參考](https://www.postgresql.org/docs/17/app-psql.html)

也可以從 PowerShell 執行一次查詢後直接返回：

```powershell
docker compose exec db psql -U week04 -d week04_bridge -c "SELECT current_database(), current_user;"
```

這個查詢在容器內執行，沒有經過 Windows 的主機 port。因此它成功只代表容器內資料庫可用；Windows 上的 Python 連線仍需用 `db_bridge.py check` 驗證。

資料庫 `week04_bridge` 由 PostgreSQL 映像在第一次啟動、資料目錄為空時，依 `POSTGRES_DB` 建立；`db_bridge.py init` 才建立產品表與示範資料。沿用已有資料的 volume 時，不會重新初始化；只修改 YAML 的 `POSTGRES_PASSWORD` 也不會變更既有帳號密碼。[PostgreSQL 官方映像說明](https://hub.docker.com/_/postgres)

## 10. Docker 與 Compose 指令的差別

`docker compose` 依本專案的 YAML 與服務名稱操作；一般 `docker` 指令可以查看目前 Docker 引擎的資源，或用容器名稱操作。

| 用途 | Compose 寫法 | 一般 Docker 寫法 |
| --- | --- | --- |
| 查看容器 | `docker compose ps -a`（本專案） | `docker ps -a`（目前引擎的全部容器） |
| 查看日誌 | `docker compose logs --tail 50 db` | `docker logs --tail 50 roadmap-week04-db-1` |
| 進入 shell | `docker compose exec db sh` | `docker exec -it roadmap-week04-db-1 sh` |
| 停止容器 | `docker compose stop db` | `docker stop roadmap-week04-db-1` |

一般 `docker exec` 的 `-i` 保留標準輸入，`-t` 配置終端機，常合寫成 `-it`；`docker compose exec` 預設已提供互動式終端機。容器名稱若有變更，以 `docker ps -a` 的輸出為準。[Docker 容器指令](https://docs.docker.com/reference/cli/docker/container/)、[Compose exec](https://docs.docker.com/reference/cli/docker/compose/exec/)

其他常用的唯讀查詢：

```powershell
docker image ls     # 列出本機映像，例如 postgres:17-alpine
docker volume ls    # 列出資料卷
docker stats --no-stream  # 查看容器當下的 CPU、記憶體等用量
docker system df    # 查看 Docker 資源的磁碟用量
```

映像是建立容器的範本；容器是執行環境；volume 用來保存需要跨容器重建保留的資料。[Docker CLI 參考](https://docs.docker.com/reference/cli/docker/)
