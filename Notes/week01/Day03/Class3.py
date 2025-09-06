# functiona to arbitary number of arguments
def multiple_arg(*args):
    c = 0
    for i in args:
        c += i

    return c

out = multiple_arg(5,5,4,2)
print(out)