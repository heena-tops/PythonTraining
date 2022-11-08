val = input("Enter a character : ")

if(val.isalpha()):
    if(val=='a' or val=='e' or val=='i' or val=='o' or val=='u'
        or val=='A' or val=='E' or val=='I' or val=='O' or val=='U'):
        print("Vowel")

    else:
        print("Consonant")

else:
    print("Invalid input !!!")