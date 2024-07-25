from unittest.mock import patch
from util.rmfile import remove_file  # 実際のモジュール名と関数名に合わせて変更してください
from unittest.mock import patch

from util.rmfile import remove_file  # 実際のモジュール名と関数名に合わせて変更してください


@patch('os.path.isfile', return_value=True)
@patch('os.remove')
def test_remove_file_success(mock_remove, mock_isfile):
    """
    概要: remove_file関数の正常動作をテスト
    条件: 削除対象のファイルが存在する
    確認: 関数がTrueを返し、ファイルが正常に削除されるか
    """
    filename = 'dummy.txt'
    with patch('pathlib.Path.is_file', return_value=True):
        with patch('pathlib.Path.resolve', return_value=filename):
            status = remove_file(filename)
            assert status is True
            mock_remove.assert_called_once_with(filename)

@patch('os.path.isfile', return_value=False)
def test_remove_file_not_exists(mock_isfile):
    """
    概要: remove_file関数でファイルが存在しない場合の動作をテスト
    条件: 削除対象のファイルが存在しない
    確認: 関数がTrueを返し、ファイル削除操作が行われないか
    """
    filename = 'dummy.txt'
    with patch('pathlib.Path.is_file', return_value=False):
        status = remove_file(filename)
        assert status is True

@patch('os.path.isfile', return_value=True)
@patch('os.remove', side_effect=PermissionError)
def test_remove_file_permission_error(mock_remove, mock_isfile):
    """
    概要: remove_file関数でファイルの削除に失敗した場合の動作をテスト
    条件: ファイルの削除権限がない
    確認: 関数がFalseを返し、適切なエラーメッセージが表示されるか
    """
    filename = 'dummy.txt'
    with patch('pathlib.Path.is_file', return_value=True):
        with patch('pathlib.Path.resolve', return_value=filename):
            status = remove_file(filename)
            assert status is False
            mock_remove.assert_called_once_with(filename)

@patch('os.path.isfile', return_value=True)
@patch('os.remove', side_effect=OSError)
def test_remove_file_os_error(mock_remove, mock_isfile):
    """
    概要: remove_file関数でOSエラーが発生した場合の動作をテスト
    条件: OSErrorが発生する
    確認: 関数がFalseを返し、適切なエラーメッセージが表示されるか
    """
    filename = 'dummy.txt'
    with patch('pathlib.Path.is_file', return_value=True):
        with patch('pathlib.Path.resolve', return_value=filename):
            status = remove_file(filename)
            assert status is False
            mock_remove.assert_called_once_with(filename)

@patch('os.path.isfile', return_value=True)
@patch('os.remove', side_effect=Exception)
def test_remove_file_unknown_error(mock_remove, mock_isfile):
    """
    概要: remove_file関数で予期しないエラーが発生した場合の動作をテスト
    条件: 予期しない例外が発生する
    確認: 関数がFalseを返し、適切なエラーメッセージが表示されるか
    """
    filename = 'dummy.txt'
    with patch('pathlib.Path.is_file', return_value=True):
        with patch('pathlib.Path.resolve', return_value=filename):
            status = remove_file(filename)
            assert status is False
            mock_remove.assert_called_once_with(filename)
