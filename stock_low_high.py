# Design an algorithm that determines the maximum profit that
# could have been made by buying and then selling a single
# share over a given day range, subject to the constraint that
# the buy and the sell have to take place at the start of the day

import random
import sys


# Code to setup problem
class Share:

    def __init__(self):
        self.low = random.randint(0, 1000000)
        self.high = random.randint(self.low + 1, 10000000)
        self.opening_bell = random.randint(self.low, self.high)

    def get_high(self):
        return self.high

    def get_low(self):
        return self.low

    def get_open(self):
        return self.opening_bell

    def print_share(self):
        print("Low:", self.low)
        print("Opening Bell:", self.opening_bell)
        print("High:", self.high)


def example_stock(num_days):
    days = []
    for num in range(num_days):
        share = Share()
        days.append(share)
    return days


apple = example_stock(40)
ge = example_stock(1000000)

day1 = Share()
day1.opening_bell = 10
day1.low = 8
day1.high = 25
day2 = Share()
day2.opening_bell = 15
day2.low = 4
day2.high = 20
day3 = Share()
day3.opening_bell = 20
day3.low = 30
day3.high = 45
google = [day1, day2, day3]

# for num in range(len(google)):
#     print("Day:", num)
#     google[num].print_share()


#######################################
# Solutions #

def brute_force(stock):
    highest_difference = 0
    buy_date = 0
    sell_date = 0
    for num1 in range(len(stock)):
        to_compare = stock[num1].get_open()

        for num2 in range(num1, len(stock)):
            if stock[num2].get_open() - to_compare > highest_difference:
                highest_difference = stock[num2].get_open() - to_compare
                buy_date = num1
                sell_date = num2

    print("Profit:", highest_difference)
    print("Buy Day:", buy_date)
    print("Sell Day:", sell_date)


def optimal(stock):
    min_price = sys.maxsize
    highest_profit = 0
    buy = 0
    sell = 0
    for num in range(len(stock)):
        if stock[num].opening_bell < min_price:
            min_price = stock[num].opening_bell
            buy = num
        elif stock[num].opening_bell - min_price > highest_profit:
            highest_profit = stock[num].opening_bell - min_price
            sell = num

    print("Profit:", highest_profit)
    print("Buy Day:", buy)
    print("Sell Day:", sell)


# brute_force(apple)
# optimal(apple)
# brute_force(ge)
optimal(ge)
# brute_force(google)
# optimal(google)
