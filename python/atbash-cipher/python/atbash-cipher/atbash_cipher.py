from string import ascii_lowercase
import textwrap


def change_letter(letter):
    alpha = ascii_lowercase
    return alpha[~ alpha.find(letter.lower())]


def decode(string):
    result = ""

    for char in string:
        if char.isalpha():
            result += change_letter(char)
        elif char.isdigit():
            result += char

    return result


def encode(string):
    string = decode(string)
    return " ".join(textwrap.wrap(string, 5))