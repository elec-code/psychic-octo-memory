import pytest
from unittest.mock import patch, mock_open
from util.rdtxtf import read_textfile

def test_read_textfile_success():
    """
    概要: read_textfile関数の正常動作をテスト
    条件: 有効なテキストファイルを読み込む
    確認: 各行の改行を除去したリストが正しく返されるか
    """
    mock_data = "line1\nline2\nline3\n"
    with patch('builtins.open', mock_open(read_data=mock_data)):
        status, lines = read_textfile('dummy.txt')
        assert status is True
        assert lines == ['line1', 'line2', 'line3']

def test_read_textfile_file_not_found():
    """
    概要: read_textfile関数でファイルが見つからない場合の動作をテスト
    条件: 存在しないファイルを読み込む
    確認: 関数がFalseを返し、空のリストが返されるか
    """
    with patch('builtins.open', side_effect=FileNotFoundError):
        status, lines = read_textfile('dummy.txt')
        assert status is False
        assert lines == []

def test_read_textfile_permission_error():
    """
    概要: read_textfile関数でファイルのアクセス権がない場合の動作をテスト
    条件: アクセス権のないファイルを読み込む
    確認: 関数がFalseを返し、空のリストが返されるか
    """
    with patch('builtins.open', side_effect=PermissionError):
        status, lines = read_textfile('dummy.txt')
        assert status is False
        assert lines == []

def test_read_textfile_unicode_decode_error():
    """
    概要: read_textfile関数でファイルのデコードに失敗した場合の動作をテスト
    条件: 不正なエンコーディングのファイルを読み込む
    確認: 関数がFalseを返し、空のリストが返されるか
    """
    with patch('builtins.open', side_effect=UnicodeDecodeError('utf-8', b"", 0, 1, 'reason')):
        status, lines = read_textfile('dummy.txt')
        assert status is False
        assert lines == []

def test_read_textfile_unknown_error():
    """
    概要: read_textfile関数で不明なエラーが発生した場合の動作をテスト
    条件: 不明なエラーが発生する
    確認: 関数がFalseを返し、空のリストが返されるか
    """
    with patch('builtins.open', side_effect=Exception):
        status, lines = read_textfile('dummy.txt')
        assert status is False
        assert lines == []
