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
