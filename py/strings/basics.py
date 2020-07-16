sentence = "The quick brown fox jumps over the lazy dog"

def print_chars():
    # printing each character
    for c in sentence:
        print(c)

def print_words():
    # writing the characters into a variable unless it is a space
    words = []
    word = ""
    for c in sentence:
        if c == ' ':
            # print current word, reset it afterwards
            print(word)
            words.append(word)
            word = ""
        else:
            word += c
    # write the last word, if it is not empty
    if word and word != "":
        print(word)
        words.append(word)

def search_token():
    # search for word which contains a token
    token = "f"
    for word in sentence.split():
        if token in word:
            print(word)