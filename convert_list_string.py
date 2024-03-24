#!/usr/bin/env python3


""" this function takes a List  and 
returns a single string with all the elements of 
the list separated by a one space."""


def convert_list_string(list: list):
    conv_string = ", ".join(list)
    return conv_string


# print is for testing purposes
# print(convert_list_string(["a", "b", "c"]))
