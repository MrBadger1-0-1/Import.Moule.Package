from datetime import datetime, date, time

from application.salary import calculate_salary
from application.db.people import get_employees

dictionary= {'Ivan':'5', 'Jhon':'2'}

def main():
    dt = datetime.now()
    print(dt.date())
    get_employees(dictionary, 'Venya', '2')
    calculate_salary(dictionary, 'Venya')


if __name__ == '__main__':
   main()