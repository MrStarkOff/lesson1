def get_summ(one, two, delimiter="&"):
    return str(one + delimiter + two).upper()
    

print(get_summ("Learn", "python"))