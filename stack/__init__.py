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

@check50.check(compiles)
def pushes_and_prints_one_email():
    """pushes and prints email with 'Hello, World' as subject"""
    from re import match
    expected = "--> Printing all emails from newest to oldest.\nHello, World\n"
    actual = check50.run("./stack").stdin("push").stdin("Hello, World").stdin("print").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)
 
@check50.check(compiles)
def pushes_and_prints_three_emails():
    """pushes and prints emails with 'Hello, World', 'Are you there?', and 'Seriously!' as subjects"""
    from re import match
    expected = "--> Printing all emails from newest to oldest.\nSeriously!\nAre you there?\nHello, World\n"
    actual = check50.run("./stack").stdin("push").stdin("Hello, World").stdin("push").stdin("Are you there?").stdin("push").stdin("Seriously!").stdin("print").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def pushes_and_prints_five_emails():
    """pushes and prints emails with 'Hello, World', 'Are you there?', 'Seriously!', 'C'mon...', and ':/' as subjects"""
    from re import match
    expected = "--> Printing all emails from newest to oldest.\n:/\nC'mon...\nSeriously!\nAre you there?\nHello, World\n"
    actual = check50.run("./stack").stdin("push").stdin("Hello, World").stdin("push").stdin("Are you there?").stdin("push").stdin("Seriously!").stdin("push").stdin("C'mon...").stdin("push").stdin(":/").stdin("print").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)
