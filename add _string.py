def add_string(word):
    if len(word)>3:
        return word + "ing"
    elif word.endswith(ing):
        return word + "ly"
    else len(word)<3:
        return word
print(dd_string("string"))
print(dd_string("add"))
print(dd_string("go"))
