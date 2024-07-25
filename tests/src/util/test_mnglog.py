from unittest.mock import patch, mock_open

import pytest
from util.mnglog import LOG_DIR, LOG_BASENAME


@pytest.fixture
def mock_logger():
    with patch('logging.getLogger') as mock_logger:
        yield mock_logger

def mock_isfile_side_effect(path):
    """ モック用のisfile関数 """
    print(f"Checking if file exists: {path}")
    if path in [
        f"{LOG_DIR}/{LOG_BASENAME}.3",
        f"{LOG_DIR}/{LOG_BASENAME}.2",
        f"{LOG_DIR}/{LOG_BASENAME}.1",
        f"{LOG_DIR}/{LOG_BASENAME}"
    ]:
        return True
    return False

@patch('os.path.isfile', side_effect=mock_isfile_side_effect)
@patch('shutil.move', side_effect=Exception('Move error'))
@patch('os.remove')
def test_rotate_logs_move_error(mock_remove, mock_move, mock_isfile):
    """
    概要: _rotate_logs関数でshutil.moveが失敗した場合の動作をテスト
    条件: shutil.moveが例外を投げる
    確認: 関数がFalseを返し、適切なエラーメッセージが表示されるか
    """
    # 機能検査で実施する

@patch('os.path.isfile', return_value=True)
@patch('shutil.move')
@patch('os.remove')
def test_rotate_logs_success(mock_remove, mock_move, mock_isfile):
    """
    概要: _rotate_logs関数の正常動作をテスト
    条件: error.logおよびバックアップファイルが存在する
    確認: バックアップファイルが正しくローテーションされるか
    """
    # 機能検査で実施する

@patch('os.path.isfile', return_value=False)
def test_rotate_logs_no_files(mock_isfile):
    """
    概要: _rotate_logs関数の動作をテスト
    条件: error.logおよびバックアップファイルが存在しない
    確認: 関数がTrueを返し、ファイル操作が行われないか
    """
    # 機能検査で実施する

@patch('builtins.open', new_callable=mock_open, read_data="key: value")
@patch('yaml.safe_load', return_value={})
@patch('logging.config.dictConfig')
def test_setup_logger_sub_success(mock_dictConfig, mock_safe_load, mock_open):
    """
    概要: _setup_logger_sub関数の正常動作をテスト
    条件: errlog.yamlが正しく読み込まれる
    確認: ロガーが正しく設定されるか
    """
    # 機能検査で実施する

@patch('builtins.open', new_callable=mock_open)
@patch('yaml.safe_load', side_effect=Exception('YAML error'))
@patch('logging.config.dictConfig')
def test_setup_logger_sub_yaml_error(mock_dictConfig, mock_safe_load, mock_open):
    """
    概要: _setup_logger_sub関数でyaml.safe_loadが失敗した場合の動作をテスト
    条件: yaml.safe_loadが例外を投げる
    確認: 関数がFalseを返し、適切なエラーメッセージが表示されるか
    """
    # 機能検査で実施する

@patch('src.util.mnglog._rotate_logs', return_value=True)
@patch('src.util.mnglog._setup_logger_sub', return_value=True)
def test_setup_logger_success(mock_setup_logger_sub, mock_rotate_logs):
    """
    概要: setup_logger関数の正常動作をテスト
    条件: _rotate_logsおよび_setup_logger_subが正常に動作する
    確認: 関数がTrueを返すか
    """
    # 機能検査で実施する

@patch('src.util.mnglog._rotate_logs', return_value=False)
@patch('src.util.mnglog._setup_logger_sub')
def test_setup_logger_rotate_logs_fail(mock_setup_logger_sub, mock_rotate_logs):
    """
    概要: setup_logger関数で_rotate_logsが失敗した場合の動作をテスト
    条件: _rotate_logsがFalseを返す
    確認: 関数がFalseを返し、_setup_logger_subが呼ばれないか
    """
    # 機能検査で実施する
