import os
if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1 created by Aditya")
    while True:
        x=input("Enter what you want me to speak :")
        command=f"say {x}"
        if x=='q':
            os.system("say 'bye bye'")
            break
        os.system(command)
