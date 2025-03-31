"""Dictionary"""

___author___ = 730774657


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary"""
    output: dict[str, str] = {}
    for key in input:
        output[input[key]] = key
    return output


def count(items: list[str]) -> dict[str, int]:
    """Counts the number of times each string in a list is present"""
    result: dict[str, int] = {}
    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
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
    for word in words:
        length: int = len(word)
        if length in result:
            result[length].add(word)
        else:
            result[length] = {word}
    return result
