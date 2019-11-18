import check50
import check50.c

@check50.check()
def exists():
    """brightness.c exists"""
    check50.exists("brightness.c")

@check50.check(exists)
def compiles():
    """brightness.c compiles"""
    check50.c.compile("brightness.c", lcs50=True)

@check50.check(compiles)
def rejects_0_args():
    """rejects 0 arguments entered at the command line with exit code 1"""
    check50.run("./brightness").exit(1)

@check50.check(compiles)
def rejects_2_args():
    """rejects 2 arguments entered at the command line with exit code 1"""
    check50.run("./brightness").exit(1)

@check50.check(compiles)
def computes_a_as_1():
    """correctly calculates the score for "a" as 1"""
    check50.run("./brightness beach.bmp").stdout("Brightness: 168", regex=False).exit(0)
