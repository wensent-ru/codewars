"""
Abbreviate a Two Word Name

Write a function to convert a name into initials.
The output should be two capital letters with a dot separating them.
It should look like this:

Sam Harris => S.H
patrick feeney => P.F
"""


def abbrev_name(name):
    return ".".join([i[0] for i in name.split()]).upper()
