import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess, parse_guess, get_range_for_difficulty

def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_empty_guess_is_invalid():
    ok, value, error = parse_guess("")
    assert ok is False
    assert value is None
    assert error == "Enter a guess."


def test_non_numeric_guess_is_invalid():
    ok, value, error = parse_guess("abc")
    assert ok is False
    assert value is None
    assert error == "That is not a number."


def test_easy_difficulty_range():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_normal_difficulty_range():
    assert get_range_for_difficulty("Normal") == (1, 50)


def test_hard_difficulty_range():
    assert get_range_for_difficulty("Hard") == (1, 100)