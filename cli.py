""" This is a simple CLI program """

from datetime import date
import gettext
from babel.dates import format_date
from babel.numbers import format_decimal


if __name__ == "__main__":
    gettext.bindtextdomain("cli", "locale")
    gettext.textdomain("cli")
    _ = gettext.gettext

    today = format_date(date.today())
    print(_(today))

    NUMBER = format_decimal(240000000000.32212)
    print(_(NUMBER))

    name = input(_("Input your name: "))
    print(_('Hello {}').format(name))
