#loadbearing comment DO NOT DELETE
#this script adds protein
#created specifically as a learning example for u/kxshxsh



def proteinadd():
    #this function asks for user inputs on how many eggs, then how many loaves of bread are being used.
    print('Welcome to Protein Adder!')
    try:
        eggs=float(input('How many eggs are you adding to your omelet today?'))
    #asks for how many eggs
        
    except:
        print("That's not a number. Please try again.")
        proteinadd()
        #makes sure the eggs variable is a float, and returns to the beginning if it's
        #not. This is called recursion and is bad, but this is only an example
        #and needs to be simple.
    
    try:
        loaves=float(input('How many loaves of bread are you adding to your omelet today?'))
    #asks for how many loaves
    
    except:
        print("That's not a number. Please try again.")
        proteinadd()
        #makes sure the loaves variable is a float, and returns to the beginning if it's
        #not. This is called recursion and is bad, but this is only an example
        #and needs to be simple.
        
    
    protein_per_egg= float(6) #grams
    #this line assigns the number 6 to the protein_per_egg variable
    
    protein_per_loaf= float(2) #grams
    #this line assigns the number 2 to the protein_per_loaf variable
    
    protein_in_the_omelet= (float((eggs*protein_per_egg)))+(float((loaves*protein_per_loaf)))
    #the above line multiplies the user inputs by how much protein each item has
    #, then adds them together
    
    print(f'Your omelet will have {protein_in_the_omelet} grams of protein')
    #this print uses f strings because f strings are awesome. the
    #letters in the curly {} brackets counts as a variable.
    check_if_user_wants_to_restart()
    #this calls a function to see if you want to close the program

def check_if_user_wants_to_restart():
    #this asks if you want to close the program, and restarts if you enter anything
    #but 'y'
    answer=input('Would you like to close this program? y/n')
    if answer=='y':
        quit()
        #this quits, I dont have to define quit because it's built into python.
    else:
        proteinadd()
        #calls proteinadd and restarts it.

proteinadd()
#this actually 'calls' or activates the proteinadd function. Python doesnt do anything until
#you call the function, so it will let you define as many functions as you like
#before the program actually does anything.
    
