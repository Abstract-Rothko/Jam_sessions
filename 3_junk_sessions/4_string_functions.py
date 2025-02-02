# String Functions Project
# This mini-project re-creates some of the most common string methods in python
# How close I got to its actual method is up for debate
# Still, these functions produce the same, or a similar result, so I'm satisfied'

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z"]
capitals = [i.upper() for i in letters]
letters_ordinal = [ord(i) for i in letters]
capitals_ordinal = [ord(i) for i in capitals]

class StringError(Exception):
    pass

def _capitalize(entry):
    """
    Return a capitalized version of the string. More specifically, 
    make the first character have upper-case and the rest lower-case.
    
    >>> _capitalize('Capitalism F**** You One Letter At A Time.')
    
    > 'Capitalism f**** you one letter at a time.'
    
    """
    var = ""
    first_letter = entry[0]
    other_letters = entry[1:]
    if first_letter in capitals:
        var += first_letter
    else:
        upper_case = chr(ord(first_letter) - 32)
        var += upper_case
    for i in other_letters:
        if i in capitals:
            lower_case = chr(ord(i) + 32)
            var += lower_case
        else:
            var += i
    return var
    

def _center(entry, spaces = 10, type = "★"):
    """
    Returns a centred string of length spaces.
    Padding is done using a specified fill character(type = "★")
    
    >>> _center("zenith", 12)
    
    > '★★★zenith★★★'
    
    """
    if len(entry) > spaces:
        raise StringError
    remainder_spaces = spaces - len(entry)
    spaces_left = remainder_spaces // 2
    spaces_right = remainder_spaces - spaces_left
    return (type * spaces_left) + entry + (type * spaces_right)


def _lower(entry):
    """
    Returns a copy of the string with all latin letters converted to lower-case.
    
    >>> _lower("KEVIN HART")
    
    > 'kevin hart'
    
    """
    var = ""
    for i in entry:
        if i in letters:
            var += i
        elif i in capitals:
            lower_case = chr(ord(i) + 32)
            var += lower_case
        else:
            var += i
    return var


def _upper(entry):
    """
    Returns a copy of the string with all latin letters converted to upper-case.
    
    >>> _upper("dwayne johnson")
    
    > 'DWAYNE JOHNSON'
    
    """
    var = ""
    for i in entry:
        if i not in capitals and i not in letters and i != " ":
            raise StringError("Only alphabetical characters and whitespaces are allowed")
        elif i in letters:
            upper_case = chr(ord(i) - 32)
            var += upper_case
        elif i == " ":
            var += i
        elif i in capitals:
            var += i
        else:
            raise StringError("Entries can only be non-empty arrangement of alphabetical characters")
    return var


def _count(entry, search_value, ignore_casing = False):
    """
    Returns the number of non-overlapping occurrences of substring in S[start:end].
    
    >>> _count("pussy", "u")
    
    > 1
    
    """
    if len(search_value) != 1:
        raise StringError("search_value argument should be 1 letter.")
    counter = 0
    if ignore_casing == False:
        for i in entry:
            if i == search_value:
                counter += 1
    else:
        lower_case_entry = _lower(entry)
        lower_case_search_value = _lower(search_value)
        for i in lower_case_entry:
            if i == lower_case_search_value:
                counter += 1
    return counter

def _join(entry, delimeter = ","):
    """
    Joins all items of tuple/list into one string.
    Concatenates any number of strings.
    
    >>> _join(["Me", "+", "untouched", "grass", "=", "social", "life."], delimeter = " ")
    
    > 'Me + untouched grass = social life.'
    
    """
    string = ""
    for i in entry[:len(entry) - 1]:
        string += str(i) + delimeter
    string += entry[-1]
    return string
    
    
def _lstrip(entry):
    """
    Removes whitespaces from the beginnong of a string
    """
    counter = 0 # counts the number of whitespaces
    while entry[counter] == " ":
        counter += 1
    return entry[counter: ]


def _rstrip(entry):
    """
    Removes trailing whitespaces in a string
    """
    counter = -1
    while entry[counter] == " ":
        counter -= 1
    if counter == -1:
        counter = len(entry) + 1
    else:
        counter = len(entry) - counter
    return entry[:counter]


def _split(entry, sep = " "):
    """
    Return a list of substrings in the string, using sep as the seperator string.
    
    >>> _split("Life is better on Saturn.")
    
    > ['Life', 'is', 'better', 'on', 'Saturn']
    """
    lst = []
    counter = 0
    for i in entry:
        if i == sep:
            lst.append(counter)
            counter += 1
        else:
            counter += 1
            
    tracker = len(lst)
    new_list = []
    number = 0
    while tracker != 0:
        for i in lst:
            new_list.append(entry[number: i])
            number = i + 1
            tracker -= 1
    
    new_list.append(entry[number:])
    while new_list[-1] == sep:
        new_list.pop()
    
    return new_list
    


def _strip(entry):
    """
    Return a copy of the string with the leading and trailing whitspace removed.
    """
    value = _lstrip(entry)
    new_entry = _rstrip(value)
    return new_entry
    
def _swapcase(entry):
    """
    Convert upper-case characters to lower-case and vice versa.
    
    >>> _swapcase("jUICE wrld")
    
    > 'Juice WRLD'
    
    """
    var = ""
    for i in entry:
        if i in letters:
            upper_case = chr(ord(i) - 32)
            var += upper_case
        elif i in capitals:
            lower_case = chr(ord(i) + 32)
            var += lower_case
        else:
            var += i
    return var
    
    
def _title(entry):
    """
    Return a version of the string where each word is title-cased. 
    More specifically, words start with upper-cased characters and all 
    remaining characters are lower-case.
    """
    lower_case = _lower(entry)
    split = _split(lower_case)
    capitalized = []
    for i in split:
        capitalized.append(_capitalize(i))
    joined = _join(capitalized, " ")
    return joined
    