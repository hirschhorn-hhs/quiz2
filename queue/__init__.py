import check50
import check50.c

@check50.check()
def exists():
    """queue.c exists"""
    check50.exists("queue.c")

@check50.check(exists)
def compiles():
    """queue.c compiles"""
    check50.c.compile("queue.c", lcs50=True)

@check50.check(compiles)
def raises_error_with_no_order_numbers_1():
    """raises an error when trying to print no order numbers"""
    from re import match
    expected = "--> Printing all order numbers from oldest to newest.\nError: List of order numbers is empty.\n"
    actual = check50.run("./queue").stdin("p").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def raises_error_with_no_order_numbers_2():
    """raises an error when trying to print no order numbers after one enqueue and one dequeue"""
    from re import match
    expected = "--> Printing all order numbers from oldest to newest.\nError: List of order numbers is empty.\n"
    actual = check50.run("./queue").stdin("e").stdin("1").stdin("d").stdin("p").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)
