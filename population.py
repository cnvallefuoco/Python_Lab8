#Introduction function to describe what the program is designed to do
def intro():
    print("This program that will tell you how many people are from each state. ")


def dict_count():
        #open the new file
        file = open("location.txt","r")
        #read the file
        filer = file.readline()
        #parce the data
        line = filer.split()
        #create the dictionary
        State = {}
        #establish a count for each state, add one if the state is the same
        for word in line:
            if word in State:
                State[word] += 1
            else:
                #dont add to the count if it is not the same state
                State[word] = 1
        #output to the console the count
        print("Count: " , State)


def main():
    #call all functions and remaining code
    intro()
    #endword is used to stop the program from continuing to prompt the user for input
    endword = " "
    while endword != "Done":
        #prompt the user for their home city
        userCity = input("Enter the city you are from: ")
        #prompt the user for their home state
        userstate = input("Enter the state you are from(Use Abbreviations Ex. MD for Maryland):  ")

        #open output file
        file = open("location.txt","a")
        #open output file
        fullLocation = open("fulllocation.txt","a")
        #append data to new outputfile
        fullLocation.write(userCity+","+userstate+"\n")
        #write to the first file the state, this will help us get the count
        file.write(userstate + " ")
        #output to the console the city and state, just to how the user there input's
        print(userCity + ","+ userstate)
        #endword once again helps establish if the user wants to continue the program or terminate
        endword = input("Do you wish to enter another location? if not enter Done :")
    dict_count()

#call main or the program won’t work
main()
