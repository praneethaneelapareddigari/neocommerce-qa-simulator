import pytest
@pytest.mark.parametrize('browser_name', ['chrome','firefox'])
def test_cross_browser_matrix(browser_name):
    assert browser_name in ['chrome','firefox']
