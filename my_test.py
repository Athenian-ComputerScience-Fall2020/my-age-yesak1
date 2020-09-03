import pytest
from my_code import *

global age
age = 17

def test_age_now(capsys):
    age_now(age)
    captured = capsys.readouterr()
    assert captured.out == f"I am currently {age} years old.\n\n"
    # assert age_now(17) == 17

def test_age_1(capsys):
    age_1(age)
    captured = capsys.readouterr()
    assert captured.out == f"Next year I'll be {age + 1} years old.\n\n"
    # assert age_1(17) == 18

def test_age_10(capsys):
    # Test age in 10 years
    age_10(age)
    captured = capsys.readouterr()
    assert captured.out == f"In 10 years, I'll be {age + 10}!\n\n"
    # assert age_10(17) == 27

def test_age_50(capsys):
    # My age in 50 years!
    age_50(age)
    captured = capsys.readouterr()
    assert captured.out == f"In 50 years, I'll be {age + 50}! Wow!\n\n"
    # assert age_50(17) == 67
