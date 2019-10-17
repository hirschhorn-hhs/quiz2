import check50
import check50.c

@check50.check()
def exists():
    """sillystring.c exists."""
    check50.exists("sillystring.c")
    
@check50.check(exists)
def compiles():
    """sillystring.c compiles."""
    check50.c.compile("sillystring.c", lcs50=True)
