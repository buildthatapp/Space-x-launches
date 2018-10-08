import pytest
import app

# testing index view
def test_index():
    assert app.index('hello') == 'hello'