# だいたい正しい Python 入門（３）

Copyright © 2022 IDEHARA, Norimimichi. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the license is included in the section entitled “GNU Free Documentation License”.

---
subtitle: 初心者のための関数定義

author: "出原至道 (idehara@tama.ac.jp)"

date: \today{}

---

\newpage

## 関数定義を使いこなそう

### 関数の定義

```Python
def getHello(message,count):
    m = message * count
    return m

s = getHello('hello', 10)
print( s )
```

これまで、他の人が用意してくれている「関数」を使ってきました。関数は `( )` のついた形の命令でしたね。たとえば：

```Python
x = [1,2,3]

n = len(x)
# 配列の長さ（要素の個数）を答えてくれる関数

print( n )  
# 「画面にものを表示する」仕事をしてくれる関数。
# 答えは期待していない
```

python では、この「関数」を、自分で新しく作ることができます。

関数の作り方
```Python
def 新しく作る関数の名前 ( 引数リスト ):
    処理の中身
    return 関数の答
```
- 関数に渡す値を **引数**（ひきすう）と呼びます。素直に「いんすう」と読みたくなりますが、通常「いんすう」は「因数」を表します。

- 関数から返される値を**戻り値**（もどりち）と呼びます。 **返り値**（かえりち）と呼ぶ人もいます。

- 「引数リスト」の変数には、呼び出した人が関数に渡した値が代入されてから、関数が実行されます。関数の外側に同じ名前の変数があっても、それとは無関係な変数です。この関数の中でだけ存在している変数です。

- 関数の中で使った変数も、関数の外からは見えません。関数の中でだけ存在しています。

- 「関数の中身」で `return 値` という命令を実行すると、値を戻り値として、関数の実行を**直ちに終了**します。その先は実行されません。

- 一つの関数の中で、あちこちに `return` が出てきてもかまいません。ただし、`return` を実行したとたんに関数が終了することには注意しましょう。



例：
```Python
def getHello(message,count):
    if count<1:
        return '回数がおかしいです'
    print(message,'を',count,'回繰り返します')
    m = message * count
    return m

s = getHello('hello', 10)
print( s )
s2 = getHello('world', -5)
print( s2 )
```

```Python
def getHello(message,count):
    if count<1:
        return '回数がおかしいです'
    print(message,'を',count,'回繰り返します')
    m = message * count
    return m

s = getHello('hello', 10)
print( s )
print( m )
```

---
### 関数の副作用・変数のスコープ

```python
def addNumber(x,y):
    x = x * 10 + y
    return x

x = 3
print( addNumber(x,1) )
print( addNumber(x,3) )
print( x )
print( y )
```


関数の中で「引数を受け取って、それに基づいた答を返す」以外の動作が行われることがあります。たとえば、画面に何かを表示したり、ほかの変数を直接参照したり、書き換えたりすることがこれに当たります。これを **副作用** と呼びます。副作用のある関数は、デバッグが難しくなるために、できれば避けたほうがよいです。

- 変数を参照できる場所を **変数のスコープ** と呼びます。

- この例で、関数の引数として定義されている変数 `x` と、関数の外側で定義されている変数 `x` は、全くの別物です。
- 関数の内側で定義されている変数を、関数の外側から参照することはできません。関数の内側の変数のスコープは、関数内に限定されます。
- 関数の外側で定義されている変数は、**関数内で同じ名前の変数が定義されていなければ関数内で参照することができます**。ただし（通常は）値を代入することはできません。
  - むりやり関数の外部の変数を書き換える方法はありますが、予想のつかない副作用が発生する・エラーの温床になるなど、ろくなことにならないので、使わないように。
- 外部の変数の参照ができるからといっても、可能であれば引数で渡すようにするべきです。副作用のある関数は、読みにくく、保守しにくいコードになります。

例：
```python
# 良くないプログラム例
def getHello(message):
    m = message * count
    return m

count = 3
print( getHello('hello') )
count = 5
print( getHello('world') )
```

---
### さまざまな戻り値　（高難度）

```Python
def getSumAverage(x):
    s = sum(x)
    a = s / len(x)
    return [s,a]

point = [60,80,55]
print( getSumAverage(point) )
```

ここまでの例では、戻り値に単純な数値や文字・文字列を返しました。しかし、python では、どのような型でも返すことができます。

- これまでに知っている範囲では、「リスト」を使うことで、複数の答を返すことができます。
- その他、辞書型・集合型・タプル・関数（！）など、およそ何でも戻り値にできます。

```Python
import math
# ２次方程式を解いてくれる関数。
# 答はタプルで返ってくるので、２変数を並べて受け取れる
def solve2(a,b,c):
    q = math.sqrt( b*b - 4*a*c )
    x1 = -b + q
    x2 = -b - q
    return (x1,x2)

a1,a2 = solve2(1,-3,2)
print(a1,a2)
```

```Python
# 文字列に使われている文字を教えてくれる関数
# 答は集合型
def letters(s):
    charSet = set(list(s))
    return charSet

print( letters('tamadai') )
```

```Python
# 文字列に使われている文字の出現回数を数えてくれる関数
# 答は辞書型
def letterCount(s):
    ans = dict()
    for c in s:
        if c in ans:
            ans[c] +=1
        else:
            ans[c] = 1
    return ans

print( letterCount('tamadai') )
```

```Python
# 指定した２次関数を作ってくれる関数
# 答に返ってくるのは「関数」なので、それを呼ぶことができる
def createFunction(a,b,c):
    return lambda x : a*x*x + b*x + c

f1 = createFunction(1,0,0)
f2 = createFunction(1,2,1)
print(f1(0),f1(1),f1(2))
print(f2(0),f2(1),f2(2))
```

---
### 関数の再定義（要注意！）

```Python
def len(x):
    return 1000

a = [1,2,3]
print( len(a) )
```

すでに存在している関数を、再定義することができます。あとから定義したほうが有効になります。

- うっかり、基本関数（`len` とか `print` とか）を再定義してしまうと、何が何やらわからない動作をします。注意しましょう。
- 基本関数を**変数で上書きする**のも、初心者がよく起こす間違いです。注意しましょう。

```Python
# print 回数だけ hello を表示するプログラム……のはず
print = 10
s = 'hello'
for _ in range(print):
    print(s)
```



