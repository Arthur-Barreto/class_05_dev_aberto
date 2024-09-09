""" Script que imprime a data e o autor do último commit feito no repositório. """

#!/usr/bin/env python3
import gettext
from dev_aberto import hello

if __name__ == "__main__":
    gettext.bindtextdomain("cli", "locale")
    gettext.textdomain("cli")
    _ = gettext.gettext

    date, name = hello()
    print(_("Último commit feito em: {} por {}").format(date, name))
