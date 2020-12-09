#Caleb Keller
#9/21/2020
#Mad Libs
#Uses the Fitness Gram Pacer Test, and was found by DEVON who posted the text onto the internet.
word = input("Adjective: ")
noun1 = input("Noun: ")
num1 = int(input("Number: "))
num2 = int(input("Number: "))
noun2 = input("Noun: ")
verb1 = input("Verb: ")
sound1 = input("Sound: ")
noun3 = input ("Noun: ")
sound2 = input("Sound: ")
noun4 = input("Noun: ")
print(str.format("""The FitnessGram™ Pacer Test is a multi-{1} capacity test \nthat progressively gets more {0} as it continues.\n
The {2} meter pacer test will begin in {3} seconds.\n
{4} up at the start.
The {5}ing speed starts slowly, but gets faster each minute after you hear this \nsignal: *{6}*.\n
A single {7} should be completed each time you hear this sound: *{8}*.\n
Remember to {5} in a straight line, and {5} as long as possible.\n
The second time you fail to complete a {7} before the sound, your test is over.\n
The test will begin on the word {9}.\n
On your mark, get ready, {6}""",word,noun1,num1,num2,noun2,verb1,sound1,noun3,sound2,noun4))

