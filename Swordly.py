import random

def dict_create(language):
    with open(language, 'r', encoding='utf8') as file:
        wordlist = list(filter(lambda s: "-" not in s and "." not in s, [i.rstrip() for i in file.readlines()]))
    return wordlist


def wordhunt(word):
    length = len(word)
    attempts = 6
    output = "_" * length
    while attempts != 0 and output != word:
        print(f'Осталось попыток: {attempts}\n', output)
        input_word = input()
        while len(input_word) != length:
            print(f'Введите слово длины {length}\n')
            input_word = input()
        for i in range(length):
            if word[i] == input_word[i]:
                output = list(output)
                output[i] = word[i]
                output = "".join(output)
        attempts -= 1
    if output == word:
        return True
    else:
        return False


def wordly(wordlist):
    word = random.choice(wordlist)
    if wordhunt(word):
        print(f"Позравляем, вы угадали слово {word}!")
    else:
        print(f"К сожалению, вы не смогли угадать слово {word}")
    print("Хотите сыграть еще раз?\n", "1. Да\n", "2. Нет\n")
    onemore = input()
    while onemore not in ["1", "2"]:
        print("Введите 1 или 2")
        onemore = input()
    if onemore == "1":
        wordly(wordlist)


print("Выберите язык\n", "1. Русский\n", "2. English\n")
lang_choice = input()
while lang_choice not in ["1", "2"]:
    print("Введите 1 или 2")
    lang_choice = input()
if lang_choice == "1":
    wordlist = dict_create("russian.dict")
else:
    wordlist = dict_create("english.dict")
wordly(wordlist)