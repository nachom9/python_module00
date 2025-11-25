#!/usr/bin/env python

def ft_seed_inventory(fruit, number, unit):
    print(fruit, "seeds:", end= " ")
    print(number , end= " ")
    if unit == "packets":
        print("packets available")
    elif unit == "grams":
        print("grams total")
    elif unit == "area":
        print("square meters")
