import sys

import pytest
from util.getarg import get_args
from util.version import VERSION, RELEASE_DATE


def mock_argv(*args):
    """ コマンドライン引数をモックするためのヘルパー関数 """
    sys.argv = list(args)

@pytest.fixture
def mock_sys_argv():
    """ コマンドライン引数をモックするためのfixture """
    original_argv = sys.argv.copy()
    yield mock_argv
    sys.argv = original_argv

def test_get_args_default(mock_sys_argv):
    """
    概要: デフォルトのコマンドライン引数での動作をテスト
    条件: コマンドライン引数を指定しない
    確認: デフォルトの引数が正しく設定されているか
    """
    mock_sys_argv('main.py')
    is_ok, args = get_args()
    assert is_ok is True
    assert args.input_filename == '../io/input/input.txt'
    assert args.output_filename == '../io/output/output.txt'

def test_get_args_with_input(mock_sys_argv):
    """
    概要: 入力ファイル名を指定した場合の動作をテスト
    条件: -i オプションで入力ファイル名を指定
    確認: 指定した入力ファイル名が正しく設定されているか
    """
    mock_sys_argv('main.py', '-i', 'input_test.txt')
    is_ok, args = get_args()
    assert is_ok is True
    assert args.input_filename == 'input_test.txt'
    assert args.output_filename == '../io/output/output.txt'

def test_get_args_with_output(mock_sys_argv):
    """
    概要: 出力ファイル名を指定した場合の動作をテスト
    条件: -o オプションで出力ファイル名を指定
    確認: 指定した出力ファイル名が正しく設定されているか
    """
    mock_sys_argv('main.py', '-o', 'output_test.txt')
    is_ok, args = get_args()
    assert is_ok is True
    assert args.input_filename == '../io/input/input.txt'
    assert args.output_filename == 'output_test.txt'

def test_get_args_with_all_options(mock_sys_argv):
    """
    概要: 全てのオプションを指定した場合の動作をテスト
    条件: -i および -o オプションで入力ファイル名と出力ファイル名を指定
    確認: 指定した入力ファイル名と出力ファイル名が正しく設定されているか
    """
    mock_sys_argv('main.py', '-i', 'input_test.txt', '-o', 'output_test.txt')
    is_ok, args = get_args()
    assert is_ok is True
    assert args.input_filename == 'input_test.txt'
    assert args.output_filename == 'output_test.txt'

def test_get_args_version(capsys, mock_sys_argv):
    """
    概要: バージョン情報を表示するオプションの動作をテスト
    条件: -v オプションを指定
    確認: バージョン情報が正しく表示されるか
    """
    mock_sys_argv('main.py', '-v')
    with pytest.raises(SystemExit):  # argparseのversionオプションは終了するので、SystemExitをキャッチ
        get_args()
    captured = capsys.readouterr()
    assert f"main.py: VERSION='{VERSION}' RELEASE_DATE='{RELEASE_DATE}'" in captured.out
