# INPUT
date = input("Date (MM/DD/YYYY): ")

# VARIABLES
month = date[0:2]
day = date[3:5]
year = int(date[6::])

# DICTIONARIES
doomsdays = {"01-common": 3,
             "01-leap": 4,
             "02-common": 28,
             "02-leap": 29,
             "03": 14,
             "04": 4,
             "05": 9,
             "06": 6,
             "07": 11,
             "08": 8,
             "09": 5,
             "10": 10,
             "11": 7,
             "12": 12
             }

numberToWord = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

moduloYearToValue = {0: 2,
                     100: 0,
                     200: 5,
                     300: 3
                     }

days = {0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday"
        }

# CALCULATIONS
def yearCode(year):
    return (year % 400) + (year % 100) // 12 + (year % 100) % 12 + ((year % 100) % 12) // 4

def leapCheck(year):
    if year % 100 % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 % 4 == 0 and year % 400 == 0:
        return True
    return False

def dayOfTheWeek(code, leap, month, day, year):
    if leap and (month == "01" or month == "02"):
        doomsday = doomsdays[month+"leap"]

    else:
        doomsday = doomsdays[month]

    if doomsday > day:
        return f"{numberToWord[month]} {day}, {year} is a {days[(code - doomsday + day) % 7]}."

    else:
        return f"{numberToWord[month]} {day}, {year} is a {days[(code + doomsday - day) % 7]}."

print(dayOfTheWeek(yearCode(year), leapCheck(year), month, int(day), year))
