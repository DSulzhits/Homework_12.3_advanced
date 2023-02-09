import pytest
from utils import dicts


@pytest.fixture
def data():
    return {"vcs": "mercurial"}, {}


def test_key_value(data):
    test_data_1, test_data_2 = data
    assert dicts.get_val(test_data_1, "vcs") == "mercurial"
    assert dicts.get_val(test_data_1, "vcs", "git") == "mercurial"
    assert dicts.get_val(test_data_1, "", "git") == "git"
    assert dicts.get_val(test_data_2, "vcs", "git") == "git"
    assert dicts.get_val(test_data_2, "vcs", "bazaar") == "bazaar"
    assert dicts.get_val(test_data_2, "") == "git"
