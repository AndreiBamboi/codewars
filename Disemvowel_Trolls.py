def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    upper_vowels = [x.upper() for x in [i for i in vowels]]
    full_list= vowels + upper_vowels
    string_nou = ''.join([l for l in string if l not in full_list])
    print(string_nou)
    print(upper_vowels)

disemvowel("This website is for losers LOL!")