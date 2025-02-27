text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

clean_text = text.replace(",", "").replace(".", "")

words = clean_text.split()

numbers = (list(map(len,(words))))

clean_numbers = "".join(map(str, numbers))

print(clean_numbers)