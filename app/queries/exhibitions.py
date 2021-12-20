# даты проведения выставки по её номеру
def period_by_number(number):
    return "select Data_nachala_provedenija, Data_kontsa_provedenija " \
           f"from Vystavka where Nomer_meroprijatija = {number};"
