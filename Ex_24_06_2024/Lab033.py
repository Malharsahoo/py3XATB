# filter the vowels from list
'''letters=["a","b","d","e","i","j","o"]
def vowel(let):
    vowels=["a","e","i","o","u"]
    return let  in vowels
vowel_letters_is=filter(vowel,letters)
print(list(vowel_letters_is))'''
#o/p=['a', 'e', 'i', 'o']


# filter the consonant from the list
my_letters=["a","c","e","g","i","h","m","o","p","u","b","c"]
def consonant(l):
    vowels_list=["a","e","i","o","u"]
    return l not in vowels_list
consonant_is=filter(consonant,my_letters)
print(list(consonant_is))
#o/p=['c', 'g', 'h', 'm', 'p', 'b', 'c']