def banner(message,border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("Default banner")
banner("Banner with * sign", "*")
banner("Banner with explicit param",border="*")
banner(border=".",message="Banner with positional arguments")