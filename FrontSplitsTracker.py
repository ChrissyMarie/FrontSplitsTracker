from datetime import datetime

def readUserDate(userID):

    #create file if it doesn't exist
    fcreate = open(userID + "Date.txt", "a")
    fcreate.close()

    #try to read the file
    startDate = datetime.now()
    fin = open(userID + "Date.txt", "r")
    line = fin.readline()

    if (len(line) > 0):
        #File has contents, so read them
        #print("Length of line is: " + str(len(line)))
        startDate = datetime.fromtimestamp(float(line))
        fin.close()

    else:
        #Create timestamp in our new file
        fin.close()
        fout = open(userID + "Date.txt", "w")
        fout.write(str(startDate.timestamp()) + "\n")
        fout.close()

    print("Timestamp in the file is: " + str(startDate) + "\n")

    return startDate

def readUserRightSplits(userID):

    #create file if it doesn't exist
    fcreate = open(userID + "RightSplits.txt", "a")
    fcreate.close()

    #try to read the file
    rightSplitsStart = 0
    fin = open(userID + "RightSplits.txt", "r")
    line = fin.readline()

    if (len(line) > 0):
        #File has contents, so read them
        rightSplitsStart = int(line)

    fin.close()

    return rightSplitsStart


def readUserLeftSplits(userID):

    #create file if it doesn't exist
    fcreate = open(userID + "LeftSplits.txt", "a")
    fcreate.close()

    #try to read the file
    leftSplitsStart = 0
    fin = open(userID + "LeftSplits.txt", "r")
    line = fin.readline()

    if (len(line) > 0):
        #File has contents, so read them
        leftSplitsStart = int(line)

    fin.close()

    return leftSplitsStart


# Ask the user for their user ID. If the the user ID does not exist, this is a
#   new user.

print("Welcome to your front splits tracker!\n\n")
userID = input("Please enter your user ID: ")


# If this is a new user, create a new file based on their chosen ID and set
#   a goal date for achievement of 180 degree splits. If this is not a new
#   user, open thier existing file and read their data, displaying goal date
#   and projected range of motion for current date.

userStartDate = readUserDate(userID)
userRightSplits = readUserRightSplits(userID)
userLeftSplits = readUserLeftSplits(userID)

newUser = False

#User enters splits angle in degrees if new account
if (userRightSplits == 0):

    #Now we know this is a new user
    newUser = True

    startRS = input("Please enter the angle of your right splits in degrees: ")
    userRightSplits = int(startRS)
    startLS = input("Please enter the angle of your left splits in degrees: ")
    userLeftSplits = int(startLS)

    #save to file

    #open the file and write right splits
    fout = open(userID + "RightSplits.txt", "w")
    fout.write(str(userRightSplits) + "\n")
    fout.close()

    #open the file and write left splits
    fout = open(userID + "LeftSplits.txt", "w")
    fout.write(str(userLeftSplits) + "\n")
    fout.close()

print("Your starting right splits is: " + str(userRightSplits))
print("Your starting left splits is: " + str(userLeftSplits))

if (newUser == False):
    # Ask for current data
    newRS = int(input("Please enter your current right splits in degrees: "))
    newLS = int(input("Please enter your current left splits in degrees: "))
    improveRS = newRS - userRightSplits
    improveLS = newLS - userLeftSplits
    print("Your right splits have improved by " + str(improveRS) + " degrees.")
    print("Your left splits have improved by " + str(improveLS) + " degrees.")
    currentDate = datetime.now()
    dateDifference = currentDate - userStartDate
    #print("dateDifference: " + str(dateDifference))
    daysSinceStart = int(dateDifference.days)
    #print("daysSinceStart: " + str(daysSinceStart))
    degreesToGoRS = 180 - newRS
    #print("degreesToGoRS: " +str(degreesToGoRS))
    degreesToGoLS = 180 - newLS

    if (improveRS > 0):
        rateRS = daysSinceStart/improveRS
        daysToRS = rateRS * degreesToGoRS
        print("At this rate of improvement, you will achieve your full right splits in " + str(int(daysToRS)) + " days.")
    else:
        print("You have not seen any improvement in you right splits. Please keep trying.")

    if (improveLS > 0):
        rateLS = daysSinceStart/improveLS
        daysToLS = rateLS * degreesToGoLS
        print("At this rate of improvement, you will achieve your full left splits in " + str(int(daysToLS)) + " days.")
    else:
        print("You have not seen any improvement in you left splits. Please keep trying.")











