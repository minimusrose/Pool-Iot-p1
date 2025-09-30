import sys
from string import punctuation

def text_analyser(text = None) : 
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
    if len(sys.argv) == 2: 
        text_to_analyse = sys.argv[1]
    elif text is not None:
        text_to_analyse = text
    else: # Aucun argument n'a été passé ni via ligne de commande, ni directement à la fonction

        text_to_analyse = input("What is the text to analyse? ")
            
    if not isinstance(text_to_analyse, str) : 
        print("AssertionError : argument is not a string.")
        return
    else :     
        upper_case_number = 0
        lower_case_number = 0
        punctuation_number = 0
        spaces_number = 0
        for letter in text_to_analyse : 
            if letter.isupper():
                upper_case_number+=1
            elif letter.islower() : 
                lower_case_number+=1
            elif letter.isspace() :
                spaces_number+=1
            elif letter in punctuation :
                punctuation_number+=1
        characters_number = upper_case_number + lower_case_number + punctuation_number + spaces_number        
        print("The text contains",characters_number, "character(s) : ")
        print(upper_case_number,"upper letter(s)")
        print(lower_case_number, "lower letter(s)")
        print(punctuation_number, "punctuation mark(s)")
        print(spaces_number, "space(s)")



if __name__ == "__main__" : 
    if len(sys.argv) > 2 : 
        print("AssertionError : more than one argument are provided. ")  
    elif len(sys.argv) == 1:
        text_analyser()
    else : 
        text_analyser(sys.argv[1])

    