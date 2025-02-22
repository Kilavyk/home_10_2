import pytest
from src.decorators import log, write_log, my_function, check_that_agr_is, predicate_is_int


def test_log_errors(capsys):

    @log()
    def foo(x, y):
        return x + y

    with pytest.raises(TypeError):
        foo(1, "2")
    messag = capsys.readouterr()
    assert "".join(messag.out.split("-->")[-2:]) == " TypeError:  (1, '2'), {}\n"



def test_log_file_errors():

    @log(filename="log.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open("log.txt", "r", encoding="utf-8") as f:
        all_lines = f.readlines()
        messag = all_lines[-1]
    assert "".join(messag.split("-->")[-2:]) == " my_function  OK\n"



def test_my_function():
    assert my_function(2, 5) == 7



