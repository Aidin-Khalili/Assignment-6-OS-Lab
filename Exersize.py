from os import system,path
WORDS = []
def read_file():
    if path.exists('My-words_bank.txt'):
        file = open('My-words_bank.txt', 'r')
        all_context = file.read()
        lines = all_context.split('\n')
        for i in range(0, len(lines) - 1, 2):
            WORDS.append({'english': lines[i], 'persian': lines[i+1]})
        file.close()
    else:
        print("We can not open the file! there is no text file that is : \'My-words_bank\'")
        input("Press Enter on your keyword to exit program")
        exit()

def save():
    file = open('My-words_bank.txt', 'w')
    for i in range(len(WORDS)):
        file.write(WORDS[i]['english'] + '\n')
        if i == len(WORDS) - 1:
            file.write(WORDS[i]['persian'])
        else:
            file.write(WORDS[i]['persian'] + '\n')
    file.close()
    print('The new version of data had been save in file successfully.')

def add_new_word():
    print('To add new word in database please ...')
    eng = input('Enter word in English : ')
    for w in WORDS:
        if w['english'] == eng:
            print("This word Already exist & we can\'t add it!")
            input("Press Enter on your keyword to continue")
            break
    else:
        per = input('Enter word in Persian : ')
        new_dict = {'english': eng, 'persian': per}
        WORDS.append(new_dict)
        print("Your word had been added successfully & we try to store in database")
        save()
        input("Press Enter on your keyword to continue.")

def translating_english_to_presian():
    print('To translate English To Persian :')
    user_text = get_input_text()
    user_sentences = user_text.split('.')
    output_text = ''
    for sen in user_sentences:
        user_words = sen.split(' ')
        output_sentence = ''
        for user_word in user_words:
            for word in WORDS:
                if user_word == word['english']:
                    output_sentence += word['persian'] + ' '
                    break
            else:
                output_sentence += user_word + ' '
        output_text += output_sentence + '. '
    print('Your text in Persian is : ' + output_text)
    input("Please press enter on keyword to continue.")

def translating_presian_to_english():
    print('To translate Persian to English :')
    user_text = get_input_text()
    user_sentences = user_text.split('.')
    output_text = ''
    for sen in user_sentences:
        user_words = sen.split(' ')
        output_sentence = ''
        for user_word in user_words:
            for word in WORDS:
                if user_word == word['persian']:
                    output_sentence += word['english'] + ' '
                    break
            else:
                output_sentence += user_word + ' '
        output_text += output_sentence + '. '
    print('So your text in English is : ' + output_text)
    input("Please press enter on keyword to continue.")

def get_input_text():
    return input('Now please enter the text that you want to be translated : ')

def menu():
    System("clean")
    print("Please choose one item : ")
    print('1. Add new word to database')
    print('2. Translate text English to Persian')
    print('3. Translate text Persian to English')
    print('4. Exit \n')
    choice = abs(int(input()))
    while not (1 <= choice <= 4):
        choice = abs(int(
            input("You had entered incorrectly. Please enter a number between 1 and 4 : ")))
    return choice
    
# Main start

read_file()
while True:
    choice = menu()
    if choice == 1:
        add_new_word()
    elif choice == 2:
        translating_english_to_presian()
    elif choice == 3:
        translating_presian_to_english()
    elif choice == 4:
        print("Thanks for using our transelator. Have good time ;)")
        break