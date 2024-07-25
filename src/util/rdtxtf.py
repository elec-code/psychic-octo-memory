"""
モジュール名: rdtxtf
概要: テキストファイル読み込みモジュール

関数:
- read_textfile: UTF8テキストファイルを読み込んで各行の改行を除去したリストで返す
"""

import logging

# loggerの取得
logger = logging.getLogger(__name__)

def read_textfile(filename:str) ->tuple[bool, list[str]]:
    """
    概要: 入力ファイルを読み込んで各行の改行を除去したリストで返す
    引数: filename: 入力ファイル名
    返り値: 
      1. status
      2. 読み込んだ内容。改行を除去した文字列のリスト
    """
    is_ok = True
    lines = []
    logger.info('入力ファイル読み込み開始')

    try:
        with open(filename, mode='r', encoding='utf-8') as fin:
            lines = [line.rstrip('\n') for line in fin]
    except FileNotFoundError as e:
        logger.exception(f'入力ファイルが見つかりません{filename=}')
        is_ok = False
    except PermissionError as e:
        logger.exception(f'入力ファイルのアクセス権がないためファイルが開けません{filename=}')
        is_ok = False
    except UnicodeDecodeError as e:
        logger.exception(f'入力ファイルのデコードに失敗しました{filename=}')
        is_ok = False
    except Exception as e: # 不明なエラー
        logger.exception(f'不明なエラーにより入力ファイルの読み込みに失敗しました{filename=}')
        is_ok = False
    
    return is_ok, lines
