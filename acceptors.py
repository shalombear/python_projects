"""Prompt the user for an answer and return an acceptable value to the program

Functions:
yn_acceptor -- for asking yes/no questions, returns a boolean
posint_acceptor -- for obtaining a positive integer
natnum_acceptor -- for obtaining a nonnegative integer
int_acceptor -- for obtaining an integer
num_acceptor -- for obtaining a number, returns a float
seq_acceptor -- asks for a sequence of inputs and stores them to a list
    args: n (length of sequence), name (of object being entered)
"""

import otoodles

#A standard error message to be used by all the functions
error_msg = "\nI'm sorry. That is not an acceptable input. Please try again.\n"

def yn_acceptor(question):
    """Ask a yes/no question and return a boolean"""
    #Keeps asking the question until user
    #inputs a response that begins with either 'y' or 'n'.
    ender = False
    while not ender:
        
        #Taking only the first letter of the response allows the
        #user to input 'y', 'yes', 'yeah', etc.
        #The exception is for if the user response is the empty string
        try:
            reply = str(input(question+' (y/n): '))[0].lower()
        except:
            reply = ""
            
        #Output is a boolean, True for 'yes' and False for 'no'
        if reply == 'y':
            return True
        elif reply == 'n':
            return False
        else:
            print(error_msg)

def posint_acceptor(question):
    """Request a positive integer and return it"""
    #Keeps asking the question until user
    #inputs a positive integer.
    ender = False
    while not ender:
        try:
            reply = int(input(question+' (Enter a positive integer): '))
        except:
            reply = 0
        if reply > 0:
            return reply
        else:
            print(error_msg)

def natnum_acceptor(question):
    """Request a non-negative integer and return it"""
    #Keeps asking the question until user
    #inputs a natural number.
    ender = False
    while not ender:
        try:
            reply = int(input(question+' (Enter a natural number): '))
        except:
            reply = -1
        if reply >= 0:
            return reply
        else:
            print(error_msg)

def int_acceptor(question):
    """Request an integer and return it"""
    #Keeps asking the question until user
    #inputs an integer.
    ender = False
    while not ender:
        try:
            reply = int(input(question+' (Enter an integer): '))
        except:
            reply = 'x'
        if type(reply) == int:
            return reply
        else:
            print(error_msg)

def num_acceptor(question):
    """Request an integer and return it"""
    #Keeps asking the question until user
    #inputs an integer.
    ender = False
    while not ender:
        try:
            reply = float(input(question+' (Enter a number): '))
        except:
            reply = 'x'
        if type(reply) == float:
            return reply
        else:
            print(error_msg)

def seq_acceptor(n, name, typer=str):
    """
    Request 'n' entries of type 'typer' with label 'name'
    Store them to a list
    """
    
    lister = []
    for i in range(n):
        accepted = False
        while not accepted:
            try:
                entry = typer(input('Enter the {} {}: '.format(otoodles.ordinal(i+1), name)))
            except:
                print(error_msg)
            else:
                accepted = True
                lister.append(entry)
    return lister
