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
def rejects_bad_file():
    """rejects a bad filename entered at the command line with exit code 2"""
    check50.run("./brightness test").exit(2)

@check50.check(compiles)
def calculates_black_as_0():
    """correctly calculates the brightness for black.bmp as 0"""
    check50.run("./brightness black.bmp").stdout("Brightness: 0", regex=False).exit(0)

@check50.check(compiles)
def calculates_blue_as_85():
    """correctly calculates the brightness for blue.bmp as 85"""
    check50.run("./brightness blue.bmp").stdout("Brightness: 85", regex=False).exit(0)

@check50.check(compiles)
def calculates_white_as_255():
    """correctly calculates the brightness for white.bmp as 255"""
    check50.run("./brightness white.bmp").stdout("Brightness: 255", regex=False).exit(0)

@check50.check(compiles)
def calculates_beach_as_168():
    """correctly calculates the brightness for beach.bmp as 168"""
    check50.run("./brightness beach.bmp").stdout("Brightness: 168", regex=False).exit(0)

@check50.check(compiles)
def calculates_dart_as_134():
    """correctly calculates the brightness for dart.bmp as 134"""
    check50.run("./brightness dart.bmp").stdout("Brightness: 134", regex=False).exit(0)
    
@check50.check(compiles)
def calculates_night_as_16():
    """correctly calculates the brightness for night.bmp as 16"""
    check50.run("./brightness night.bmp").stdout("Brightness: 16", regex=False).exit(0)
