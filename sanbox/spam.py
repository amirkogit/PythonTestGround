# this will add a word 'spam' every time we call this function
def add_spam(menu =[]):
    menu.append("spam")
    return menu


def add_spam2(menu = None):
    if menu is None:
        menu = []
    menu.append("spam")
    return menu


def main():
    # passing non-empty arguments and adding spam three times
    # works fine
    vegetables_menu = ["potato","tomato"]
    add_spam(vegetables_menu)
    add_spam(vegetables_menu)
    add_spam(vegetables_menu)

    print(vegetables_menu)

    # passing non-empty arguments and adding spam three times
    # works fine
    fruit_menu = ["apples","oranges"]
    fruit_menu = add_spam2(fruit_menu)
    fruit_menu = add_spam2(fruit_menu)
    fruit_menu = add_spam2(fruit_menu)

    print(fruit_menu)

    # passing empty argument and adding spam three times
    # spam is added three times because menu[] is defined only once when
    # we enter the method add_spam()
    empty_menu = add_spam()
    empty_menu = add_spam()
    empty_menu = add_spam()

    print(empty_menu)

    # passing empty argument and adding spam three times
    # spam is added once because we are clearing the menu[] if argument is None
    empty_menu2 = add_spam2()
    empty_menu2 = add_spam2()
    empty_menu2 = add_spam2()

    print(empty_menu2)

if __name__ == "__main__":
    main()