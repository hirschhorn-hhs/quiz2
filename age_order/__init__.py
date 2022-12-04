import check50
import check50.c

@check50.check()
def exists():
    """age_order.c exists"""
    check50.exists("age_order.c")

@check50.check(exists)
def compiles():
    """age_order.c compiles"""
    check50.c.compile("age_order.c", lcs50=True)

@check50.check(compiles)
def years_diff_months_match_days_match():
    """correctly sorts students when only years are different"""
    check50.run("./age_order").stdin("4").stdin("Simon").stdin("1").stdin("1").stdin("2003").stdin("Lyra").stdin("1").stdin("1").stdin("2005").stdin("Olivia").stdin("1").stdin("1").stdin("2004").stdin("Audrey").stdin("1").stdin("1").stdin("2006").stdout("Simon\nOlivia\nLyra\nAudrey\n", regex=False)

@check50.check(compiles)
def years_match_months_diff_days_match():
    """correctly sorts students when only months are different"""
    check50.run("./age_order").stdin("4").stdin("Simon").stdin("3").stdin("1").stdin("2005").stdin("Lyra").stdin("2").stdin("1").stdin("2005").stdin("Olivia").stdin("5").stdin("1").stdin("2005").stdin("Audrey").stdin("7").stdin("1").stdin("2005").stdout("Lyra\nSimon\nOlivia\nAudrey\n", regex=False)

@check50.check(compiles)
def years_match_months_match_days_diff():
    """correctly sorts students when only days are different"""
    check50.run("./age_order").stdin("4").stdin("Simon").stdin("1").stdin("23").stdin("2005").stdin("Lyra").stdin("1").stdin("12").stdin("2005").stdin("Olivia").stdin("1").stdin("19").stdin("2005").stdin("Audrey").stdin("1").stdin("3").stdin("2005").stdout("Audrey\nLyra\nOlivia\nSimon\n", regex=False)
    
@check50.check(compiles)
def not_all_match():
    """correctly sorts students when a lot of things are different"""
    check50.run("./age_order").stdin("8").stdin("Simon").stdin("3").stdin("3").stdin("2005").stdin("Lyra").stdin("2").stdin("4").stdin("2005").stdin("Olivia").stdin("5").stdin("19").stdin("2004").stdin("Audrey").stdin("8").stdin("14").stdin("2003").stdin("Adam").stdin("2").stdin("1").stdin("2005").stdin("Lauren").stdin("5").stdin("17").stdin("2004").stdin("Sarah").stdin("2").stdin("18").stdin("2005").stdin("Margaret").stdin("6").stdin("14").stdin("2003").stdout("Margaret\nAudrey\nLauren\nOlivia\nAdam\nLyra\nSarah\nSimon\n", regex=False)
