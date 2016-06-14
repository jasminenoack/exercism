#
# Skeleton file for the Python "Bob" exercise.
#
def hey(what):
    if what.strip() == "":
        return 'Fine. Be that way!'
    elif what == what.upper() and any(char.isalpha() for char in what):
        return "Whoa, chill out!"
    elif what.strip().endswith("?"):
        return "Sure."
    else:
        return "Whatever."