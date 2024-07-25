"""
モジュール名: ldconf
概要: 設定ファイルの読み込み

関数:
- load_config: config.yamlを読み込んで辞書で返す
"""

import logging
import os
import yaml

# loggerの取得
logger = logging.getLogger(__name__)

# 定数(変更しないこと)
CONFIG_FILE = '../conf/config.yaml'

def load_config()-> tuple[bool, dict]:
    """
    概要: config.yamlを読み込んで辞書で返す
    引数: なし
    返り値:
      1. is_ok
      2. 設定ファイルをパースした辞書
    その他: 
    """
    is_ok = True
    config:dict = None
    if not os.path.isfile(CONFIG_FILE):
        logger.error(f'設定ファイルが存在しません {CONFIG_FILE=}')
        is_ok = False

    if is_ok:
        try:
            with open(CONFIG_FILE, 'r', encoding='utf8') as file:
                config = yaml.safe_load(file)
        except Exception as e:
            logger.exception(f'設定ファイルの読み込み中にエラーが発生しました。 {CONFIG_FILE=}')
            is_ok = False

    return is_ok, config
