def dict_create(language):
    with open(language, 'r', encoding='utf8') as file:
        wordlist = list(filter(lambda s: "-" not in s and "." not in s, [i.rstrip() for i in file.readlines()]))
    return wordlist


def helper(mask, wordlist):
    wordlist = list(filter(lambda x: len(x) == len(mask), wordlist))
    for i in wordlist:
        check = True
        for j in range(len(i)):
            if i[j] != mask[j] and mask[j] != "_":
                check = False
        if check:
            print(i)


print("Выберите язык\n", "1. Русский\n", "2. English\n")
lang_choice = input()
while lang_choice not in ["1", "2"]:
    print("Введите 1 или 2")
    lang_choice = input()
if lang_choice == "1":
    wordlist = dict_create("russian.dict")
else:
    wordlist = dict_create("english.dict")
mask = input()
helper(mask, wordlist)