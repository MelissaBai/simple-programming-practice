def pig_latin_word(word):
    if len(word) <= 1:
        return word
    return word[1:] + word[0] + 'ay'

def pig_latin(text):
    text_list = text.split(" ")
    result = []
    for item in text_list:
        result.append(pig_latin_word(item))
    return (' ').join(result)

print pig_latin('pig latin english')
