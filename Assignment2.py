from datetime import datetime

def find_day_of_week(date_str: str) -> str:
    year, month, day = map(int, date_str.split('-'))
    date_object = datetime(year, month, day)
    return date_object.strftime('%A')

if __name__ == "__main__":
    date_input = input("Enter any Year, Month, and Date (YYYY-MM-DD): ")
    day_of_week = find_day_of_week(date_input)
    print(f"The day of the week for {date_input} is {day_of_week}.")
