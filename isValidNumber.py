import re

def is_valid(num):
    numparts = re.split("e|E", num)
    #first part integer or decimal
    if not is_int_or_dec(numparts[0]):
        return False
    #if there is a second part
    # is it an integer 
    if len(numparts) == 2:
        if not is_integer(numparts[1]):
            return False
    return True

def is_integer(num):
    try:
        int(num)
        return True
    except:
        return False

def is_decimal(num):
    n = num
    if num[0] == "+" or num[0] == "-":
        n = num[1:]
    if n[0] == "+" or n[0] == "-":
        return False
        
    if "." in n:
        if n == "." * len(n):
            return True
        nums = n.split(".")
        if not (is_integer(nums[0]) or nums[0] == "") or not (is_integer(nums[1]) or nums[1] == ""):
            return False
        return True
    return False
def is_int_or_dec(num):
    return is_integer(num) or is_decimal(num)