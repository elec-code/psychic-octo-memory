"""
モジュール名: mnglog
概要: ログファイルのセットアップを行う

関数:
- setup_logger: 下記2つを実行する
- _rotate_logs: error.logを三世代までバックアップする
- _setup_logger: errlog.yamlを読み込んで各モジュールのloggerを設定する
"""

import logging.config
import os
import shutil
import sys
import yaml
from pathlib import Path

# 定数(基本的に変更しない)
LOG_DIR = r'..\io\log'         # errlog.yamlの内容と一致させる必要あり
LOG_BASENAME = r'error.log'  # 同上
LOG_CONFIG_FILE = r'..\conf\errlog.yaml'
MAX_GENERATIONS = 3

def setup_logger()-> bool:
    """
    概要: バックアップ作成後、errlog.yamlを読み込んで各モジュールのloggerを設定する
    引数: なし
    返り値: is_ok
    その他: 
    """

    is_ok = _rotate_logs() # logのローテーションバックアップ

    if is_ok:
        is_ok = _setup_logger_sub() # errlog.yamlを読み込んで各モジュールのloggerを設定する

    return is_ok

# 以下プライベート関数

def _rotate_logs(generations=MAX_GENERATIONS)-> bool:
    """
    概要: 下記の要領でerror.logの世代バックアップをとる(generations=3の場合)
         error.log.3 => 削除      , error.log.2 => error.log.3
         error.log.1 => error.log.2, error.log => error.log.1
    引数:
      - generations(int:=MAX_GENERATIONS): 世代
    返り値: is_ok
    外部参照: LOG_DIR, LOG_BASENAME
    その他: error.logは削除しない
    """
    is_ok = True
    base_log_path = str(Path(LOG_DIR).joinpath(LOG_BASENAME))

    # ローテーション(error.log.n のnを繰り上げる)
    for i in range(generations, 0, -1):
        old_log = f"{base_log_path}.{i}"
        new_log = f"{base_log_path}.{i+1}" if i < generations else None

        if os.path.isfile(old_log):
            try:
                if new_log:
                    shutil.move(old_log, new_log)
                else:
                    os.remove(old_log)
            except Exception as e:
                is_ok = False
                print(f'{old_log} のローテーションに失敗しました: {e}', file=sys.stderr)
                break

    # error.log を error.log.1 で保存
    if is_ok:
        if os.path.isfile(base_log_path):
            try:
                shutil.move(base_log_path, f"{base_log_path}.1")
            except Exception as e:
                is_ok = False
                print(f'error.logのローテーションに失敗しました: {e}', file=sys.stderr)
    
    return is_ok

def _setup_logger_sub()-> bool:
    """
    概要: errinfo.yamlを読み込んで各モジュールのloggerを設定する
    引数: なし
    返り値: is_ok
    その他: yamlモジュールが必要
    """
    is_ok = True
    try:
        with open(LOG_CONFIG_FILE, 'r', encoding='utf8') as file:
            config = yaml.safe_load(file)
        logging.config.dictConfig(config)   # 各モジュールのログ設定
    except Exception as e:
        print(f'errinfo.yamlの読み込みに失敗しました: {e}', file=sys.stderr)
        is_ok = False

    return is_ok

