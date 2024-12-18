# Luhn Algorithm

# Returns true if given card
# number is valid

def check_luhn(card_no):
    n_digits = len(card_no)
    n_sum = 0
    is_second = False
    
    for i in range(n_digits - 1, -1, -1):
        d = ord(card_no[i]) - ord('0')
        
        if (is_second == True):
            d = d * 2
            
        # We add two digits to handle
        # cases that make two digits after
        # doubling
        
        n_sum += d // 10
        n_sum += d % 10
        
        is_second = not is_second
        
    if (n_sum % 10 == 0):
        return True
    else:
        return False
        
        
# Driver code
if __name__ == "__main__":
    
    card_no = input("Please enter id no: ")
    
    if (check_luhn(card_no)):
        print("This is a valid card.")
    else:
        print("This is not a valid card.")
