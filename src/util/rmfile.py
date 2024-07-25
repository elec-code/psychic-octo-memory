"""
モジュール名: rmfile
概要: 同名のファイルがあったら削除する

関数:
- remove_file: ファイルを削除する
"""

import logging
import os
import pathlib

# loggerの取得
logger = logging.getLogger(__name__)

def remove_file(filename:str) ->bool:
    """
    概要: ファイルを削除する
    引数: filename: 削除するファイル名
    返り値: status
    """
    is_ok = True

    file_exsits = False
    logger.info('古い出力ファイルがあれば削除します')

    # ファイルが存在するか確認
    if pathlib.Path(filename).is_file():
        file_exsits = True
        tgt_file = str(pathlib.Path(filename).resolve()) # ..を含まないフルパスに変換
    else:
        logger.info('古い出力ファイルはありませんでした')
    
    # あれば削除する
    if file_exsits:
        try:
            os.remove(tgt_file)
        except (PermissionError, OSError) as e:
            logger.exception(f'古い出力ファイルの削除に失敗しました')
            is_ok = False
        except Exception as e:
            logger.exception(f'予期しないエラーで古い出力ファイルの削除に失敗しました')
            is_ok = False
        else:
            logger.info(f'古い出力ファイルを削除しました{tgt_file=}')

    return is_ok
