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
