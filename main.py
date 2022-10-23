import os
import sys
from xml.dom import WrongDocumentErr

from deep_translator import GoogleTranslator
from pygame import mixer
from termcolor import colored
import pyttsx3
from gtts import gTTS

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

    if type.startswith("listen"):
        mixer.init()
        for w in words:
            if type == "listen":
                audio = gTTS(text=w, lang=TTS_LANGUAGE, slow=False)
            elif type == "listen slow":
                audio = gTTS(text=w, lang=TTS_LANGUAGE, slow=True)

            audio.save("w.mp3")
            mixer.music.load("w.mp3")
            mixer.music.set_volume(VOLUME)
            mixer.music.play()



            input_w = input(PROMPT)
            if input_w != w:
                failed.append(w)
                print(colored("WRONG!", "red"))


                list_w = list(w)
                compare_print = ""
                for i, char in enumerate(list(input_w)):
                    try:
                        if char == list_w[i]:
                            compare_print += colored(char, "green")
                        else:
                            compare_print += colored(char, "red")
                    except:
                        pass
                print("You Wrote:")
                print(compare_print)
                
                print("Correct Word:")
                print(colored(w, "green"))

                input("Press enter to continue...")


        mixer.quit()
            
    
    if type == "write":
        for w in words:
            os.system(CLEAR)
            trans_w = translator.translate(w)
            print(trans_w)
            input_w = input(PROMPT)
            if input_w != w:
                failed.append(w)
                print(colored("WRONG!", "red"))

                

                list_w = list(w)
                compare_print = ""
                for i, char in enumerate(list(input_w)):
                    try:
                        if char == list_w[i]:
                            compare_print += colored(char, "green")
                        else:
                            compare_print += colored(char, "red")
                    except:
                        pass
                print("You Wrote:")
                print(compare_print)
                
                print("Correct Word:")
                print(colored(w, "green"))

                input("Press enter to continue...")
            
        


            

if __name__ == "__main__":
    main()
