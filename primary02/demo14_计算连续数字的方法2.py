# _Author: zc-cris


string = "232jj2kj2"

for i in string:
    if i.isalpha():
        string = string.replace(i, " ")

print(string)  # 232  2  2
string = string.split()
# If sep is not specified or is None, any
# whitespace string is a separator and empty strings are
# removed from the result

print(len(string))  # 3
