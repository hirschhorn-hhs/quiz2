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
    """decrypts the message Czggj! Ocdn xjgjm: W,u,R"""
    check50.run("./decryption").stdin("Czggj! Ocdn xjgjm: W,u,R").stdout("Hello! This color: B,z,W", regex=False).exit(0)
