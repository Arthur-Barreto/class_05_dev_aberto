""" script to print the last commit date and author """

#!/usr/bin/env python3
import gettext
from datetime import datetime
from dev_aberto import hello
from babel.dates import format_date

if __name__ == "__main__":
    gettext.bindtextdomain("cli", "locale")
    gettext.textdomain("cli")
    _ = gettext.gettext

    my_date, name = hello()

    # Convert ISO datetime string to datetime object
    try:
        my_date = datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as e:
        print(f"Erro ao formatar a data: {e}")
        exit(1)

    # Format the date for output
    formatted_date = format_date(my_date)

    print(_("Último commit feito em: {} por {}").format(formatted_date, name))
