"""
The template pattern is useful for removing duplicate code; it's intended to support the
DRY principle. It is designed for situations where we have several different tasks to
accomplish that have some, but not all, steps in common. The common steps are implemented
in a base class, and the distinct steps are overridden in subclasses to provide custom
behaviour. In some ways, it's like a generalized strategy pattern, except similar sections
of the algorithm are shared using a base class.
"""

import sqlite3

conn = sqlite3.connect('sales.db')

conn.execute("""
    DROP TABLE IF EXISTS sales;
""")

conn.execute(
    "CREATE TABLE sales (salesperson text, "
    "amt currency, year integer, model text, new boolean)"
)

conn.execute("""
    INSERT INTO sales VALUES
    ('Tim', 16000, 2010, 'Honda Fit', 'true'),
    ('Tim', 9000, 2006, 'Ford Focus', 'false'),
    ('Gayle', 8000, 2004, 'Dodge Neon', 'false'),
    ('Gayle', 28000, 2009, 'Ford Mustang', 'true'),
    ('Gayle', 50000, 2010, 'Lincoln Navigator', 'true'),
    ('Don', 20000, 2008, 'Toyota Prius', 'false');
""")

conn.commit()
conn.close()


class QueryTemplate:
    def connect(self):
        self.conn = sqlite3.connect('sales.db')

    def construct_query(self):
        raise NotImplementedError()

    def do_query(self):
        results = self.conn.execute(self.query)
        self.results = results.fetchall()

    def format_results(self):
        output = []
        for row in self.results:
            row = [str(i) for i in row]
            output.append(", ".join(row))
        self.formatted_results = "\n".join(output)

    def output_results(self):
        raise NotImplementedError

    def process_format(self):
        self.connect()
        self.construct_query()
        self.do_query()
        self.format_results()
        self.output_results()


import datetime


class NewVehicleQuery(QueryTemplate):
    def construct_query(self):
        self.query = "SELECT* FROM sales WHERE new = 'true'"

    def output_results(self):
        print(self.formatted_results)


class UserGrossQuery(QueryTemplate):
    def construct_query(self):
        self.query = """
            SELECT salesperson, sum(amt) FROM sales GROUP BY salesperson
        """

    def output_results(self):
        filename = f"Gross_Sales_{datetime.datetime.today().strftime('%Y%m%d')}"
        with open(filename, "w") as outfile:
            outfile.write(self.formatted_results)


