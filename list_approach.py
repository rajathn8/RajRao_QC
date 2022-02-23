'''
Approach 2
Using List and Dict

'''
import argparse
import csv


def read_log_file(file_name, input_date):
    '''
    Reading CSV File and returns the list of cookies for the particular date
    '''

    cookie_list_for_date = []

    with open(file_name, "r", encoding='UTF-8') as file:

        reader = csv.reader(file)
        
        cookie_list_for_date = [ line[0] for line in reader if line[1][:10] == input_date]

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
    cookie_counter = {}

    for cookie in input_list:
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

    cookie_list = read_log_file(args.filename, args.date)
    active_cookie = return_most_active_cookie(cookie_list)

    for values in active_cookie:
        print(values)
