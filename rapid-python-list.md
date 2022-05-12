# だいたい正しい Python 入門２

Copyright © 2022 IDEHARA, Norimimichi. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the license is included in the section entitled “GNU Free Documentation License”.

---
subtitle: 初心者のためのリストと繰り返し処理

author:
- "出原至道 (idehara@tama.ac.jp)"

date: \today{}

---

## リストを使いこなそう

### リストから１個ずつ取り出そう

```Python
a = [1,7,3,2]
for x in a:
    print(a)
```

リストの要素を１個ずつ取り出しては計算に使うのが `for - in` 構文です。

```Python
for 要素をうけとる変数 in リスト:
    受け取った要素についての処理
```

`for - in` 構文では、リストの中から１個ずつ要素を読み取り、「要素をうけとる変数」に代入してから、ブロック内を実行します。

- 繰り返しの回数は、リストの要素数回です。
- 最初から順番に要素を読み出します。リストと

例：
```Python
a = list('hello')
for c in a:
    print(c)
```

---

### 回数を決めて実行しよう

```Python
for i in range(5):
    print(i, 'Hello')
```

`for - in` 構文で、`in` 節に `range(数値)` を指定すると、指定した数値の回数だけブロックを繰り返します。

- `range(数値)` は、「`[0, 1, ..., 数値-1]` というリストのようなもの」です。（実際にはリストでありません）
- このとき、「取り出した要素」には、0 から 数値-1 までの値が入ります。
- ちょうど、長さ `n` のリストの要素が [0] から [n-1] までなので、リストの要素を順番に処理するときにも使えます。
    - 例によって「0 から始まる」ところに注意！
    - リストの要素を１個ずつ取り出すだけなら、素直な `for - in` 構文のほうが楽です。
- （ちょっと高度）「取り出した要素」の「0 から 数値-1 までの値」には興味がなく、回数だけ指定して繰り返したい場合には、変数名に `_` を使うのが python の風習です。


例：
```Python
for i in range(5):
    print(i+1, '番目の奇数は', 2*i+1, 'です')
```

```Python
a ='hello''
for _ in range(10):
    print(a)
```

---

### リストの要素を増やそう

```Python
a = []
for i in range(5):
    a.append(i)
print(a)
```

リストの最後に要素を追加するときには、リスト型の変数の後ろに `.append(要素)` という命令を書きます。

- `append` 命令は、リスト型の変数にしか使えない命令です。
- `a = []` は、「空のリストを書き込みます」という意味です。このあと、`a` をリスト型として扱うために必要な命令です。

例（奇数を順番に足していきます）：
```Python
a = [0]
for i in range(7):
    a.append(a[i] + (2*i+1))
print(a)
```

---

### リストと if を組み合わせよう

```Python
print('好きな自然数を入れてください')
s = input()
ns = list(s)
print(ns)
if '0' in ns:
    print('０が入っています')
```

リストで使える演算子に `in`, `not in` があります。

- `要素 in リスト` の形で「リストに要素が含まれるならば」を表します。
- `要素 not in リスト` の形で「リストに要素が含まれないならば」を表します。
- 要素の項目を `[]` で取り出して条件式に使うこともできます。

例（色々な数を入力して、すべての場合を試してみよう）：
```Python
print('好きな自然数を入れてください')
s = input()
ns = list(s)
print(ns)
if '0' not in ns:
    print('０が入っていません')
if ns[-1] == '1':
    print('１で終わっています')
```