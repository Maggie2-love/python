def add_string(word):
    if len(word)<3:
        return word
    elif word.endswith("ing"):
        return word + "ly"
    else:
        return word + "ing"
print(add_string("string"))
print(add_string("add"))
print(add_string("go"))
