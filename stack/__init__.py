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
