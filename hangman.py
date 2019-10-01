import random

print('--Hangman!!--')
word_list = [
'Awkward',
'Bagpipes',
'Banjo',
'Bungler',
'Croquet',
'Crypt',
'Dwarves',
'Fervid',
'Fishhook',
'Fjord',
'Gazebo',
'Gypsy',
'Haiku',
'Haphazard',
'Hyphen',
'Ivory',
'Jazzy',
'Jiffy',
'Jinx',
'Jukebox',
'Kayak',
'Kiosk',
'Klutz',
'Memento',
'Mystify',
'Numbskull',
'Ostracize',
'Oxygen',
'Pajama',
'Phlegm',
'Pixel',
'Polka',
'Quad',
'Quip',
'Rhythmic',
'Rogue',
'Sphinx',
'Squawk',
'Swivel',
'Toady',
'Twelfth',
'Unzip',
'Waxy',
'Wildebeest',
'Yacht',
'Zealous',
'Zigzag',
'Zippy',
'Zombie']

comp_word = random.choice(word_list)
length_of_comp_word = len(comp_word)
number_guesses = 0
correct_guesses = ['__'] * length_of_comp_word
print(correct_guesses)
correct_word = ''.join(correct_guesses)
wrong_guesses = []
while number_guesses < 10:
    user_guess = input('Enter a letter: ')
    try:
        letter_index = comp_word.index(user_guess)
        correct_word = ''.join(correct_guesses)
        print('You got one correct!')
        for i, letter in enumerate(comp_word):
            if letter == user_guess:
                correct_guesses[i] = user_guess
        print(correct_guesses)
        print(wrong_guesses)

    except:
        print('WRONGO!')
        wrong_guesses.append(user_guess)
        print(correct_guesses)
        print(wrong_guesses)
        number_guesses += 1

    if correct_word == comp_word:
        print('You win....lucky you.')
        break
    elif number_guesses == 10:
        print('LOSER! The correct word was', comp_word,'!!!')
