import json
import os
import subprocess

if os.path.exists('terms.json'):
    os.remove('terms.json')

title = input("title?")
term_def_split = input("Between term and definition split characters: ")
set_split = input("Between definitions split characters: ")
instructions = input("Press enter to continue to add the copied text to the file\n")

with open('terms.json', 'w+') as file:
    set = {title: {}}

    '''
    if os.path.exists('quizlet_data.txt'):
        os.remove('quizlet_data.txt')

    with open('quizlet_data.txt', 'w+') as data:
        file.write('')
    '''

    quizlet_data_path = 'quizlet_data.txt'

    '''
    try:
            subprocess.run(['nano', quizlet_data_path], check=True)
    except FileNotFoundError:
            print("nano is not installed or not found in your PATH.")
    except subprocess.CalledProcessError as e:
            print(f"An error occurred while trying to open the file: {e}")
    '''

    with open(quizlet_data_path, 'r') as file:
            input_string = file.read()

    pairs = input_string.split(set_split)
    terms = {}
    definitions = {}

    for i, pair in enumerate(pairs, start=1):
        if term_def_split in pair:
            term, definition = pair.split(term_def_split)
            terms[str(i)] = term.strip()
            definitions[str(i)] = definition.strip()

    output = {
        "Terms": terms,
        "Definitions": definitions
    }
    
    print(set)
    set[title] = output
    with open('terms.json', "w+") as final:
        json.dump(set, final)
    print("\nrestart the program")