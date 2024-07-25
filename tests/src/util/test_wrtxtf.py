from unittest.mock import patch, mock_open
from util.wrtxtf import overwrite_textfile
from unittest.mock import patch, mock_open

from util.wrtxtf import overwrite_textfile


def test_overwrite_textfile_success():
    """
    概要: overwrite_textfile関数の正常動作をテスト
    条件: 有効なファイル名と内容を提供する
    確認: ファイルが正常に書き込まれるか
    """
    filename = 'dummy.txt'
    document = 'test content'
    with patch('builtins.open', mock_open()) as mocked_file:
        status = overwrite_textfile(filename, document)
        assert status is True
        mocked_file.assert_called_once_with(filename, mode='w', encoding='utf-8')
        mocked_file().write.assert_called_once_with(document)

def test_overwrite_textfile_file_not_found():
    """
    概要: overwrite_textfile関数でファイルが見つからない場合の動作をテスト
    条件: 存在しないディレクトリにファイルを書き込む
    確認: 関数がFalseを返し、適切なエラーメッセージが表示されるか
    """
    filename = 'non_existent_dir/dummy.txt'
    document = 'test content'
    with patch('builtins.open', side_effect=FileNotFoundError):
        status = overwrite_textfile(filename, document)
        assert status is False

def test_overwrite_textfile_permission_error():
    """
    概要: overwrite_textfile関数でファイルの書き込みに失敗した場合の動作をテスト
    条件: ファイルの書き込み権限がない
    確認: 関数がFalseを返し、適切なエラーメッセージが表示されるか
    """
    filename = 'dummy.txt'
    document = 'test content'
    with patch('builtins.open', side_effect=PermissionError):
        status = overwrite_textfile(filename, document)
        assert status is False

def test_overwrite_textfile_unknown_error():
    """
    概要: overwrite_textfile関数で予期しないエラーが発生した場合の動作をテスト
    条件: 予期しない例外が発生する
    確認: 関数がFalseを返し、適切なエラーメッセージが表示されるか
    """
    filename = 'dummy.txt'
    document = 'test content'
    with patch('builtins.open', side_effect=Exception):
        status = overwrite_textfile(filename, document)
        assert status is False
