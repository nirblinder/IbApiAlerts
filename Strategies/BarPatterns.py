import MyBar


def red_green(bar_last, bar_last_last):
    return True if (MyBar.is_red(bar_last_last) is True and MyBar.is_green(bar_last) is True) else False


def green_red(bar_last, bar_last_last):
    return True if (MyBar.is_green(bar_last_last) is True and MyBar.is_red(bar_last) is True) else False


def body_bigger(bar_last, bar_last_last):
    return True if ((MyBar.body_size(bar_last) / MyBar.body_size(bar_last_last)) > 1) else False
