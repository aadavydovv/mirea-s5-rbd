# информация о контрагенте по инн
def by_inn(inn):
    return "select Tabelnyj_nomer_otvetstvennogo_sotrudnika_menedzhera, Naimenovanie, KPP, OGRN, FIO_predstavitelja, " \
           "Juridicheskij_adres, Kontaktnyj_nomer_telefona, Kontaktnyj_adres_elektronnoj_pochty " \
           f"from Kontragent where INN = {inn}"


# информация о контрагентах, за которые ответственен сотрудник-менеджер с табельным номером N
def by_employee_number(number):
    return "select INN, Naimenovanie, KPP, OGRN, FIO_predstavitelja, " \
           "Juridicheskij_adres, Kontaktnyj_nomer_telefona, Kontaktnyj_adres_elektronnoj_pochty " \
           f"from Kontragent where Tabelnyj_nomer_otvetstvennogo_sotrudnika_menedzhera = {number}"
