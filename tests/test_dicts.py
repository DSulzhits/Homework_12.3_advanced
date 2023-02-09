from utils import dicts


def test_key_value():
    assert dicts.get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert dicts.get_val({"vcs": "mercurial"}, "vcs", "git") == "mercurial"
    assert dicts.get_val({}, "vcs", "git") == "git"
    assert dicts.get_val({}, "vcs", "bazaar") == "bazaar"
    assert dicts.get_val({}, "") == "git"


