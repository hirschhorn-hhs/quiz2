import check50

@check50.check()
def exists():
    """iowa.py exists"""
    check50.exists("iowa.py")

@check50.check(exists)
def rejects_0_args():
    """rejects 0 arguments entered at the command line with exit code 1"""
    check50.run("python3 iowa.py").exit(1)

@check50.check(exists)
def rejects_2_args():
    """rejects 2 arguments entered at the command line with exit code 1"""
    check50.run("python3 iowa.py foo bar").exit(1)

@check50.check(exists)
def rejects_bad_arg():
    """rejects argument that's not a .csv file with exit code 2"""
    check50.run("python3 iowa.py foo").exit(2)

@check50.check(exists)
def first_and_second_do_not_match():
    """first and second round counts do not match"""
    check50.run("python3 iowa.py a.csv").exit(3)

@check50.check(exists)
def interprets_b():
    """correctly interprets the results from County B with 10 county delegates and 1 state delegate"""
    check50.run("python3 iowa.py b.csv").stdin("10").stdin("1").stdout("SDEs for Buttigieg: 0.50\nSDEs for Sanders: 0.50").exit()

@check50.check(exists)
def interprets_c():
    """correctly interprets the results from County C with 20 county delegates and 4 state delegates"""
    check50.run("python3 iowa.py b.csv").stdin("20").stdin("4").stdout("SDEs for Biden: 0.80\nSDEs for Klobuchar: 1.60\nSDEs for Warren: 1.60").exit()

@check50.check(exists)
def interprets_d():
    """correctly interprets the results from County D with 15 county delegates and 3 state delegates"""
    check50.run("python3 iowa.py b.csv").stdin("15").stdin("3").stdout("SDEs for Buttigieg: 1.20\nSDEs for Sanders: 1.00\nSDEs for Warren: 0.80").exit()

@check50.check(exists)
def positive_int_county():
    """only accepts a positive integer from the user for the number of total county delegates"""
    check50.run("python3 iowa.py b.csv").stdin("-10").stdin("10").stdin("1").stdout("SDEs for Buttigieg: 0.50\nSDEs for Sanders: 0.50").exit()

@check50.check(exists)
def positive_int_state():
    """only accepts a positive integer from the user for the number of total state delegates"""
    check50.run("python3 iowa.py b.csv").stdin("10").stdin("0").stdin("1").stdout("SDEs for Buttigieg: 0.50\nSDEs for Sanders: 0.50").exit()
