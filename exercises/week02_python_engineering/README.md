# Week 02 — Python Engineering Basics

## 學習目標

- 使用 `venv` 與 `pip` 建立隔離環境。
- 理解 module、package 與 `src` layout。
- 練習 class、dataclass、typing 與自訂 exception。
- 使用 generator 處理逐筆資料。
- 使用 pytest 撰寫可重複執行的測試。

這週練習把 Python 程式整理成有專案結構、能管理套件、可以自動測試的程式。以下用 C#／.NET 概念對照，搭配本專案的銀行帳戶範例說明。

## 概念與 C# 對照

| 名稱 | 用途 | C#／.NET 概念對照 |
| --- | --- | --- |
| `venv` | 建立專案專用的 Python 環境 | 專案各自管理相依套件的需求；沒有完全相同的對應 |
| `pip` | 安裝、移除 Python 套件 | NuGet 的套件安裝功能 |
| module（模組） | 組織一份可匯入的程式碼 | 可先類比一個 `.cs` 檔，但不完全相同 |
| package（套件） | 組織多個 module | 類似用 namespace 組織功能，但與檔案結構有關 |
| `src` layout | 把套件原始碼集中放在 `src/` | 專案目錄配置慣例 |
| class | 把資料與行為包在一起 | `class` |
| dataclass | 自動產生資料類別常見的方法 | 部分用途類似 `record`，語意不完全相同 |
| typing | 標示預期的資料型別 | 型別宣告，但 Python 預設不強制檢查 |
| exception | 表達與處理錯誤 | `Exception`、`throw`、`try/catch` |
| generator | 需要時才逐筆產生資料 | 使用 `yield return` 的 iterator |
| pytest | 自動執行測試 | xUnit／NUnit／MSTest |

## 專案結構

```text
week02_python_engineering/
├─ pyproject.toml
├─ src/
│  └─ banking/
│     ├─ __init__.py
│     ├─ account.py
│     ├─ exceptions.py
│     └─ generators.py
└─ tests/
   ├─ test_account.py
   └─ test_generators.py
```

各檔案的用途：

| 檔案 | 用途 |
| --- | --- |
| [pyproject.toml](pyproject.toml) | 專案資訊、套件建置設定、開發相依套件與 pytest 設定 |
| [src/banking/__init__.py](src/banking/__init__.py) | 套件初始化與對外提供的匯入名稱 |
| [src/banking/account.py](src/banking/account.py) | 帳戶資料、存款與提款行為 |
| [src/banking/exceptions.py](src/banking/exceptions.py) | 金額不合法、餘額不足的自訂例外 |
| [src/banking/generators.py](src/banking/generators.py) | 逐筆篩選金額的 generator |
| [tests/test_account.py](tests/test_account.py) | 帳戶行為的測試 |
| [tests/test_generators.py](tests/test_generators.py) | generator 的測試 |

## 建立環境

### venv：每個專案使用自己的環境

