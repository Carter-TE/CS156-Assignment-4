import os


def positive_review(filename):
    for textfiles in os.listdir(filename):
        with open(os.path.join(filename, textfiles), 'r') as f:
            text = f.read()

            if text.__contains__("10/10"):
                print(textfiles)
                print(text)



def negative_review(filename):
    for textfiles in os.listdir(filename):
        with open(os.path.join(filename, textfiles), 'r') as f:
            text = f.read()
            if text.__contains__():
                print(textfiles)
                print(text)


positive_review('C:\\Users\\Dusti\\Desktop\\pos')





