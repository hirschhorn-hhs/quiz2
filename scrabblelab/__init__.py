import check50
import check50.c

@check50.check()
def exists():
    """scrabble.c exists"""
    check50.exists("scrabble.c")

@check50.check(exists)
def compiles():
    """scrabble.c compiles"""
    check50.c.compile("scrabble.c", lcs50=True)

@check50.check(compiles)
def test0():
    """handles letter cases correctly"""
    check50.run("./scrabble").stdin("LETTERCASE").stdin("lettercase").stdout("Tie!", regex=False).exit(0)

@check50.check(compiles)
def test1():
    """handles punctuation correctly"""
    check50.run("./scrabble").stdin("Punctuation!?!?").stdin("punctuation").stdout("Tie!", regex=False).exit(0)

@check50.check(compiles)
def test2():
    """correctly identifies Question? and Question! as a tie"""
    check50.run("./scrabble").stdin("Question?").stdin("Question!").stdout("Tie!", regex=False).exit(0)

@check50.check(compiles)
def test3():
    """correctly identifies hai! as winner over Oh,"""
    check50.run("./scrabble").stdin("Oh,").stdin("hai!").stdout("Player 2 wins!", regex=False).exit(0)

@check50.check(compiles)
def test4():
    """correctly identifies COMPUTER as winner over science"""
    check50.run("./scrabble").stdin("COMPUTER").stdin("science").stdout("Player 1 wins!", regex=False).exit(0)

@check50.check(compiles)
def test5():
    """correctly identifies Scrabble as winner over wiNNeR"""
    check50.run("./scrabble").stdin("Scrabble").stdin("wiNNeR").stdout("Player 1 wins!", regex=False).exit(0)

@check50.check(compiles)
def test6():
    """correctly identifies Skating! as winner over figure?"""
    check50.run("./scrabble").stdin("figure?").stdin("Skating!").stdout("Player 2 wins!", regex=False).exit(0)
