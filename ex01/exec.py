import sys
def strings_treatment() : 
    if len(sys.argv) == 1 : 
        print("Usage : python exec.py <string1> [string2 ...]")
        return
    
    elif len(sys.argv) == 2 :
        input_string = sys.argv[1]
    
    else : 
        input_string = " ".join(sys.argv[1:])
       
    swaps_string = input_string.swapcase()
    final_string = swaps_string[::-1]
    print(final_string)

if __name__ == "__main__" :     
    strings_treatment()
            
