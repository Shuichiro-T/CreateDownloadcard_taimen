import argparse
import csv
from PIL import Image, ImageDraw, ImageFont
import qrcode

#QRコードを張り付ける
def paste_qrcode(url, base_image, qr_size, qr_position_x, qr_position_y):
    #QRコードを作成
    qrcode_image = qrcode.make(url)
    qrcode_image = qrcode_image.resize((qr_size, qr_size))

    #張り付けられる画像をコピー
    copy_image = base_image.copy()

    #QRコードを張り付け
    copy_image.paste(qrcode_image, (qr_position_x, qr_position_y))

    return copy_image

#シリアルコードを張り付ける
def paste_serial(serial, base_image, serial_size, serial_position_x, serial_position_y, serial_font):

    #張り付けられるイメージ書き込み用に
    draw_image = ImageDraw.Draw(base_image)

    #フォントの指定
    font = ImageFont.truetype(font=serial_font, size=serial_size)

    #フォントを張り付け
    draw_image.text((serial_position_x, serial_position_y), serial[:3] + ' ' + serial[3:6] + ' ' + serial[6:9] + ' ' + serial[9:], fill='#000', font=font)

    return base_image


def main():

    #引数の設定
    parser = argparse.ArgumentParser(description='対面電書のCSVからシリアル番号とURLをテンプレート画像に貼るプログラムです')
    parser.add_argument('-i','--input_csv', help='対面電書からダウンロードするCSVファイルのパス', required=True)
    parser.add_argument('-o','--output_dir', help='出力するディレクトリ', required=True)
    parser.add_argument('-t','--template', help='テンプレートとなる画像のパス', required=True)
    parser.add_argument('-qs','--qr_size', help='QRコードのサイズ', type=int, required=False, default=410)
    parser.add_argument('-qx','--qr_position_x', help='QRコード貼り付ける場所（左上を０としてのX座標）', type=int, required=False, default=0)
    parser.add_argument('-qy','--qr_position_y', help='QRコード貼り付ける場所（左上を０としてのY座標）', type=int, required=False, default=0)
    parser.add_argument('-ss','--serial_size', help='シリアルコードのサイズ', type=int, required=False, default=50)
    parser.add_argument('-sx','--serial_position_x', help='シリアルコードを貼り付ける場所（左上を０としてのX座標）', type=int, required=False, default=50)
    parser.add_argument('-sy','--serial_position_y', help='シリアルコードを貼り付ける場所（左上を０としてのY座標）', type=int, required=False, default=420)
    parser.add_argument('-sf','--serial_font', help='シリアルコードのフォント（フォントファイルのパスorフォントファイル名）', required=True)

    args = parser.parse_args()

    #CSVの行数分ループ
    csv_file = open(args.input_csv, "r")
    f = csv.DictReader(csv_file)
    for row in f:
        output_image = paste_qrcode(row['secret-url'], Image.open(args.template), args.qr_size, args.qr_position_x, args.qr_position_y)
        output_image = paste_serial(row['password'], output_image, args.serial_size, args.serial_position_x, args.serial_position_y, args.serial_font)
        output_image.save(args.output_dir + row['number'].zfill(4) + '.jpg')

    print('終了')

if __name__ == "__main__":
    main()