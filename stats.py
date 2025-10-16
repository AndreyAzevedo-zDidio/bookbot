# Python
def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    characteres = text.lower()
    count = {}
    result =[]
    for character in characteres:
        count[character] = count.get(character, 0) +1
    for letter, qtd in count.items():
        if letter.isalpha():
            result.append({"char": letter, "num": qtd})
    result.sort(reverse=True, key=sort_on)
    return result
def sort_on(item):
    return item["num"]

