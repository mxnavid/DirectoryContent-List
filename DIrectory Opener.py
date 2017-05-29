import os

def opener(directory):
    stuffsInDirectory=os.listdir(directory)
    for i in stuffsInDirectory:
        print(i)


def main():
    directory = input("Please input the directory name: ")
    opener(directory)

main()


