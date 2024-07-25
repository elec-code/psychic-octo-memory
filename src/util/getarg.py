"""
モジュール名: getarg
概要: コマンドライン引数を解釈する
関数:
- get_args: コマンドライン引数を解析して返す
エラー: エラー番号の項およびerrinfo.yamlに記載
"""

import argparse
import sys

from util.version import VERSION, RELEASE_DATE


def get_args() -> tuple[bool, argparse.Namespace]:
    """
    概要: コマンドライン引数を解析して返す
    引数: なし
    返り値:
      1. isOk
      2. args: コマンドライン引数
    その他: error.logは削除しない
    参考資料:
    https://docs.python.org/ja/3/library/argparse.html#quick-links-for-add-argument
    """

    is_ok = True
    args = None
    NOTE = '詳細は python main.py -h で表示されるヘルプを参考にしてください'
    try:
        parser = argparse.ArgumentParser(description=NOTE)

        parser.add_argument('-i',
                            required=False,
                            dest='input_filename',
                            default='../io/input/input.txt',
                            help='入力ファイル名 (既定値=”%(default)s”)',
                            )

        parser.add_argument('-o',
                            dest='output_filename',
                            required=False,
                            default='../io/output/output.txt',
                            help='出力ファイル名 (”既定値=%(default)s”)',
                            )

        parser.add_argument('-v', '--version', action='version',
                            version='%(prog)s' + f': {VERSION=} {RELEASE_DATE=}')

        args = parser.parse_args()

    except Exception as e:
        print(e, file=sys.stderr)  # この時点ではlogger設定していない
        is_ok = False

    return is_ok, args
