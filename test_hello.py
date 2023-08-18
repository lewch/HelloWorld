from hello import f
import pytest

def test_mytest():
    with pytest.raises(SystemExit):
        f()