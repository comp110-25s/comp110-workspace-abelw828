"""Basic wordle copy"""

__author__ = "730774657"


def contains_char(word: str, letter: str) -> bool:
    """Check if a letter is present in the word"""
    idx: int = 0
    assert len(letter) == 1, f"len('{letter}') is not 1"
    while idx < len(word):
        if word[idx] == letter:
            return True
        idx = idx + 1
    return False


def emojified(word: str, secret: str) -> str:
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    result: str = ""
    assert len(word) == len(secret), "Guess must be same length as secret"
    while i < len(word):
        if word[i] == secret[i]:
            result = result + GREEN_BOX
        else:
            if contains_char(word=secret, letter=word[i]) == True:
                result = result + YELLOW_BOX
            else:
                result = result + WHITE_BOX
        i = i + 1
    return result


def input_guess(n: int) -> str:
    """Player inputing guesses"""
    guess: str = input(f"Enter a {n} character word:")
    if len(guess) != n:
        print(f"That wasn't {n} characters! Try again.")
        print(input_guess(n=n))
    else:
        return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    win: bool = False

    while turn <= 6 and win == False:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            """Win"""
            win = True
            print(f"You won in {turn}/6 turns!")
        turn = turn + 1
    if turn > 6 and win == False:
        """Loss"""
        print("X/6 - Sorry, try again tomorrow.")


if __name__ == "__main__":
    main(secret="codes")
