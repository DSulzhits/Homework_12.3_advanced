import pytest
from utils import dicts


@pytest.fixture
def data():
    return {"vcs": "mercurial"}


@pytest.fixture
def data_1():
    return {}


def test_key_value(data):
    assert dicts.get_val(data, "vcs") == data("vcs")
    assert dicts.get_val(data, "vcs", "git") == data("vcs")


def test_key_value(data_1):
    assert dicts.get_val(data_1, "vcs", "git") == "git"
    assert dicts.get_val(data_1, "vcs", "bazaar") == "bazaar"
    assert dicts.get_val(data_1, "") == "git"
