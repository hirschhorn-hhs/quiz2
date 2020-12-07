import check50
import check50.c

@check50.check()
def exists():
    """h-index.c exists"""
    check50.exists("h-index.c")

@check50.check(exists)
def compiles():
    """h-index.c compiles"""
    check50.c.compile("h-index.c", lcs50=True)

@check50.check(compiles)
def reprompts_for_bad_input():
    """reprompts the user when an invalid number of papers is entered"""
    check50.run("./h-index").stdin("-1").stdin("0").stdin.("21").reject()
