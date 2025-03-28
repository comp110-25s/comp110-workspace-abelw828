"""Dictionary"""

___author___ = 730774657


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary"""
    output: dict[str, str] = {}
    for key in input:
        output[input[key]] = key
    return output


def count(item: list[str]) -> dict[str, int]:
    """Counts the number of times each string in a list is present"""
    result: dict[str, int] = {}
    idx: int = 0
    if idx < len(item):
        k: str = item[idx]
        if k in result:
            result[k] += 1
        else:
            result[k] = 1
        idx += 1
    return result


def favorite_color(group: dict[str, str]) -> str:
    """Counts how many times each color is given to find the favorite"""
    colors: list[str] = []
    for key in group:
        colors.append(group[key])
    fav_count: dict[str, int] = count(colors)
    fave: str = ""
    max: int = 0
    for key in fav_count:
        num: int = fav_count[key]
        if num > max:
            fave = key
            max = num
    return fave


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Sorts words into a dictonary based on lengths of words"""
    result: dict[int, set[str]] = {}
    idx: int = 0
    while idx < len(words):
        length: int = len(words[idx])
        if length in result:
            result[length].add(words[idx])
        else:
            result[length] = set(words[idx])
        idx += 1
    return result
