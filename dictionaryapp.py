import difflib

print("Dictionary")

print("1 for searching")

print("2 for adding")

choice = int(input("Enter your choice: "))


mydict={'ape':'kind of monkey', 'apple':'fruit', 
'peach':'fruit2', 'puppy':'cute face'}


if choice==1:

    word = input("Enter word: ")

    word = word.lower()

    if word in mydict:

        print(mydict[word])

    else:

        word=difflib.get_close_matches(word, mydict.keys(),n=2)
        (word,word1)=word #unpacking of values.

        yn = input("Did you mean, '"+ word+"' (y/n): ")

        yn = yn.lower()

        if yn == 'y':

            print(mydict[word])

        elif yn == 'n':

            print('''The word is not present at that moment.Please add if possible.''')

elif choice==2:

    word = input("Enter word: ")

    meaning = input("Enter meaning: ")

    mydict[word]=meaning

    print("added", word," : ",mydict[word])

    print("updated!")

else:
    
    print("you entered a wrong choice!")
