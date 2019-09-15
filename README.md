# 機能
[対面電書](https://taimen.jp)で作成されるCSVから一括でダウンロードカードを作成する。
プログラムを実行するとテンプレート画像にシリアルコードと秘密のURLのQRが張り付けられ、指定した出力ディレクトリにダウンロードカードが出力される

# 必要なもの
 * python3
 * pip

# インストール方法

```shell
$ pip install -r requirements.txt
```

# 実行例

```shell
$ python CreateDownloadcardTaimendensho.py -i ./taimen_serial.csv -o out/ -t temp.jpg -sf DejaVuSansMono.ttf
```

# パラメータ詳細

| パラメータ名 | 短縮パラメータ | 必須 | 意味 | 例 |
|:-----------|:-----------|:-----------|:-----------|:-----------|
|--input_csv |-i |必須 |対面電書からダウンロードしたCSVファイルのパス |./taimen_serial.csv |
|--output_dir |-o |必須 |出力するディレクトリ 最後に「/」を入れること| ./out/ |
|--template |-t |必須 |テンプレートとなる画像のパス |temp.jpg |
|--qr_size |-qs |任意 |QRコードのサイズ | 50 |
|--qr_position_x |-qx |任意 |QRコード貼り付ける場所のX座標（左上が0） |50 |
|--qr_position_y |-qy |任意 |QRコード貼り付ける場所のY座標（左上が0） | 50|
|--serial_size |-ss |任意 |シリアルコードのサイズ |50 |
|--serial_position_x |-sx |任意 |シリアルコードを貼り付ける場所のX座標（左上が0） |50 |
|--serial_position_y |-sy |任意 |シリアルコードを貼り付ける場所のY座標（左上が0） |50 |
|--serial_font |-sf |必須 |シリアルコードのフォント　フォントファイルのファイル名を指定する | DejaVuSansMono.ttf |
 
