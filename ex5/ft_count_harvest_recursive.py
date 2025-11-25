#!/usr/bin/env python

def ft_count_harvest_recursive(days = -1):
    harvest_day = -1
    if days == -1:
        days = int(input("Days until harvest: "))
        harvest_day = days
    if (days > 0):
        ft_count_harvest_recursive(days - 1)
        print("Day", days)
        flag = 0
    if harvest_day == days:
        print("Harvest time!")
ft_count_harvest_recursive()
