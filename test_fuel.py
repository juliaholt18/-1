from fuel import convert, gauge
import pytest

def main():
    test_f()
    test_error()


def test_f():
    #assert convert ("4/4") == 1
    #assert gauge(1) == "F"
    assert convert ("3/4") == 75
    assert gauge(75) == "75%"
    assert convert ("1/2") == 50
    assert gauge(50) == "50%"


def test_error():
    assert convert ("1/4") == 25
    assert gauge(25) == "25%"
    assert convert ("0/4") == 0
    assert gauge(0) == "E"
    with pytest.raises(ValueError):
        assert convert("dog/cat")
    with pytest.raises(ZeroDivisionError):
        assert convert("4/0")


if __name__ == "__main__":
    main()
