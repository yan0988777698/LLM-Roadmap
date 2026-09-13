# Week 01 — Python Syntax for C# Developer

## 學習目標

- 理解 List、Tuple、Set、Dict 的特性與適用情境。
- 使用 comprehension 簡潔地轉換或篩選資料。
- 使用 `enumerate()` 同時取得索引和值。
- 使用 `zip()` 逐筆配對多組資料。
- 將熟悉的 C# 演算法改寫成 Python，並分析時間與空間複雜度。

這週先熟悉後續資料處理與機器學習程式會反覆使用的 Python 語法。以下用 C#／.NET 概念對照，搭配本目錄的 collections 與 Two Sum 範例說明。

## 概念與 C# 對照

| Python 名稱 | 用途 | C#／.NET 概念對照 |
| --- | --- | --- |
| `list` | 有順序、可修改、可包含重複值的集合 | `List<T>` |
| `tuple` | 有順序、建立後不能修改的集合 | ValueTuple，例如 `(int Id, string Name)`；語意不完全相同 |
| `set` | 儲存不重複元素，適合成員查找與集合運算 | `HashSet<T>` |
| `dict` | 以唯一 key 對應 value | `Dictionary<TKey, TValue>` |
| comprehension | 由可迭代資料轉換或篩選出新集合 | 常見用途接近 LINQ 的 `Select()`／`Where()` |
| `enumerate()` | 走訪資料時同時取得索引和值 | 可類比 LINQ 帶 index 的 `Select()` |
| `zip()` | 將多組可迭代資料逐筆配對 | `Enumerable.Zip()` |
| `in` | 判斷元素或 key 是否存在 | `Contains()`／`ContainsKey()` |

這些是方便入門的概念對照，不表示兩種語言的型別與執行行為完全相同。

## 專案結構

```text
week01_python_syntax/
├─ README.md
├─ collections_demo.py
└─ two_sum.py
```

各檔案的用途：

| 檔案 | 用途 |
| --- | --- |
| [collections_demo.py](collections_demo.py) | 示範四種 collection、comprehension、`enumerate()` 與 `zip()` |
| [two_sum.py](two_sum.py) | 使用 Dict 實作 Two Sum，並以三個案例驗證結果 |

## 執行方式

在本目錄 `exercises/week01_python_syntax` 執行：

```powershell
python collections_demo.py
python two_sum.py
```

`collections_demo.py` 會印出各種集合操作的結果。Set 沒有用來表示固定位置，因此不應依賴它的輸出順序。

`two_sum.py` 的三個 `assert` 都通過時會印出：

```text
All tests passed.
```

如果任何 `assert` 的條件不成立，程式會拋出 `AssertionError`。

## List：有順序且可以修改

建立 List：

```python
numbers = [1, 2, 3, 4, 5]
```

List 保留元素順序、允許重複值，而且可以在建立後修改。索引從 `0` 開始：

```python
print(numbers[0])   # 1
print(numbers[-1])  # 5，-1 代表最後一個元素

numbers.append(6)
print(numbers)      # [1, 2, 3, 4, 5, 6]
```

`append()` 會把一個元素加入尾端。切片則可以取出一段資料：

```python
print(numbers[1:4])  # [2, 3, 4]
```

