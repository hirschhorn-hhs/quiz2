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
