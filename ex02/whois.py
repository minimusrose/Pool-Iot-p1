import sys

def integer_type()  : 
    # Output the type of an integer : odd, even or zero.
    if len(sys.argv) == 1 : 
        print("Usage : python whois.py <string1>")
    elif len(sys.argv) > 2 : 
        print("AssertionError : more than one argument are provided. ") 
    else : 
        try : 
            integer = int(sys.argv[1])
            if integer == 0 :
                print("I'm zero.")
            elif integer % 2 == 0 : 
                print("I'm Even.")
            else : 
                print("I'm Odd.") 
        except ValueError :
            print("AssertionError : argument is not an integer") 
          
        
        
if __name__ == "__main__" : 
    integer_type()