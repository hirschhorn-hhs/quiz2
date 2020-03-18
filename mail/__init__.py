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
    check50.run("./mail")..stdin("1").stdout("$1.00").exit(0)
