"""Tests for dictionary"""

___author___ = 730774657

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert() -> None:
    assert invert({"blue": "cold", "red": "warm"}) == {"cold": "blue", "warm": "red"}
    assert invert({"": ""}) == {"": ""}
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_count() -> None:
    assert count(["red", "red"]) == {"red": 2}
    assert count(["red", "blue", "yellow"]) == {"red": 1, "blue": 1, "yellow": 1}
    assert count([]) == {}


def test_favorite_color() -> None:
    assert favorite_color({"Jane": "blue", "John": "orange", "Jack": "blue"}) == "blue"
    assert favorite_color({"Jane": "blue", "John": "orange"}) == "blue"
    assert favorite_color({}) == ""


def test_bin_len() -> None:
    assert bin_len(["how", "are", "you", "?"]) == {3: {"how", "are", "you"}, 1: {"?"}}
    assert bin_len(["i", "am", "okay"]) == {1: {"i"}, 2: {"am"}, 4: {"okay"}}
    assert bin_len([""]) == {0: {""}}
