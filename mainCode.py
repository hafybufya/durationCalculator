import numpy as np

def date_time_calc(date_inputted=None):
    """
    Function which returns today - date_time_calc
    """
    today = np.datetime64('today')
    if date_inputted is None:
        #only asks is no date inputted -> necessary for unit tests
        while True:
            try:
                date_inputted = np.datetime64(input("Insert a date (YYYY-MM-DD): "))
                
                if date_inputted > today:
                    print("Date cannot be a future date.")
                else:
                    date_inputted = date_inputted
                    break
            except ValueError:
                print("Must be in format YYYY-MM-DD")
    else:
        # if date_inputted is None (unit_test) converts to np.datetime64
        date_inputted = np.datetime64(date_inputted)
    
    num_days = today - date_inputted
    return num_days

#using xfill{2} using it so that users input values seperately maybe

if __name__ == "__main__":
    date_time_result= date_time_calc()  # calls function and asks for input
    print(f"Number of days: {date_time_result}")



