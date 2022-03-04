# テストページ

This is a test page. Never mind.

<!-- textlint-disable
ja-technical-writing/no-mix-dearu-desumasu
-->

これはテスト用のページであり、ノートブックの内容は公開前に変更されることがあります。

<!-- textlint-enable -->


## ノートブック

1. 高機能な電卓
1. 条件分岐
1. 反復処理
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

- [動作確認](https://nbviewer.jupyter.org/github/tueda/PS2022SS/blob/develop/notebooks/00_%E5%8B%95%E4%BD%9C%E7%A2%BA%E8%AA%8D.ipynb) [![Download ipynb](https://img.shields.io/badge/download-ipynb-brightgreen.svg?logo=jupyter)](https://raw.githubusercontent.com/tueda/PS2022SS/develop/notebooks/00_%E5%8B%95%E4%BD%9C%E7%A2%BA%E8%AA%8D.ipynb) [![Launch Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tueda/PS2022SS/develop?filepath=notebooks/00_%E5%8B%95%E4%BD%9C%E7%A2%BA%E8%AA%8D.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tueda/PS2022SS/blob/develop/notebooks/00_%E5%8B%95%E4%BD%9C%E7%A2%BA%E8%AA%8D.ipynb?hl=ja)


## Development

<!-- textlint-disable
ja-engineering-paper/use-si-units
-->

As of 4th March 2022, Google Colaboratory and Binder use Python 3.7.12.
Hence, we adapt Python 3.7 in this course.
```bash
# Install Python 3.7 (hopefully 3.7.12) on Ubuntu 20.04.
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.7

# Set up the development environment.
poetry env use python3.7
poetry install
poetry run task prepare
```
Python 3.7 is now in the security-fix phase.
See also [PEP 537 -- Python 3.7 Release Schedule](https://www.python.org/dev/peps/pep-0537/).

Note: when adding the PPA, you may be blocked by corporate proxies.
If so, try [this](https://stackoverflow.com/a/67619514).

<!-- textlint-enable -->


## Branches

- [`main`](https://github.com/tueda/PS2022SS/tree/main): dummy text
- [`develop`](https://github.com/tueda/PS2022SS/tree/develop): general development, including temporary versions
- [`release`](https://github.com/tueda/PS2022SS/tree/release): push to deploy
- [`gh-pages`](https://github.com/tueda/PS2022SS/tree/gh-pages): deployment target
