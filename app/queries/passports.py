# паспортные данные по серии и номеру паспорта
def by_number(number):
    return "select Kod_podrazdelenija, Mesto_rozhdenija, Kem_vydan, Data_vydachi, Pol, Data_rozhdenija," \
           f"Mesto_zhitelstva from Pasportnye_dannye where Serija_i_nomer_pasporta = {number};"
