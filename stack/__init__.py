import check50
import check50.c

@check50.check()
def exists():
    """stack.c exists"""
    check50.exists("stack.c")

@check50.check(exists)
def compiles():
    """stack.c compiles"""
    check50.c.compile("stack.c", lcs50=True)

@check50.check(compiles)
def pushes_and_prints_one_email():
    """pushes and prints Hello, World email"""
    check50.run("./stack").stdin("push").stdin("Hello, World").stdin("print").stdout("\n-> Printing all emails from newest to oldest.\nHello, World\nWhat would you like to do? (push, pop, print, quit) ")
