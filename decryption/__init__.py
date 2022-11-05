import check50
import check50.c

@check50.check()
def exists():
    """decryption.c exists"""
    check50.exists("decryption.c")

@check50.check(exists)
def compiles():
    """decryption.c compiles"""
    check50.c.compile("decryption.c", lcs50=True)

@check50.check(compiles)
def decrypt_message():
    """decrypts the message Fg, dpgclb! Ucyp rfgq amjmp qfgpr: 8-B"""
    check50.run("./decryption").stdin("Fg, dpgclb! Ucyp rfgq amjmp qfgpr: 8-B").stdout("Hi, friend! Wear this color shirt: 8-D", regex=False).exit(0)
