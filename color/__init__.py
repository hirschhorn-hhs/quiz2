import check50
import check50.c

@check50.check()
def exists():
    """color.c exists"""
    check50.exists("color.c")

@check50.check(exists)
def compiles():
    """color.c compiles"""
    check50.c.compile("color.c", lcs50=True)

@check50.check(compiles)
def all_three_colors_match:
    """all three colors match"""
    check50.run("./color").stdin("Pink").stdin("Pink").stdin("Pink").stdout("Everyone likes the same color!\n", regex=False).exit(0)
