'''VARIABLES'''
day_1 = open("um-deliveries-20140519.txt")
day_2 = open("um-deliveries-20140520.txt")
day_3 = open("um-deliveries-20140521.txt")

delivery_days = [day_1, day_2, day_3]

'''FUNCTIONS'''
def get_delivery_info(the_file):
    '''single function to call for delivery info, when passing in the day's file''' 
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()

def get_daily_delivery_info(delivery_days):
    for day in delivery_days:
        print (day)
        get_delivery_info(day)


get_daily_delivery_info(delivery_days)

# print("Day 1")
# get_delivery_info(day_1)

# print()

# print("Day 2")
# get_delivery_info(day_2)

# print()

# print("Day 3")
# get_delivery_info(day_3)
