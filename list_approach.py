'''
Approach 2
Using List

'''
import argparse
import csv
from collections import Counter


def read_log_file(file_name, input_date):
    '''Reading CSV File and returns the list of cookies for the particular date '''

    cookie_list_for_date = []

    with open(file_name, "r", encoding='UTF-8') as file:

        reader = csv.reader(file)

        for line in reader:

            if line[1][:10] == input_date:
                cookie_list_for_date.append(line[0])

    '''
    To Do 
    --> Add Chunks
    --> We can add additional checks to make sure our file is not corrupt
    --> Exception Handling if file not found 
    '''

    return cookie_list_for_date


def return_most_active_cookie(input_list):
    '''
    Function takes in a list and returns most frequent element
    '''
    cookie_counter = Counter(input_list)

    if len(cookie_counter) == 0:
        return 'No Cookie for Mentioned Date'

    max_cookie_count = max(cookie_counter.values())
    return [cookie for cookie in cookie_counter if cookie_counter[cookie] == max_cookie_count]


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Return the most active cookie')
    parser.add_argument('-f', '--filename', help='File to be Parsed')
    parser.add_argument(
        '-d', '--date', help='mention the date to get its most active cookie')

    args = parser.parse_args()
    cookie_list = read_log_file(args.filename, args.date)
    active_cookie = return_most_active_cookie(cookie_list)

    print(active_cookie)
