import os
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.0 by Adnaan")
    while True:
        x = input("Enter what you want to speak: ")
        if x=='q':
            print("say'Bye Bye Dost'")
            break
        command = f"say {x}"
        os.system(command)



