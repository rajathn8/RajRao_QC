'''
Approach 1
Requires Pandas
'''
import argparse
import datetime as dt
import pandas as pd


def read_log_file(file_name):
    '''Reading CSV File '''

    file = pd.read_csv(file_name)
    '''
    To Do
    --> Add Chunks
    --> We can add additional checks to make sure our file is not corrupt
    --> Exception Handling if file not found
    '''

    return file


def parse_input_date(input_date):
    '''Parse the Input Date to datetime format'''

    input_date = dt.datetime.strptime(input_date, '%Y-%m-%d').date()

    return input_date


def return_most_active_cookie(input_log_file, input_date):
    '''
    Function takes in a Dataframe and returns most active cookie for the specified date
    '''
    # Convert TimeStamp to datetime
    # New Column created with date
    input_log_file['date'] = pd.to_datetime(
        input_log_file['timestamp']).dt.date

    filtererd_cookie_for_day = input_log_file[input_log_file['date']
                                              == input_date]['cookie']

    cookie_counter = {}

    for cookie in filtererd_cookie_for_day:
        if cookie in cookie_counter:
            cookie_counter[cookie] = cookie_counter[cookie]+1
        else:
            cookie_counter[cookie] = 1

    if len(cookie_counter) == 0:
        return ['No Cookie for Mentioned Date']

    max_cookie_count = max(cookie_counter.values())

    return [cookie for cookie in cookie_counter if cookie_counter[cookie] == max_cookie_count]


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Return the most active cookie')
    parser.add_argument('-f', '--filename', help='File to be Parsed')
    parser.add_argument(
        '-d', '--date', help='mention the date to get its most active cookie')
    args = parser.parse_args()

    log_file = read_log_file(args.filename)
    cookie_date = parse_input_date(args.date)

    active_cookie = return_most_active_cookie(log_file, cookie_date)

    for values in active_cookie:
        print(values)

'''
Test Cases

1 -  Input date is not present in the Log File
2 -  Input date is there in the log file 
3 -  Input date is there in the log file and there frequency of cookies is the same
        - take the most recent cookie
            Since the log file is in ascending order the topmost cookie will be considererd
            as the most frequesnt cookie
            
4 -  Input date format is not correct
5 -  Input Log file format is not correct
6 -  Input Log file is big - Have to use chunks

'''
'''
Each Operation has been breaken down into multiple operations to add more features
'''
