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


# наименование, кпп и огрн контрагента по инн 1234567894
# = "select Naimenovanie, KPP, OGRN, Juridicheskij_adres from Kontragent where INN = 1234567894;"

# фио представителя, контактные номер телефона и адрес эл. почты по инн 1234567904
# = "select FIO_predstavitelja, Kontaktnyj_nomer_telefona, Kontaktnyj_adres_elektronnoj_pochty from Kontragent where INN = 1234567904;"

# наименование и инн контрагентов без единого контакта
# = "select Naimenovanie, INN from Kontragent where Kontaktnyj_nomer_telefona is null and Kontaktnyj_adres_elektronnoj_pochty is null;"