假設專案 A 和專案 B 需要不同版本的同一個套件，各自建立虛擬環境，就可以分別安裝。`venv` 負責建立環境，`pip` 負責把套件裝進指定的環境。[Python 官方說明](https://docs.python.org/3/tutorial/venv.html)

在本目錄 `exercises/week02_python_engineering` 執行：

```powershell
py -m venv .venv
.\.venv\Scripts\python -m pip install -e ".[dev]"
```

第一行使用 `py` 選定的 Python 執行 `venv` 模組，建立名為 `.venv` 的環境。

### pip：安裝專案與相依套件

第二行使用 `.venv` 裡的 Python 執行 `pip`。指定完整的 Python 路徑，可以明確知道套件安裝到哪個環境，也不需要先執行啟用環境的指令。

- `-m pip`：由這個 Python 執行 pip 模組。
- `install`：安裝套件。
- `-e`：使用開發模式安裝；修改一般 Python 原始碼後，通常不用重新安裝。
- `.`：安裝目前目錄的專案。
- `[dev]`：一起安裝專案定義的開發用額外相依套件。

本專案的 `pyproject.toml` 定義了 `dev = ["pytest>=8.0"]`，所以這個指令也會安裝 pytest。`dev` 是本專案取的名稱，不是 Python 固定內建的一組套件。[pip 開發模式安裝說明](https://pip.pypa.io/en/stable/topics/local-project-installs/)

## module、package 與 src layout

### module：一份可匯入的模組

本專案的 `account.py` 就是一個 module，裡面可以放 class、函式與變數。例如：

```python
from banking.account import Account
```

意思是從 `banking` 套件的 `account` 模組匯入 `Account`。

### package：把相關模組組織起來

`banking` 是一個 package，包含 `account`、`exceptions`、`generators` 等模組。

`__init__.py` 是一般套件的初始化檔案。它可以留空，也可以設定套件對外提供的名稱。你的檔案裡有：

```python
from .account import Account
```

其中 `.` 表示目前套件。這讓外部也可以寫：

```python
from banking import Account
```

Python 另有可省略 `__init__.py` 的 namespace package；本週先理解目前使用的一般套件結構。[Python 模組與套件說明](https://docs.python.org/3/tutorial/modules.html)

### src layout：把套件原始碼放在 src 下

`src` layout 是目錄配置慣例：可匯入的套件放在 `src/` 下，測試與專案設定放在外面。

本專案安裝後使用 `from banking import Account`；`src` 是原始碼的容器，不是匯入名稱的一部分。`pyproject.toml` 的 `where = ["src"]` 告訴建置工具從這裡尋找套件。

這種配置有助於避免程式只是因為從專案根目錄執行而剛好能 import，掩蓋安裝設定的問題。因此先執行前面的安裝指令，再執行測試。[PyPA 目錄配置說明](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)

## class 與 dataclass

### class：把帳戶資料與行為包在一起

以下是簡化的語法示範，不需要用它取代本專案的 `Account`：

```python
class Account:
    def __init__(self, owner: str):
        self.owner = owner

account = Account("Alice")
print(account.owner)  # Alice
```

- `__init__`：初始化物件，作用接近 C# 建構子的初始化部分。
- `self`：目前這個物件，類似 C# 的 `this`；Python 的一般實例方法會明確接收它。
- `self.owner`：這個物件的屬性。
- `Account("Alice")`：建立物件，不需要寫 `new`。

class 可以同時保存資料與定義方法。銀行帳戶的資料包含擁有者與餘額，方法包含存款與提款。[Python class 說明](https://docs.python.org/3/tutorial/classes.html)

### dataclass：自動產生資料類別常用的方法

使用 `dataclass`，前面的初始化可以簡化為：

```python
from dataclasses import dataclass

@dataclass
class Account:
    owner: str

account = Account("Alice")
print(account)  # Account(owner='Alice')
```

`@dataclass` 是套用在類別上的裝飾器，會依欄位與設定產生常見方法。預設包含：

| 方法 | 用途 |
| --- | --- |
| `__init__` | 接收欄位值並初始化物件 |
| `__repr__` | 產生方便檢視物件內容的文字表示 |
| `__eq__` | 比較同類別物件的欄位值是否相等 |

dataclass 仍然是 class，可以自己加入 `deposit()`、`withdraw()` 等方法；預設欄位也可以修改。它不會自動驗證餘額是否合理。

本專案使用 `@dataclass(slots=True)`。`slots=True` 在這個類別中限制實例使用已定義的屬性，並通常減少每個實例的記憶體負擔；它不代表物件不可修改。[Python dataclass 說明](https://docs.python.org/3/library/dataclasses.html)

## typing：標示預期的資料型別

本專案的方法宣告：

```python
def deposit(self, amount: Decimal) -> Decimal:
```

這是方法簽名片段，表示 `amount` 預期是 `Decimal`，回傳值也預期是 `Decimal`。概念上對應 C# 的：

```csharp
public decimal Deposit(decimal amount)
```

Python 的 `Decimal` 來自 `decimal` 標準函式庫，本專案以 `Decimal("100")` 這類寫法表示金額。

**Python 的 type hint 預設不會在執行時強制檢查型別，也不會自動轉型。** 例如：

```python
def identity(value: int) -> int:
    return value

print(identity("hello"))  # 執行時仍會印出 hello
```

編輯器或型別檢查工具可以指出這個呼叫的型別問題，但函式本身沒有執行型別驗證。

因此，`amount: Decimal` 是型別提示；`if amount <= 0:` 則是在執行時檢查金額是否大於零。後者是值的檢查，也不等於完整的型別檢查。[Python typing 說明](https://docs.python.org/3/library/typing.html)

## exception：表達與處理錯誤

本專案在 `exceptions.py` 定義：

```python
class InsufficientFundsError(ValueError):
    """Raised when an account cannot cover a withdrawal."""
```

這個類別繼承 `ValueError`，用來表達「餘額不足」。類別內只有說明字串也合法，代表沒有額外加入方法。

提款金額超過餘額時，`withdraw()` 會執行：

```python
raise InsufficientFundsError("Insufficient funds")
```

呼叫端可以捕捉並處理這個錯誤：

```python
from decimal import Decimal
from banking import Account, InsufficientFundsError

account = Account(owner="Alice", balance=Decimal("50"))

try:
    account.withdraw(Decimal("100"))
except InsufficientFundsError:
    print("餘額不足，請調整提領金額")
```

`raise` 對應 C# 的 `throw`，`except` 對應 `catch`。自訂例外讓呼叫端可以區分金額不合法的 `InvalidAmountError` 與餘額不足的 `InsufficientFundsError`，分別處理。[Python 例外處理說明](https://docs.python.org/3/tutorial/errors.html)

## generator：需要時才逐筆產生資料

以下用整數示範，本專案的 `iter_amounts_at_least()` 則使用 `Decimal` 金額：

```python
def amounts_at_least(amounts, minimum):
    for amount in amounts:
        if amount >= minimum:
            yield amount

result = amounts_at_least([10, 50, 100], 50)

print(next(result))  # 50
print(next(result))  # 100
```

呼叫含有 `yield` 的函式時，先取得 generator，函式主體尚未開始執行。每次 `next()` 才繼續執行，直到遇到下一個 `yield`。

`yield` 交出值後會暫停，保留目前執行位置，下次再接著跑。概念接近 C# iterator 裡的 `yield return amount;`。

這讓函式不用先建立完整的結果 list。上例的輸入 list 仍已存在，省下的是另外建立完整輸出 list 的需求。

同一個 generator 取完後就耗盡了，再呼叫 `next()` 會拋出 `StopIteration`；`for` 迴圈會自動處理這個結束訊號。`list(result)` 則會把剩餘結果全部取出並存成 list。[Python generator 說明](https://docs.python.org/3/tutorial/classes.html#generators)

本專案的型別提示還包含：

- `Iterable[Decimal]`：可以逐筆走訪、每筆預期是 `Decimal` 的輸入，例如 list 或 generator。
- `Iterator[Decimal]`：可以持續取得下一筆 `Decimal` 的物件；這個函式回傳的 generator 就是 iterator。

## pytest：把預期行為寫成自動測試

例如存款測試可以寫成：

```python
from decimal import Decimal
from banking import Account

def test_deposit_updates_balance():
    account = Account(owner="Alice")

    account.deposit(Decimal("100"))

    assert account.balance == Decimal("100")
```

這對應 C# 測試常見的 Arrange → Act → Assert：準備帳戶、執行存款、檢查餘額。

pytest 會依命名規則尋找測試，例如 `test_account.py` 裡的 `test_` 開頭函式。`assert` 條件不成立時，測試就會失敗。

預期某個操作會拋出例外時，可以寫：

```python
from decimal import Decimal
import pytest
from banking import Account, InvalidAmountError

def test_deposit_rejects_zero():
    account = Account(owner="Alice")

    with pytest.raises(InvalidAmountError):
        account.deposit(Decimal("0"))
```

這個測試預期存入零元會拋出 `InvalidAmountError`。若沒有拋出例外，測試反而會失敗。[pytest 官方入門](https://docs.pytest.org/en/stable/getting-started.html)

你現有的帳戶測試還使用 `@pytest.mark.parametrize`，讓同一個測試分別使用零與負數執行，不用重複寫兩份測試。

## 練習順序

1. 閱讀 `tests/test_account.py`，把每個測試翻成一句中文預期行為，例如「存入 100 後，餘額應該是 100」。
2. 對照 `account.py` 的實作，完成尚未實作的部分；已有實作則逐段確認邏輯。
3. 執行測試：

```powershell
.\.venv\Scripts\python -m pytest
```

## 完成標準

- 所有 pytest 測試通過。
- 能解釋 `__init__.py` 的用途。
- 能解釋 dataclass 與一般 class 的差異。
- 能解釋 type hint 不等於 runtime validation。
- 能解釋 generator 為何不必一次建立完整 list。
