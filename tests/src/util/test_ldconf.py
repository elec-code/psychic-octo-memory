import pytest
from unittest.mock import patch, mock_open
from util.ldconf import load_config

@pytest.fixture
def mock_logger():
    with patch('logging.getLogger') as mock_logger:
        yield mock_logger

@patch('builtins.open', new_callable=mock_open, read_data="key: value")
@patch('os.path.isfile', return_value=True)
@patch('yaml.safe_load', return_value={'key': 'value'})
def test_load_config_success(mock_isfile, mock_safe_load, mock_open, mock_logger):
    """
    概要: 設定ファイルの読み込みが成功する場合のテスト
    条件: 設定ファイルが存在し、正常に読み込まれる
    確認: 正常に読み込まれたかどうか
    """
    status, config = load_config()
    assert status is True
    assert config == {'key': 'value'}

@patch('os.path.isfile', return_value=False)
def test_load_config_file_not_found(mock_isfile, mock_logger):
    """
    概要: 設定ファイルが存在しない場合のテスト
    条件: 設定ファイルが存在しない
    確認: エラーメッセージが表示され、ステータスがFalseであること
    """
    status, config = load_config()
    assert status is False
    assert config is None

@patch('builtins.open', new_callable=mock_open)
@patch('os.path.isfile', return_value=True)
@patch('yaml.safe_load', side_effect=Exception('読み込みエラー'))
def test_load_config_exception(mock_isfile, mock_safe_load, mock_open, mock_logger):
    """
    概要: 設定ファイルの読み込み中に例外が発生する場合のテスト
    条件: 設定ファイルの読み込み中に例外が発生する
    確認: エラーメッセージが表示され、ステータスがFalseであること
    """
    status, config = load_config()
    assert status is False
    assert config is None
