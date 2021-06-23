text = input()
word = input()
def search(text, word):
    a=text.find(word)
    if a==-1:
        print("Word not found")
        quit()
    else:
        print("Word found")
        quit()

print(search(text, word))
