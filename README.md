# ゼロから作る Deep Learning

---

![表紙](https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch/images/deep-learning-from-scratch.png)

---

本リポジトリはオライリー・ジャパン発行書籍『[ゼロから作る Deep Learning](http://www.oreilly.co.jp/books/9784873117584/)』のサポートサイトです。

## ファイル構成

|フォルダ名 |説明                         |
|:--        |:--                          |
|ch01       |1章で使用するソースコード    |
|ch02       |2章で使用するソースコード    |
|...        |...                          |
|ch08       |8章で使用するソースコード    |
|common     |共通で使用するソースコード   |
|dataset    |データセット用のソースコード |

### ファイル内容

* `ch07/`: 畳み込みニューラルネットワーク
    - `simple_convnet.py`: CNNのサンプル。7.5節のSimpleConvNetの実装。
    - `train_convnet.py`: `simple_convnet.py`で定義したCNNを使ってMNISTの画像を学習。数時間かかる長い処理です。分類精度も計算。
    - `visualize_filter.py`: SimpleConvNetの第1層目のフィルタの可視化。7.6.1項参照。
    - `apply_filter.py`: SimpleConvNetの第1層のフィルタをかけたときの画像を表示してフィルタの効果を可視化。7.6.1節参照。
    - `gradient_check.py`: 勾配確認。5.7.3のCNN(SimpleConvNet)バージョン。本文では特にコメントなし。
    - `params.pkl`: 学習済みSimpleConvNetのピクルファイル。MNISTのデータ。

* `common/`
    - `layers.py`: 各層の定義(Rule, Sigmoid, Affine, SoftmaxWithLoss, Dropout, BatchNormalization, Convolution, Pooling)。いずれの層もfoward, backward関数が定義されている。ConvolutionとPoolingでは`util.py`で定義されているim2col, col2imを使用。
    - `util.py`: CNNの実装で必須になるim2col, col2imが定義されている。

ソースコードの解説は本書籍をご覧ください。

## 必要条件
ソースコードを実行するには、下記のソフトウェアがインストールされている必要があります。

* Python 3.x
* NumPy
* Matplotlib

※Pythonのバージョンは、3系を利用します。

## 実行方法

各章のフォルダへ移動して、Pythonコマンドを実行します。

```
$ cd ch01
$ python man.py

$ cd ../ch05
$ python train_nueralnet.py
```

## ライセンス

本リポジトリのソースコードは[MITライセンス](http://www.opensource.org/licenses/MIT)です。
商用・非商用問わず、自由にご利用ください。

## 正誤表

本書の正誤情報は以下のページで公開しています。

https://github.com/oreilly-japan/deep-learning-from-scratch/wiki/errata

本ページに掲載されていない誤植など間違いを見つけた方は、[japan＠oreilly.co.jp](<mailto:japan＠oreilly.co.jp>)までお知らせください。

