from datetime import datetime


CURRENT_YEAR = datetime.now().year
ZODIAC = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
GENERATIONS = ["The Greatest Generation", "The Silent Generation", "The Baby Boomer Generation", "Generation X", "Millennials(Generation Y)", "Generation Z", "Generation Alpha"]
THIRTY_DAY_MONTHS = [4, 6, 9, 11]
THIRTY_ONE_DAY_MONTHS = [1, 3, 5, 7, 8, 10, 12]


class BirthDateError(Exception):
    pass
    

def age(year, month, day):
    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = CURRENT_YEAR
    if current_month > month and current_day > day:
        return current_year - year
    else:
        return current_year - year - 1
    
    
def leap_year(year):
    result = False
    if year % 4 == 0:
        result = True
    if year % 100 == 0:
        result = False
    if year % 400 == 0:
        result = True
    return result


def birthdate_validator(year, month, day):
    if year in range(CURRENT_YEAR - 100, CURRENT_YEAR + 1):
        if leap_year(year):
            if month == 2:
                return day in range(1, 30)
            elif month in THIRTY_DAY_MONTHS:
                return day in range(1, 31)
            elif month in THIRTY_ONE_DAY_MONTHS:
                return day in range(1, 32)
            else:
                raise BirthDateError(f"{year}-{month}-{day} is incorrect. Please fix.")
        else:
            if month == 2:
                return day in range(1, 29)
            elif month in THIRTY_DAY_MONTHS:
                return day in range(1, 31)
            elif month in THIRTY_ONE_DAY_MONTHS:
                return day in range(1, 32)
            else:
                raise BirthDateError
    else:
        raise BirthDateError


def star_sign(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return ZODIAC[0]
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return ZODIAC[1]
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return ZODIAC[2]
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return ZODIAC[3]
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return ZODIAC[4]
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return ZODIAC[5]
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return ZODIAC[6]
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return ZODIAC[7]
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return ZODIAC[8]
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return ZODIAC[9]
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return ZODIAC[10]
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return ZODIAC[11]
    else:
        raise BirthDateError
        
        
def gen(year):
    if year in range(1901, 1925):
        return GENERATIONS[0]
    elif year in range(1925, 1946):
        return GENERATIONS[1]
    elif year in range(1946, 1965):
        return GENERATIONS[2]
    elif year in range(1965, 1980):
        return GENERATIONS[3]
    elif year in range(1980, 1995):
        return GENERATIONS[4]
    elif year in range(1995, 2013):
        return GENERATIONS[5]
    elif year in range(2013, CURRENT_YEAR +1):
        return GENERATIONS[6]
    else:
        raise BirthDateError(f"{year} is not within range(1900, {CURRENT_YEAR + 1}).")
        
        
def main():
    your_name = input("Enter your name: ")
    birth_year = int(input("Enter your birth year: "))
    birth_month = int(input("Enter your birth month(1-12): "))
    birth_day = int(input("Enter your birth day(1 - 31): "))
    if birthdate_validator(birth_year, birth_month, birth_day):
        your_age = age(birth_year, birth_month, birth_day)
        your_zodiac = star_sign(birth_month, birth_day)
        your_gen = gen(birth_year)
        print()
        print("Your details are as follows...")
        print("------" * 6)
        print(f"""
Name: {your_name}
Age: {your_age}
Zodiac Sign: {your_zodiac}
Generation: {your_gen}
        """)
        print("------" * 6)
        
        
if __name__ == "__main__":
    main()