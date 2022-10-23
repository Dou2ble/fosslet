import os
import sys

from deep_translator import GoogleTranslator
from pygame import mixer
from termcolor import colored

import utils
from config import *
from globals import *

translator = GoogleTranslator('auto', DEFENITION_LANGUAGE)

# initiate q_lists list
q_lists = []
for i, f in enumerate(os.listdir("lists")):
    q_lists.append(f)
    

def main():
    os.system(CLEAR)
    print("Select a quiz to take:")
    utils.pprint(q_lists)

    quiz = q_lists[int(input(PROMPT))]

    with open("lists/" + quiz) as f:
        words = f.read().splitlines()

    os.system(CLEAR)
    print("Which study type do you want to use?")
    utils.pprint(STUDY_TYPES)
    type = STUDY_TYPES[int(input(PROMPT))]
    
    running = True
    while running:
        # start the quiz
        take_quiz(type, words)

        # ask the user if they want to retake the words they failed
        if len(failed) > 0:
            os.system(CLEAR)
            print(f"You failed these {str(len(failed))} words:")
            for w in failed:
                print(colored(w, "red"))


            print("Do you want to retake the quiz?")
            utils.pprint(YES_NO)
            if YES_NO[int(input(PROMPT))] == "yes":
                words = failed
            else:
                running = False
            
        else:
            running = False
        
    sys.exit()
    
    
    

def take_quiz(type: str, words: list):
    os.system(CLEAR)

    global failed
    failed = []

    if type == "listen":
        for w in words:
            print(w)
    
    if type == "write":
        for w in words:
            os.system(CLEAR)
            trans_w = translator.translate(w)
            print(trans_w)
            if input(PROMPT) != w:
                failed.append(w)
                print(colored("WRONG!", "red"))
                input("Press enter to continue...")
            
        


            

if __name__ == "__main__":
    main()
