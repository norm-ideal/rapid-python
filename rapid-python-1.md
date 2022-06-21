# だいたい正しい Python 入門（１）

Copyright © 2022 IDEHARA, Norimimichi. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the license is included in the section entitled “GNU Free Documentation License”.

---
subtitle: 初心者のための条件分岐演習

author: "出原至道 (idehara@tama.ac.jp)"

date: \today{}

---

\newpage

## 条件分岐

### あるときだけ実行できるようになろう

```Python
print('あなたの年齢を入れてください')
y = int( input() )
if y<6:
    print('本当ですか？')
print( y, '歳ですね' )
```

条件判断をする `if` 命令を使うと、「このときにだけ命令を実行して欲しい」という指示を書けます。「このときに」を表す式を「条件式」と呼びます。

書き方：
```Python
if 条件式:
    条件に当てはまったときに実行したい命令１
    条件に当てはまったときに実行したい命令２
    条件に当てはまったときに実行したい命令３
    ……
普通に実行したい命令
……
```

- python では、特定のプログラムの要素の影響にある部分（ブロック）を、行の最初を下げて表します。
- スペースの数は、通常４つのスペースを使います。
    - 他の人と一緒に作業するときには、別の指定があるかもしれません。それに従ってください。
- 条件式で使える代表的な記号：
    - 大小比較 `<`, `>`, `<=`, `>=` （＝を後ろに書くことに注意）
    - 等しい・等しくない `==`, `!=` （「等しい」は＝を２個書く。１個だと「代入」）

例（色々な数を入力して、すべての場合を試してみよう）：
```Python
print('好きな自然数を入れてください')
s = input()
ni = int(s)
print(ni)
if ni % 7 == 0:
    print('７の倍数です')
if ni % 11 == 0:
    print('11 の倍数です')
if ni % 13 == 0:
    print('13 の倍数です')
```

---

### if を組み合わせよう

```Python
print('好きな自然数を入れてください')
n = int( input() )
if n % 7 == 0:
    print('７の倍数です')
    if n % 11 == 0:
        print('しかも 11 の倍数です')
```

`if` のブロックの中に `if` を書くことができます。

- どんどんブロックが深くなります。
- ブロックの中は、外側の `if` が成り立たないと実行されないことに注意してください。

例（色々な数を入力して、すべての場合を試してみよう）：
```Python
print('好きな自然数を入れてください')
n = int( input() )
if n % 7 == 0:
    print('７の倍数です')
    if n % 11 == 0:
        print('しかも 11 の倍数です')
        if n % 13 == 0:
            print('しかも 13 の倍数です')
```

---

### 「……でないとき」が書けるようになろう

```Python
print('あなたの年齢を入れてください')
y = int( input() )
if y<18:
    print('未成年です')
else:
    print('成年です')
```

`if` の条件ブロックが終了した直後に `else:` を置くことで、「そうでないならば」というブロックを始められます。

- `if`,`else` などに限らず、「次の行から新しいブロックを始める」とき、`:`（コロン）を行の最後に書きます。
- `else` は、`if` と同じ高さまで文字を下げます。

書き方：
```Python
if 条件式:
    条件にあったときのブロック
else:
    条件に合わなかったときのブロック
```

例（色々な数を入力して、すべての場合を試してみよう）：
```Python
print('あなたの年齢を入れてください')
y = int( input() )
if y<18:
    print('未成年です')
else:
    if y<20:
        print('成年ですが、お酒はまだダメです')
    else:
        print('お酒 OK です')
```

---

### （ちょっと高度）「そうでなくて〜ならば」が書けるようになろう

```Python
print('あなたの年齢を入れてください')
y = int( input() )
if y<18:
    print('未成年です')
elif y<20:
    print('成年ですが、お酒はまだダメです')
else:
    print('お酒 OK です')
```

「〜でないときに、〜ならば」という条件が、プログラミングではよく出てきます。これまでの書き方では、条件が多くなると、

```
if xxx:
    ...
else:
    if yyy:
        ...
    else:
        if zzz:
            ...
        else:
            ...
```

となって、どんどん行の頭が下がっていってしまいます。これを簡単に書くために「そうでなくて〜ならば」を書くための命令が `elif:` です。これを使うと、

```
if xxx:
    ...
elif yyy:
    ...
elif zzz:
    ...
else:
    ...
```

と簡単に書くことができます。（とくにこれを使わなくても、if - else で頑張って書くこともできます）

例：とくになし

---

ここまでで、基礎的な入出力・条件分岐の命令をマスターしました。TOPSIC のレベル１、AtCoder のレベル A がほとんど解けるはずです。

---

## 練習問題
