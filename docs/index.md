---
title:
---


# 物理シミュレーション

説明スライドはCoursePowerに置きます。


## ノートブック

<!-- textlint-disable
ja-technical-writing/no-unmatched-pair,
ja-technical-writing/sentence-length,
ja-technical-writing/max-comma,
ja-technical-writing/max-kanji-continuous-len
-->

1. [高機能な電卓](previews/01_高機能な電卓.html) [![Download ipynb](https://img.shields.io/badge/download-ipynb-brightgreen.svg?logo=jupyter)](notebooks/01_%E9%AB%98%E6%A9%9F%E8%83%BD%E3%81%AA%E9%9B%BB%E5%8D%93.ipynb){: download=01_高機能な電卓.ipynb} [![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tueda/PS2022SS/gh-pages?filepath=notebooks/01_%E9%AB%98%E6%A9%9F%E8%83%BD%E3%81%AA%E9%9B%BB%E5%8D%93.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tueda/PS2022SS/blob/gh-pages/notebooks/01_%E9%AB%98%E6%A9%9F%E8%83%BD%E3%81%AA%E9%9B%BB%E5%8D%93.ipynb?hl=ja)
    - 基本的な算術演算（`+`, `-`, `*`, `/`, `//`, `%`, `**`）
    - 変数
    - データ型（`int`, `float`, `str`）
    - ユーザー入力と出力（`input`, `print`）
    - 数学関数（`import math`）
1. [条件分岐](previews/02_条件分岐.html) [![Download ipynb](https://img.shields.io/badge/download-ipynb-brightgreen.svg?logo=jupyter)](notebooks/02_%E6%9D%A1%E4%BB%B6%E5%88%86%E5%B2%90.ipynb){: download=02_条件分岐.ipynb} [![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tueda/PS2022SS/gh-pages?filepath=notebooks/02_%E6%9D%A1%E4%BB%B6%E5%88%86%E5%B2%90.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tueda/PS2022SS/blob/gh-pages/notebooks/02_%E6%9D%A1%E4%BB%B6%E5%88%86%E5%B2%90.ipynb?hl=ja)
    - `if`文
    - 比較演算
    - ブール演算
    - じゃんけんゲーム
1. [反復処理](previews/03_反復処理.html) [![Download ipynb](https://img.shields.io/badge/download-ipynb-brightgreen.svg?logo=jupyter)](notebooks/03_%E5%8F%8D%E5%BE%A9%E5%87%A6%E7%90%86.ipynb){: download=03_反復処理.ipynb} [![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tueda/PS2022SS/gh-pages?filepath=notebooks/03_%E5%8F%8D%E5%BE%A9%E5%87%A6%E7%90%86.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tueda/PS2022SS/blob/gh-pages/notebooks/03_%E5%8F%8D%E5%BE%A9%E5%87%A6%E7%90%86.ipynb?hl=ja)
    - `while`文と`for`文
    - 数当てゲーム
    - リストと`range`オブジェクト
    - 覆面算
    - 【発展】円周率の級数表示
1. 関数
1. グラフの描画
1. 文字列処理
1. 乱数
1. モンテカルロ法
1. ランダムウォーク
1. フラクタル
1. セルオートマトン
1. 方程式の解
1. 運動のシミュレーション
1. まとめ演習

<!-- don't want to merge two consecutive lists -->

- [動作確認](previews/00_動作確認.html) [![Download ipynb](https://img.shields.io/badge/download-ipynb-brightgreen.svg?logo=jupyter)](notebooks/00_%E5%8B%95%E4%BD%9C%E7%A2%BA%E8%AA%8D.ipynb){: download=00_動作確認.ipynb} [![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tueda/PS2022SS/gh-pages?filepath=notebooks/00_%E5%8B%95%E4%BD%9C%E7%A2%BA%E8%AA%8D.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tueda/PS2022SS/blob/gh-pages/notebooks/00_%E5%8B%95%E4%BD%9C%E7%A2%BA%E8%AA%8D.ipynb?hl=ja)
    - ホフスタッターの蝶

<!-- textlint-enable -->


## Jupyterノートブックプレビューア

- [kokes/nbviewer.js: live demo](https://kokes.github.io/nbviewer.js/viewer.html)（Ondrej Kokes氏）：
`.ipynb`ファイルをドラッグ・アンド・ドロップすると、その内容が表示されます。


<!-- textlint-disable
ja-engineering-paper/prh,
ja-technical-writing/ja-no-weak-phrase
-->

## 参考になる（かもしれない）Web上のドキュメント

<!-- textlint-enable -->


<!-- textlint-disable
ja-technical-writing/sentence-length,
ja-technical-writing/ja-no-redundant-expression,
ja-technical-writing/ja-no-weak-phrase,
jtf-style/4.1.1.句点(。)
-->

この講義では扱わないものの、よく使われるPythonの機能として次のものが挙げられます。これらについては、必要となったときに学習するとよいでしょう。

- クラスの定義
- ファイルの入出力
- 辞書型などのデータ構造
- 例外および例外処理

さらに、次のことも知っておくと有益かもしれません。

- よく使われる標準ライブラリおよびサードパーティのライブラリ
- 非同期処理・並列処理
- docstringや型ヒントの書き方
- アプリケーションおよびライブラリのパッケージング・単体テスト
- （Pythonに限らず）もっと高度な計算アルゴリズムやデータ構造

そのために、次のWebサイトが参考になるかもしれません。

<!-- textlint-enable -->


<!-- textlint-disable
ja-technical-writing/sentence-length,
ja-technical-writing/max-kanji-continuous-len
-->

- [ゼロからのPython入門講座](https://www.python.jp/train/index.html)（Python Japan）：
  プログラミング入門者向けのチュートリアル。
- [Python チュートリアル](https://docs.python.org/ja/3/tutorial/)（Python Software Foundation）：
  Python公式サイト（本家）のチュートリアルの日本語訳。ほかのプログラミング言語でのプログラミング経験のある人向けのような気もする。
- [ゼロから学ぶPython](https://kaityo256.github.io/python_zero/)（渡辺宙志氏）：
  Web上に公開されている講義録。後半はシミュレーションや機械学習も。本になっている。
- [Pythonで学ぶコンピュテーショナル・シンキングとデータ科学](https://wagtail.cds.tohoku.ac.jp/coda/python/index.html)（早川美徳氏）：
  ボリュームのある講義録。データ科学寄り。
- [コンピュータ処理](https://amorphous.tf.chiba-u.jp/lecture.files/chem_computer/index.html)（大窪貴洋氏）：
  化学屋さん寄り（たぶん）のPythonの講義録。
- [Pythonプログラミング入門](https://utokyo-ipp.github.io/index.html)（東京大学数理・情報教育研究センター）：
  Pythonの詳細な講義録。
- [プログラミング演習 Python 2021](https://hdl.handle.net/2433/265459)（喜多一氏、森村吉貴氏、岡本雅子氏）：
  PDFファイルとして公開されている講義録。
- [機械学習帳](https://chokkan.github.io/mlnote/)（岡崎直観氏）：
  Pythonによる機械学習の講義資料。
- [Introduction to Computer Science and Programming in Python](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)（MIT OpenCourseWare）：
  Pythonによるプログラミング入門（英語）。
- [Scipy Lecture Notes](https://scipy-lectures.org/)
  Pythonを用いた科学技術計算のチュートリアル（英語）。
- [Python Programming And Numerical Methods: A Guide For Engineers And Scientists](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html)（Qingkai Kong氏、Timmy Siauw氏、Alexandre Bayen氏）：
  プログラミング＆数値計算の入門者向けの本のネット公開版（英語）。

<!-- textlint-enable -->
