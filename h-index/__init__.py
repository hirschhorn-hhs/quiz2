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
    check50.run("./h-index").stdin("-1").stdin("0").stdin("21").reject()

@check50.check(compiles)
def h_index_0():
    """correctly calcualtes an h-index of 0 for 1 paper with 0 citations"""
    check50.run("./h-index").stdin("1").stdin("Paper 1").stdin("0").stdout("H-index: 0", regex=False).exit(0)

@check50.check(compiles)
def h_index_1():
    """correctly calcualtes an h-index of 1 for 1 paper with 1 citation"""
    check50.run("./h-index").stdin("1").stdin("Paper 1").stdin("1").stdout("H-index: 1", regex=False).exit(0)

@check50.check(compiles)
def h_index_2():
    """correctly calcualtes an h-index of 1 for 1 paper with 2 citations"""
    check50.run("./h-index").stdin("1").stdin("Paper 1").stdin("2").stdout("H-index: 1", regex=False).exit(0)

@check50.check(compiles)
def h_index_3():
    """correctly calcualtes an h-index of 7 for 10 papers"""
    check50.run("./h-index").stdin("10").stdin("Paper 1").stdin("50").stdin("Paper 2").stdin("40").stdin("Paper 3").stdin("33").stdin("Paper 4").stdin("23").stdin("Paper 5").stdin("12").stdin("Paper 6").stdin("11").stdin("Paper 7").stdin("8").stdin("Paper 8").stdin("5").stdin("Paper 9").stdin("1").stdin("Paper 10").stdin("0").stdout("H-index: 7", regex=False).exit(0)

@check50.check(compiles)
def h_index_0_bonus():
    """[bonus] correctly sorts then calcualtes an h-index of 1 for 3 papers"""
    check50.run("./h-index").stdin("3").stdin("Paper 1").stdin("0").stdin("Paper 2").stdin("1").stdin("Paper 3").stdin("20").stdout("H-index: 1", regex=False).exit(0)

@check50.check(compiles)
def h_index_1_bonus():
    """[bonus] correctly sorts then calcualtes an h-index of 2 for 3 papers"""
    check50.run("./h-index").stdin("3").stdin("Paper 1").stdin("2").stdin("Paper 2").stdin("1").stdin("Paper 3").stdin("20").stdout("H-index: 2", regex=False).exit(0)

@check50.check(compiles)
def h_index_2_bonus():
    """[bonus] correctly sorts then calcualtes an h-index of 3 for 5 papers"""
    check50.run("./h-index").stdin("5").stdin("Paper 1").stdin("2").stdin("Paper 2").stdin("20").stdin("Paper 3").stdin("1").stdin("Paper 4").stdin("5").stdin("Paper 5").stdin("10").stdout("H-index: 3", regex=False).exit(0)
