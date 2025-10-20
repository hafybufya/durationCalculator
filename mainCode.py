import numpy as np

def date_time_calc(date_inputted=None):
    """Function which performs 'today - user input date' calculation."""
    today = np.datetime64('today')
    if date_inputted is None:
        date_inputted = np.datetime64(input("Insert a date (YYYY-MM-DD): "))
    
    date_inputted = np.datetime64(date_inputted)

    num_days = today - date_inputted
    return num_days

print(date_time_calc())


#using xfill{2} using it so that users input seperately.

if __name__ == "__main__":
    date_time_result= date_time_calc()  # calls function and asks for input
    print(f"Number of days: {date_time_result}")