#Make a dictionary of dictionaries

#Can search by name
NAMES = {}

#Can search by category
CATEGORIES = {}

def csvName():
    i = 0
    for line in open('debate_resp.csv', 'r'):
        if i == 0:
            first_line = line.split(",")
        elif i != 0:
            curr_line = line.split(",")
            newDict = {}
            count = 1
            while(count < 5):
                newDict[first_line[count]] = curr_line[count]
                count ++
            NAMES[curr_line[0]] = newDict
        i ++

def csvCat():
    i = 0
    for line in open('debate_resp.csv', 'r'):
        if i == 0:
            first_line = line.split(",")
        elif i != 0:
            curr_line = line.split(",")
            newDict = {}
            count = 0
            while(count < 4):
                newDict[first_line[count]] = curr_line[count]
                count ++
            if CATEGORIES[curr_line[4]] == None: 
                CATEGORIES[curr_line[4]] = newDict
            else:
                (first last)")
                print NAMES[name]
                

        elif choice == 2:
            try:
                cat = raw_input("Type in the Category you want 

        else:
            print "Sorry, that isn't a specified choice."
    except:
        print "Sorry, that doesn't seem to work. Try Again:\n Choose a dictionary: (1) By Name, (2) By Category."
    
    
    
