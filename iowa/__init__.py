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
