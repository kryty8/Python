# Is this Palindrome?

# Make a function
def palindorm(teststring):
    # reverse string to condition
    if teststring == teststring[::-1]:
        return "This is palyndrome"
    return "This is not palyndrome"

#For still working program

# main program

# .isalnum() method checks whether all the characters in a
# given string are either alphabet or numeric (alphanumeric) characters.

run = True
while(run):
    # input word
    teststring = input("Write Your Palyndrome or write 'exit' to stop the program:")

    # for stop program
    if teststring == "exit":
        run = False
        break

    # compare "small" words
    teststring = teststring.lower()

    # empty string for new string
    nstring = ""

    for x in teststring:
        if x.isalnum():
            nstring +=x
            #addint single character to the word

    print("Palindrome test: ", palindorm(nstring))
