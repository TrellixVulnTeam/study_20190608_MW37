"""this is for default dict which can solve counting string"""
# !/usr/bin/env python3
# coding=utf-8
from collections import defaultdict


def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana', 'apple', 'orange', 'grape', 'banana']
    # TODO: use defaultdict to count each element
    # fruit_counter = defaultdict(int)   # initialize it with empty int, you can also use str to empty string
    fruit_counter = defaultdict(lambda: 100)    # now it will start off at 100, normally it is lambda:0
    # count the element in the list
    for fruit in fruits:
        fruit_counter[fruit] += 1
    # print the result
    for (k, v) in fruit_counter.items():
        print(k + ':' + str(v))


if __name__ == '__main__':
    main()