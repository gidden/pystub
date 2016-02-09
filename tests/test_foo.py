from nose.tools import assert_equal

from pystub import foo

def test_bar():
    assert_equal(foo.bar(), 42)
