sentence = "The quick brown fox jumps over the lazy dog"

for c in sentence:
    print(c)

word = ""
for c in sentence:
    if c == ' ':
        print(word)
        word = ""
    else:
        word += c
if word and word != "":
    print(word)

token = "f"

for i in range(len(sentence) - 1):
    c = sentence[i]
    if c != token:
        continue
    start = i
    while sentence[i] != ' ':
        i += 1
    print(sentence[start:i])
