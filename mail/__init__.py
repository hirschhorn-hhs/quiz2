import check50
import check50.c

@check50.check()
def exists():
    """mail.c exists"""
    check50.exists("mail.c")

@check50.check(exists)
def compiles():
    """mail.c compiles"""
    check50.c.compile("mail.c", lcs50=True)

@check50.check(compiles)
def cost_of_1_oz_envelope():
    """calculates the cost of a 1 oz large envelope as $1.00"""
    check50.run("./mail").stdin("1").stdout("$1.00", regex=False).exit(0)

@check50.check(compiles)
def cost_of_2_point_5_oz_envelope():
    """calculates the cost of a 2.5 oz large envelope as $1.40"""
    check50.run("./mail").stdin("2.5").stdout("$1.40", regex=False).exit(0)

@check50.check(compiles)
def cost_of_4_point_2_oz_envelope():
    """calculates the cost of a 4.2 oz large envelope as $1.80"""
    check50.run("./mail").stdin("4.2").stdout("$1.80", regex=False).exit(0)

@check50.check(compiles)
def cost_of_12_point_34_oz_envelope():
    """calculates the cost of a 12.34 oz large envelope as $3.40"""
    check50.run("./mail").stdin("12.34").stdout("$3.40", regex=False).exit(0)

@check50.check(compiles)
def cost_of_13_oz_envelope():
    """calculates the cost of a 13 oz large envelope as $3.40"""
    check50.run("./mail").stdin("13").stdout("$3.40", regex=False).exit(0)
