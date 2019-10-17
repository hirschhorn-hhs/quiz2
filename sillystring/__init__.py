import check50
import check50.c

@check50.check()
def exists():
    """sillystring.c exists"""
    check50.exists("sillystring.c")

@check50.check(exists)
def compiles():
    """sillystring.c compiles"""
    check50.c.compile("sillystring.c", lcs50=True)

@check50.check(compiles)
def converts_king_to_kInG():
    """converts king to kInG"""
    check50.run("./sillystring king").stdout("kInG").exit(0)

@check50.check(compiles)
def converts_King_to_KiNg():
    """converts King to KiNg"""
    check50.run("./sillystring King").stdout("KiNg").exit(0)
