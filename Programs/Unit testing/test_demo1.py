import pytest
from demo1 import get_weather,add, divide
def test_get_weather():
    assert get_weather(-5) == "Freezing"
    assert get_weather(0) == "Cold"
    assert get_weather(15) == "Cold"
    assert get_weather(20) == "Warm"
    assert get_weather(25) == "Warm"
    assert get_weather(30) == "Hot"
    assert get_weather(35) == "Hot"
    
    
def test_add():
    assert add(2, 3) == 5
    assert add(0, 5) == 5,"0+5 should be 5"
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -5) == -10
    assert add(100, 200) == 300
    
def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(-6, 2) == -3
    assert divide(0, 1) == 0
    with pytest.raises(ValueError,match="Cannot divide by zero"):
        divide(5, 0)
    with pytest.raises(ValueError):
        divide(0, 0)