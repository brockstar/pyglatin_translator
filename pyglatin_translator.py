pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    #print (original)
    first = word[0]
    if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
        print ("vowel")
    else:
        new_word = (word[1:]+ first + pyg)
        print (new_word)
else:
    print ('empty')



