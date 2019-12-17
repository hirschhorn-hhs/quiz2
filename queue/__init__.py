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

@check50.check(compiles)
def enqueues_and_prints_one_order_number():
    """enqueues and prints order number 1"""
    from re import match
    expected = "--> Printing all order numbers from oldest to newest.\nOrder #1\n"
    actual = check50.run("./queue").stdin("e").stdin("1").stdin("p").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)
 
@check50.check(compiles)
def enqueues_and_prints_three_order_numbers():
    """enqueues and prints order numbers 1, 2, and 3"""
    from re import match
    expected = "--> Printing all order numbers from oldest to newest.\nOrder #1\nOrder #2\nOrder #3\n"
    actual = check50.run("./queue").stdin("e").stdin("1").stdin("e").stdin("2").stdin("e").stdin("3").stdin("p").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def enqueues_and_prints_fiver_order_numbers():
    """enqueues and prints order numbers 1, 2, 3, 4, 5, and 6"""
    from re import match
    expected = "--> Printing all order numbers from oldest to newest.\nOrder #1\nOrder #2\nOrder #3\nOrder #4\nOrder #5\nOrder #6\n"
    actual = check50.run("./queue").stdin("e").stdin("1").stdin("e").stdin("2").stdin("e").stdin("3").stdin("e").stdin("4").stdin("e").stdin("5").stdin("e").stdin("6").stdin("p").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def enqueues_2_dequeues_1_and_prints():
    """enqueues 2 order numbers, dequeues 1 order number, and then prints"""
    from re import match
    expected = "--> Printing all order numbers from oldest to newest.\nOrder #2\n"
    actual = check50.run("./queue").stdin("e").stdin("1").stdin("e").stdin("2").stdin("d").stdin("p").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def enqueues_2_dequeues_1_enqueues_1_and_prints():
    """enqueues 2 order numbers, dequeues 1 order number, enqueues another order number, and then prints"""
    from re import match
    expected = "--> Printing all order numbers from oldest to newest.\nOrder #2\nOrder #3\n"
    actual = check50.run("./queue").stdin("e").stdin("1").stdin("e").stdin("2").stdin("d").stdin("e").stdin("3").stdin("p").stdout()
    if not match(expected, actual):
        raise check50.Mismatch(expected, actual)
