import check50

@check50.check()
def exists():
    """iowa.py exists"""
    check50.exists("iowa.py")
    check50.include("a.csv", "b.csv", "c.csv", "d.csv")
