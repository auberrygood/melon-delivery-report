'''VARIABLES'''
day_1 = open("um-deliveries-20140519.txt")
day_2 = open("um-deliveries-20140520.txt")
day_3 = open("um-deliveries-20140521.txt")

delivery_days = [day_1, day_2, day_3]

'''FUNCTIONS'''
def get_delivery_info(the_file):
    '''single function to call for delivery info, when passing in the day's file via defined variable''' 
    for line in (the_file):
        line = line.rstrip()
        words = line.split('|') #define element separation by presence of "|"

        melon = words[0]  #melon is the first element in the line of words
        count = words[1]  #count is the second element in the line of words
        amount = words[2]  #amount is the third element in the line of words

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()

def get_daily_delivery_info(delivery_days):
    "function that produces delivery info for each day, given a single list of days"
    counter = 1    #counter so that header will change to respective day each time code is looped
    for day in (delivery_days):
        print (f"Day {counter}:")
        get_delivery_info(day)  #call previous function that pulls deliver data for single day
        counter += 1   #adjust counter for next loop/header
        print()


'''MAIN PROGRAM'''
get_daily_delivery_info(delivery_days)
