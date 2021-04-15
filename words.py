def wordcount():
    filename = input("What is the file name?")
    file = open(filename, 'r')
    numberofwords = 0
    for w in file:
        words=w.split()
        numberofwords=numberofwords+len(words)

    print("There are " + str(numberofwords) + " words in this file.")
wordcount()
 