`1:4` 包含索引 `1`，但不包含索引 `4`。切片通常會建立新的 List。[Python List 說明](https://docs.python.org/3/tutorial/introduction.html#lists)

適合使用 List 的情況包括：

- 需要保留資料順序。
- 需要使用索引取得元素。
- 需要新增、刪除或修改元素。
- 允許出現重複值。

## Comprehension：轉換或篩選資料

`collections_demo.py` 使用 List comprehension 計算平方：

```python
squares = [number**2 for number in numbers]
```

它等同於：

```python
squares = []
for number in numbers:
    squares.append(number**2)
```

基本結構是：

```text
[輸出運算式 for 暫存變數 in 可迭代資料]
```

也可以加入條件，只保留偶數：

```python
even_numbers = [number for number in numbers if number % 2 == 0]
```

可以讀成：「逐一取得 `numbers` 裡的 `number`；如果它能被 2 整除，就把它放進新的 List。」

Comprehension 適合簡短的轉換與篩選。如果包含很多巢狀迴圈、條件或副作用，改用一般 `for` 迴圈通常更容易閱讀。[Python List comprehension 說明](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

## Dict：用 key 查找 value

建立 Dict：

```python
users = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
}
```

每筆資料由 `key: value` 組成：

```text
1 → "Alice"
2 → "Bob"
3 → "Charlie"
```

加入或更新資料時使用中括號：

```python
users[4] = "David"  # 新增
users[2] = "Bobby"  # 更新既有 key
```

同一個 Dict 中的 key 必須唯一。再次指定相同 key 會更新它的 value，而不是增加第二個相同 key。

### 中括號與 get() 的差異

```python
print(users[2])      # Bobby
print(users.get(2))  # Bobby
```

key 存在時，兩種寫法都能取得 value。key 不存在時則不同：

```python
users[99]                   # 拋出 KeyError
users.get(99)               # 回傳 None
users.get(99, "Not found")  # 回傳指定的預設值
```

如果缺少 key 代表程式錯誤，可以使用 `users[key]`；如果缺少 key 是正常情況，可以使用 `get()` 並明確處理結果。

### 走訪 key 與 value

```python
for user_id, name in users.items():
    print(f"{user_id}: {name}")
```

`items()` 每次提供一組 `(key, value)`，接著透過 tuple unpacking 分別存入 `user_id` 和 `name`。[Python Dict 說明](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

## Set：唯一元素與集合運算

List 轉成 Set 後，重複元素只會保留一份：

```python
numbers = [1, 1, 2, 2, 3, 4]
unique_numbers = set(numbers)

print(unique_numbers)  # 元素為 1、2、3、4；不要依賴顯示順序
```

Set 適合執行數學上的集合運算：

```python
first_group = {1, 2, 3}
second_group = {3, 4, 5}

print(first_group & second_group)  # 交集：{3}
print(first_group | second_group)  # 聯集：{1, 2, 3, 4, 5}
print(first_group - second_group)  # 差集：{1, 2}
```

符號的意思：

| 運算 | 名稱 | 結果 |
| --- | --- | --- |
| `A & B` | 交集 | 同時存在於 A 和 B 的元素 |
| `A \| B` | 聯集 | 存在於 A 或 B 的所有元素 |
| `A - B` | 差集 | 存在於 A、但不存在於 B 的元素 |
| `value in A` | 成員檢查 | 判斷 value 是否在 A 中 |

空 Set 必須寫成 `set()`；`{}` 建立的是空 Dict。[Python Set 說明](https://docs.python.org/3/tutorial/datastructures.html#sets)

## Tuple：建立後不能修改

`collections_demo.py` 使用 Tuple 表示一組使用者資料：

```python
user = (1, "Alice", "admin")
```

Tuple 有順序，也能使用索引，但建立後不能替換、新增或刪除其中的元素：

```python
print(user[0])  # 1
user[0] = 2     # TypeError
```

可以透過 tuple unpacking 一次取出各欄位：

```python
user_id, name, role = user
print(f"ID={user_id}, name={name}, role={role}")
```

左側變數數量必須與 Tuple 元素數量一致，否則會拋出 `ValueError`。

Tuple 適合表示一組不希望被修改、位置意義固定的值，也常用來回傳多個結果。只有一個元素的 Tuple 必須保留逗號：

```python
single = (1,)
```

[Python Tuple 說明](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

## enumerate()：同時取得索引和值

一般 `for` 迴圈只取得元素：

```python
for name in names:
    print(name)
```

需要編號時可以使用 `enumerate()`：

```python
names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")
```

輸出：

```text
1. Alice
2. Bob
3. Charlie
```

`start=1` 只改變產生的第一個編號，不會改變 List 本身仍從索引 `0` 開始的規則。省略時預設從 `0` 開始。

這通常比手動維護 `index += 1` 更清楚，也比較不容易讓索引和值不同步。[Python enumerate 說明](https://docs.python.org/3/library/functions.html#enumerate)

## zip()：逐筆配對資料

假設姓名和分數分別放在兩個 List：

```python
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 95]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

`zip()` 依相同位置配對：

```text
("Alice", 90)
("Bob", 85)
("Charlie", 95)
```

預設情況下，如果輸入長度不同，`zip()` 會在最短的一組資料用完時停止：

```python
list(zip(["Alice", "Bob"], [90]))
# [("Alice", 90)]
```

如果長度不同代表資料錯誤，在支援的 Python 版本可以使用 `strict=True`，讓長度不一致時拋出 `ValueError`：

```python
list(zip(["Alice", "Bob"], [90], strict=True))
```

[Python zip 說明](https://docs.python.org/3/library/functions.html#zip)

## Two Sum：用 Dict 將重複搜尋變成一次走訪

題目：給定一組整數與目標值，找出兩個相加等於目標值的元素索引。

```python
def two_sum(numbers: list[int], target: int) -> tuple[int, int] | None:
    num_dict: dict[int, int] = {}

    for i, num in enumerate(numbers):
        complement = target - num

        if complement in num_dict:
            return num_dict[complement], i

        num_dict[num] = i

    return None
```

`num_dict` 的內容是：

```text
已看過的數字 → 該數字的索引
```

例如：

```python
numbers = [2, 7, 11, 15]
target = 9
```

執行過程：

| `i` | `num` | `complement = 9 - num` | 查找結果 | 動作 |
| ---: | ---: | ---: | --- | --- |
| 0 | 2 | 7 | Dict 中沒有 7 | 記錄 `2: 0` |
| 1 | 7 | 2 | 找到 `2: 0` | 回傳 `(0, 1)` |

回傳 `(0, 1)` 是索引，不是數字本身：

```python
numbers[0] + numbers[1] == 2 + 7 == 9
```

程式先查找 `complement`，再把目前的 `num` 放入 Dict。這個順序可以避免同一個元素被使用兩次。例如 `[3]`、target `6` 不應該把唯一的索引 `0` 使用兩次。

如果走完整個 List 都沒有答案，函式回傳 `None`：

```python
two_sum([1, 2, 3], 99) is None
```

## Two Sum 複雜度

設輸入長度為 `n`：

- 時間複雜度：平均 `O(n)`。
- 空間複雜度：`O(n)`。

原因是每個數字最多走訪一次，而 Dict 的 key 查找與新增平均為 `O(1)`。最差情況下需要將每個走過的數字與索引存進 Dict，因此額外空間隨輸入長度成長。

如果改成兩層迴圈檢查所有數字組合，時間複雜度會是 `O(n²)`。使用 Dict 是用額外的 `O(n)` 空間換取較快的平均查找速度。

## assert：建立可重複執行的檢查

`two_sum.py` 的 `main()` 包含三個案例：

```python
assert two_sum([2, 7, 11, 15], 9) == (0, 1)
assert two_sum([3, 2, 4], 6) == (1, 2)
assert two_sum([1, 2, 3], 99) is None
```

它們分別檢查：

- 答案位於前兩個元素。
- 答案不是相鄰的第一組元素。
- 找不到答案時回傳 `None`。

`assert` 條件成立時不會輸出內容；條件不成立時會拋出 `AssertionError`。這是本週的輕量驗收方式，Week 02 會再使用 pytest 把測試整理成獨立且可自動收集的測試函式。

## main guard：直接執行與匯入時採取不同行為

兩支程式最後都有：

```python
if __name__ == "__main__":
    main()
```

直接執行檔案時，Python 會把 `__name__` 設為 `"__main__"`，所以呼叫 `main()`：

```powershell
python two_sum.py
```

從其他檔案匯入時，`main()` 不會自動執行：

```python
from two_sum import two_sum
```

這讓函式可以被其他程式或測試重複使用，而不會在 import 時執行範例輸出。[Python `__main__` 說明](https://docs.python.org/3/library/__main__.html)

## 常用操作與複雜度

以下是本週常用操作的一般平均情況；實際成本仍會受到資料量、碰撞與實作細節影響。

| 操作 | List | Tuple | Set | Dict |
| --- | ---: | ---: | ---: | ---: |
| 以索引取得元素 | `O(1)` | `O(1)` | 不支援 | 不適用 |
| `value in collection` | `O(n)` | `O(n)` | 平均 `O(1)` | 平均 `O(1)`，檢查的是 key |
| 尾端新增 | `append()` 攤銷 `O(1)` | 不可修改 | `add()` 平均 `O(1)` | 以 key 新增平均 `O(1)` |
| 保留重複元素 | 是 | 是 | 否 | key 不重複，value 可重複 |

選擇方式可以先記成：

- 需要順序、索引與修改：List。
- 一組建立後不應修改的值：Tuple。
- 需要去除重複或快速檢查成員：Set。
- 需要透過 key 快速找到 value：Dict。

## 練習順序

1. 執行 `collections_demo.py`，將每一段輸出對應回原始碼。
2. 不看程式，分別說明 List、Tuple、Set、Dict 的特性與一個適用情境。
3. 將 List comprehension 改寫成一般 `for` 迴圈，再確認結果相同。
4. 用紙筆走一次 `[2, 7, 11, 15]` 的 Two Sum，記錄每一步 Dict 的內容。
5. 執行 `two_sum.py`，確認三個案例通過。

## 完成標準

- `collections_demo.py` 可以成功執行。
- `two_sum.py` 的三個案例全部通過。
- 能說明 List、Tuple、Set、Dict 的差異與選擇方式。
- 能解釋 comprehension、`enumerate()` 與 `zip()` 的用途。
- 能解釋 Two Sum 為什麼使用 Dict。
- 能說明 Two Sum 的平均時間複雜度為 `O(n)`、空間複雜度為 `O(n)`。
