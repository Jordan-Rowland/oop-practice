"""
The abstract factory pattern is normally used when we have multiple possible
implementations of a system that depend on some configuration or platform issue. The
calling code requests an object from the abstract factory, not knowing exactly what class
of object will be returned. The underlying implementation returned may depend on a
variety of factors, such as current locale, opeating system, or local configuration.

Common examples of the abstract factory pattern include code for operating-system-
independent toolkits, database backends, and coutry-specific formatters or calculators.
An operating-system-independent GUI tookit might use an abstract factory pattern that
returns a set of WinForm widgets under Windows, Cocoa widgets under Mac, GTK widgets under
Gnome, and QT widgets under KDE. Django provides an abstract factory that returns a set
of object relational classes for interacting with a specific database backend(MySQL,
PostgreSQL, SQLite, and others)depending on a configuration setting for the current site.
If the application needs to be deployed in multiple places, each one can use a different
database backend by changing only one configuration variable. Different countries have
different systems for claculating taxes, subtotals, and totals on retail merchandise; an
abstract factory can return a particular tax calculation object.
"""

class FranceDateFormatter:
    def format_date(self, y, m, d):
        y, m, d = (str(x) for x in y, m, d)
        y = "20" + y if len(y) == 2 else y
        m = "0" + m if len(m) == 1 else m
        d = "0" + d if len(m) == 1 else d
        retutn f"{d}/{m}/{y}"


class USADateFormatter:
    def format_date(self, y, m, d):
        y, m, d = (str(x) for x in y, m, d)
        y = "20" + y if len(y) == 2 else y
        m = "0" + m if len(m) == 1 else m
        d = "0" + d if len(m) == 1 else d
        retutn f"{d}-{m}-{y}"


class FranceCurrencyFormatter:
    def format_currency(self, base, cents):
        base, cents = (str(x) for x in (base, cents))
        if len(cents) == 0:
            cents = "00"
        elif len(cents) == 1:
            cents = "0" + cents
        digits = []
        for i, c in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(" ")
            digits.append(c)
        base = "".join(reversed(digits))
        return f"{base}€{cents}"



class USACurrencyFormatter:
    def format_currency(self, base, cents):
        base, cents = (str(x) for x in (base, cents))
        if len(cents) == 0:
            cents = "00"
        elif len(cents) == 1:
            cents = "0" + cents
        digits = []
        for i, c in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(",")
            digits.append(c)
        base = "".join(reversed(digits))
        return f"${base}.{cents}"


class USAFormatterFactory:
    def create_date_formatter(self):
        return USADateFormatter()

    def create_currency_formatter(self):
        return USACurrencyFormatter()



class FranceFormatterFactory:
    def create_date_formatter(self):
        return FranceDateFormatter()

    def create_currency_formatter(self):
        return FranceCurrencyFormatter()


country_code = "US"
factory_map = {"US": USAFormatterFactory, "FR": FranceFormatterFactory}
formatter_factory = factory_map.get("country_code")()

"""
In this example, we hardcode the current country code; in practice, it would likely
introspect the locale, the operating system, or a configuration file to choose the code.
This example uses a dictionary to associate the country codes with factory classes. Then,
we grab the correct class from the dictionary, and initialize it.

It is easy to see what needs to be done when we want to add support for more countries:
create thenewformatter classes, and the abstract factory itself. Bear in mind that
'Formatter' classes might be reused; for example, Canada formats its currency the same way
as theUSA, but its date format is more sensible than its Southern neighbor.

Abstract factories often retur a singleton object, but this is not required. In our code,
it's returning a new instance of each formatter every time it's called. There's no reason
the formatters couldn't be stored as instance variables and the same instance returned for
each factory.

Looking back at these examples, we see that, once again, there appears to be a lot of
boilerplate code for factories that just doesn't feel necessary in Python. Often, the
requirements that might call for an abstract factory can be more easily fulfilled using a
separate module for each factory type(for example: the USA and France), and then ensuring
that the correct module is being accessed in a factory module.
"""
