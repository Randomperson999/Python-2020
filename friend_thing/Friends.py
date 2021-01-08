class Bestie:
    numMessages = 0
    def chat(input1):
        Bestie.numMessages = Bestie.numMessages+1
        if Bestie.numMessages > 3:
            print("I'm T I R E D")
            return
        input1 = str.lower(input1)
        if "ride" in input1:
            print("I don't have my license...")
        elif "call" in input1:
            print("ok")
        else:
            print("REEEEEEEEEEEEEEEEEEEEEEEEE")