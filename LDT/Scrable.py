# en_dict = {['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']: 1,
#            ['D', 'G']: 2,
#            ['B', 'C', 'M', 'P']: 3,
#            ['F', 'H', 'V', 'W', 'Y']: 4,
#            ['K']: 5,
#            ['J', 'X']: 8,
#            ['Q', 'Z']: 10}
import re


en_dict = {'AEIOULNSTR': 1,
           'DG': 2,
           'BCMP': 3,
           'FHVWY': 4,
           'K': 5,
           'JX': 8,
           'QZ': 10}


ru_dict = {'АВЕИНОРСТ' : 1,
      	'ДКЛМПУ' : 2,
      	'БГЁЬЯ' : 3,
      	'ЙЫ' : 4,
      	'ЖЗХЦЧ' : 5,
      	'ШЭЮ': 8 ,
      	'ФЩЪ' :10}

def is_cyrillic(word):
    return bool(re.search('[а-яА-Я]', word))




def scrable(word):
    if not is_cyrillic(word):
        word = word.upper()
        count = 0
        for letter in word:
            for item in en_dict:
                if letter in item:
                    count += en_dict[item]
                    break
    else:
        word = word.upper()
        count = 0
        for letter in word:
            for item in ru_dict:
                if letter in item:
                    count += ru_dict[item]
                    break
    print(count)

scrable("Нвнвнрророры")