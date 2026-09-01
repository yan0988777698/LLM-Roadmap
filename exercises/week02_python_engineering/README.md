# Week 02 — Python Engineering Basics

## 學習目標

- 使用 `venv` 與 `pip` 建立隔離環境。
- 理解 module、package 與 `src` layout。
- 練習 class、dataclass、typing 與自訂 exception。
- 使用 generator 處理逐筆資料。
- 使用 pytest 撰寫可重複執行的測試。

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

## 建立環境

在本目錄執行：

```powershell
py -m venv .venv
.\.venv\Scripts\python -m pip install -e ".[dev]"
```

## 練習順序

1. 閱讀 `tests/test_account.py` 的預期行為。
2. 完成 `account.py` 內的三個 `TODO`。
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

