# наименования коллекций в хранилище N
def by_storage(number):
    return f"select Naimenovanie from Kollektsija where Nomer_otvedennogo_hranilischa = {number};"
