"""
モジュール名: main
概要: メインモジュール(スクリプトの最上流)

関数:
- main: メイン関数

開発環境: Python(ver.3.12.0)
注意点: モジュール名を変更した場合はlaunch.jsonの"configurations"->"program"も変更すること
"""

import logging
import os
import sys

from util.mnglog import setup_logger # ログのローテートとレベル設定
from util.getarg import get_args # コマンドライン引数の解釈
from util.rmfile import remove_file # 古い出力ファイルの削除
from util.rdtxtf import read_textfile # 入力ファイルの読み込み
from util.ldconf import load_config # 設定ファイルの読み込み
from util.wrtxtf import overwrite_textfile # テキストファイルの書き込み

# グローバル変数(公開)
config = None

def main():
    """
    概要: メイン関数
    引数: なし
    返り値: なし
    その他: 
    """
    global config
    is_ok = True

    # 作業ディレクトリをsrcに設定
    current_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(current_dir)

    # argparseでコマンドライン引数を取得する
    is_ok, args = get_args()
    if is_ok:
        input_filename = args.input_filename
        output_filename = args.output_filename

    # ログファイルのローテーション保存とlogger一括設定
    if is_ok:
        is_ok = setup_logger() 
        logger = logging.getLogger(__name__)

    # ここまででStatusがOKでなければ終了する(最後にloggerを使うため)
    if not is_ok :
        print(is_ok, file=sys.stderr)
        return

    # アプリケーション固有の設定をする(ここ以降はloggerに出力)
    if is_ok:
        logger.info('ログ記録を開始しました')
        is_ok, config = load_config()

    # 出力ファイルと同名のファイルがあれば取り違え防止のため削除する
    if is_ok:
        is_ok = remove_file(output_filename)

    # 入力ファイルを読み込む
    if is_ok:
        is_ok, lines = read_textfile(input_filename)

    # 書き込む
    if is_ok:
        document = '\n'.join(lines) + '\n'
        is_ok = overwrite_textfile(output_filename, document)

    if is_ok:
        logger.info("正常に終了しました。")
    else:
        logger.info("エラーが発生しました。詳細はログを確認してください。")

    return

if __name__ == "__main__":
    main()
