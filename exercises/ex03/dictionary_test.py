"""Tests for dictionary"""

___author___ = 730774657

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert1() -> None:
    assert invert({"blue": "cold", "red": "warm"}) == {"cold": "blue", "warm": "red"}


def test_invert2() -> None:
    assert invert({"": ""}) == {"": ""}


def test_invert3() -> None:
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_count1() -> None:
    assert count(["red", "red"]) == {"red": 2}


def test_count2() -> None:
    assert count(["red", "blue", "yellow"]) == {"red": 1, "blue": 1, "yellow": 1}


def test_count3() -> None:
    assert count([]) == {}


def test_favorite_color1() -> None:
    assert favorite_color({"Jane": "blue", "John": "orange", "Jack": "blue"}) == "blue"


def test_favorite_color2() -> None:
    assert favorite_color({"Jane": "blue", "John": "orange"}) == "blue"


def test_favorite_color3() -> None:
    assert favorite_color({}) == ""


def test_bin_len1() -> None:
    assert bin_len(["how", "are", "you", "?"]) == {3: {"how", "are", "you"}, 1: {"?"}}


def test_bin_len2() -> None:
    assert bin_len(["i", "am", "okay"]) == {1: {"i"}, 2: {"am"}, 4: {"okay"}}


def test_bin_len3() -> None:
    assert bin_len([""]) == {0: {""}}
