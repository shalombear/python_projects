"""A module of useful tools

functions
    ordinal -- form an ordinal number
    
    capitalizer -- render the first letter in the string uppercase and the remainder lowercase

    quote_stripper -- check if string begins and ends with single or double quotes
                  strip them
                        parameters:
                            string (str)
                        returns:
                            newstring (str)

    camelcaser -- turn a collection of words into one word in CamelCase format
                        parameters:
                            string (str)
                            delimiter (str) [default: one space ' ']
                        returns:
                            word (str)

    string2boolean_parser -- convert strings 'True' or 'T' and 'False' or 'F' into boolean values
                             case-insensitive
                             all other values raise ValueError
                                parameters:
                                    string (str)
                                returns:
                                    boolean (bool)
                                    
    dict_maker -- turn a list into a dictionary with keys (1,2,3...)
                        parameters:
                            lister (any iterable object)
                        returns:
                            mydict (dict)
            
    table2class_parser -- read a delimited table from a file
                          create class based on table
                          transmogrify each line into an object in the class
                          return the class and its objects
                                parameters:
                                    filename (str)
                                    classname (str)
                                    delimiter (str) [default: ',']
                                returns:
                                    classname (class)
                                    classlist (list)
"""

import acceptors as acc

def ordinal(cardinal):
    """
    turn a cardinal number into an (English language) ordinal
        parameters:
            cardinal (int)
        returns:
            ordinal (str)
    """
    
    #First we ensure that the input is an integer
    try:
        cardinal = int(cardinal)
    except:
        return 'Not an integer'

    #The ending of a cardinal number in English
    #is determined by its final two digits
    last_digit = str(cardinal)[-1]
    try:
        second_last_digit = str(cardinal)[-2]
    except:
        second_last_digit = '0'
    if second_last_digit == '1':
        ender = 'th'
    else:
        if last_digit == '1':
            ender = 'st'
        elif last_digit == '2':
            ender = 'nd'
        elif last_digit == '3':
            ender = 'rd'
        else:
            ender = 'th'
            
    #We construct the ordinal number as a string and return it
    ordinal = str(cardinal)+ender
    return ordinal

def capitalizer(string):
    """
    render the first letter in the string uppercase and the remainder lowercase
        parameters:
            string (str)
        returns:
            newstring (str)
    """

    newstring = string[0].upper()
    newstring += string[1:].lower()
    return newstring

def quote_stripper(string):
    """
    check if string begins and ends with single or double quotes
    strip them
        parameters:
            string (str)
        returns:
            newstring (str)
    """

    if string[0] == string[-1] and (string[0] == '"' or string[0] == "'"):
        newstring = string[1:-1]
    else:
        newstring = string
    return newstring

def camelcaser(string, delimiter=" "):
    """
    turn a collection of words into one word in CamelCase format
        parameters:
            string (str)
            delimiter (str) [default: one space ' ']
        returns:
            word (str)
    """

    wordlist = string.split(delimiter)
    newstring = ""
    for word in wordlist:
        newstring += capitalizer(word)
    return newstring

def string2boolean_parser(string):
    """
    convert strings 'True' or 'T' and 'False' or 'F' into boolean values
    case-insensitive
    all other values raise ValueError
        parameters:
            string (str)
        returns:
            boolean (bool)
    """

    string = string.lower()
    if string == 'true' or string == 't':
        return True
    elif string == 'false' or string == 'f':
        return False
    else:
        raise ValueError

def dict_maker(lister):
    """
    turn a list into a dictionary with the keys being successive positive integers
        parameters:
            lister (any iterable object)
        returns:
            mydict (dict)
    """
    mydict = {}
    for i in range(len(lister)):
        mydict[i+1] = lister[i]
    return mydict

def table2class_parser(filename, classname, delimiter = ',', coder = 'utf-8'):
    """
    read delimited table from file
    create class based on table
    transmogrify each line into an object in the class
    return the class and its objects
        parameters:
            filename (str)
            classname (str)
            delimiter (str) [default: ',']
        returns:
            classname (class)
            classlist (list)
    """
    
    file = open(filename, encoding = 'utf-8')
    firstline = file.readline()
    attributelist = firstline.split(delimiter)
    classname = capitalizer(classname)
    classlist = []

    #cleanup time.
    #every line in a textfile ends with a newline character.
    attributelist[-1] = attributelist[-1][:-1]
    #the file might begin with a BOM character
    if attributelist[0][0] == '\ufeff':
        attributelist[0] = attributelist[0][1:]
    for i in range(len(attributelist)):
        attributelist[i] = quote_stripper(attributelist[i])

    #defining the init method
    def class_init(self, attributes):
        self.attributes = []
        for i in range(len(attributes)):
            attributes[i] = quote_stripper(attributes[i])
            setattr(self, attributelist[i], attributes[i])
            self.attributes.append(attributes[i])

    #defining the repr method
    def class_repr(self):
        output = ""
        for i in range(len(self.attributes)):
            output += self.attributes[i]
            output += ' | '
        output = output[:-3]
        return output

    #creating class
    Newclass = type(classname, (object,), {
        "labels": attributelist,
        "__init__": class_init,
        "__repr__": class_repr
        })

    #Instantiating the class
    ender = ""
    while not ender:
        nextline = file.readline()
        if nextline == ender:
            ender = 1
        else:
            attributes = nextline.split(delimiter)
            attributes[-1] = attributes[-1][:-1]
            x = Newclass(attributes)
            classlist.append(x)

    file.close()
    return Newclass, classlist
