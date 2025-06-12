
import random
import readchar
import time
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

clear = lambda: os.system('cls')

def main():
    option = menu()
    name_file = get_file(option)
    text = get_text(name_file)
    (duration, letter_states) = start_text(text)
    print_results(duration, letter_states, text)

 
def menu():
    print("Select level: ")
    print("1. Easy")
    print("2. Medium")
    print("3. Difficult")
    option =  int(input())
    return option

def get_file(option):
    if option == 1:
        file = "Easy.txt"
    elif option == 2:
        file = "Medium.txt"
    elif option == 3:
        file = "Difficult.txt"
    return file

def get_text(filepath):
    file = open(filepath).read().split("\n")
    return random.choice(file)

def print_text(text, letter_states):
    last_state = False
    for i in range(len(letter_states)):
        if last_state != letter_states[i] or i == 0:
            if letter_states[i]:
                print(bcolors.OKGREEN, end="")
            else:
                print(bcolors.FAIL, end= "")
        if text[i] == " " and not letter_states[i]:
            print("—", end= "")
        else:
            print(text[i], end= "")
        last_state = letter_states[i]
    
    print(bcolors.ENDC, end= "")
    print(text[len(letter_states):])


def start_text(text):
    letter_states = []
    user_cursor = 0
    start_time = time.time()
    while user_cursor < len(text):
        clear()
        print_text(text, letter_states)
        key = readchar.readkey()
        if key == readchar.key.BACKSPACE:
            if user_cursor != 0:
                user_cursor -= 1
                letter_states.pop()
        else:
            letter_states.append(key == text[user_cursor])
            user_cursor += 1
    end_time = time.time()
    return (end_time - start_time, letter_states)

def print_results(total_time, letter_states, text):
    print(f"Total time: {round(total_time)} seconds")
    error_count = 0
    for letter in letter_states:
        if not letter:
            error_count += 1
    print(f"You have committ {error_count} errors.")
    number_words = len(text.split(" "))
    words_per_minute = number_words / (total_time / 60)
    print(f"{round(words_per_minute)} words/minute")


if __name__ == "__main__":
    main()




        

