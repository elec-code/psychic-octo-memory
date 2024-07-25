"""
モジュール名: wrtxtf
概要: テキストファイル書き込みモジュール

関数:
- write_textfile: テキストファイルを出力する
"""

import logging

# loggerの取得
logger = logging.getLogger(__name__)

def overwrite_textfile(abs_filename:str, document:str) -> bool:
    """
    概要: テキストファイルを書き込む(ファイルが存在する場合は上書き、ない場合は新規)
    引数:
      abs_filename: 出力ファイル名
      document: 書き込む内容
    返り値: is_ok
    """
    is_ok = True

    logger.info('ファイル書き込み開始')

    try:
        with open(abs_filename, mode='w', encoding='utf-8') as fout:
            fout.write(document)
    except FileNotFoundError as e:
        logger.exception(f'ディレクトリがありません')
        is_ok = False
    except PermissionError as e:
        logger.exception(f'アクセス権がないためファイルの書き込みができません')
        is_ok = False
    except Exception as e:
        logger.exception(f'書き込み中にエラーが発生しました')
        is_ok = False
    
    return is_ok
