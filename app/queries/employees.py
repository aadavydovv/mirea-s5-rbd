# информация о сотруднике по табельному номеру
def by_number(number):
    return "select Serija_i_nomer_pasporta, FIO, Dolzhnost, Zarplata, Data_najma, Data_uvolnenija, " \
           f"Kontaktnyj_nomer_telefona, Kontaktnyj_adres_elektronnoj_pochty " \
           f"from Sotrudnik where Tabelnyj_nomer = {number};"


# информация об уволенных сотрудниках
def fired():
    return "select Tabelnyj_nomer, Serija_i_nomer_pasporta, FIO, Dolzhnost, Zarplata, Data_najma, Data_uvolnenija, " \
           "Kontaktnyj_nomer_telefona, Kontaktnyj_adres_elektronnoj_pochty " \
           "from Sotrudnik where Data_uvolnenija is not null;"


# поиск сотрудника по фио (поиск с метасимволами)
def by_fio(fio):
    return "select Tabelnyj_nomer, Serija_i_nomer_pasporta, FIO, Dolzhnost, Zarplata, Data_najma, Data_uvolnenija, " \
           f"Kontaktnyj_nomer_telefona, Kontaktnyj_adres_elektronnoj_pochty from Sotrudnik where FIO like '%{fio}%';"


# поиск сотрудников по должности
def by_position(position):
    return "select Tabelnyj_nomer, Serija_i_nomer_pasporta, FIO, Dolzhnost, Zarplata, Data_najma, Data_uvolnenija, " \
           f"Kontaktnyj_nomer_telefona, Kontaktnyj_adres_elektronnoj_pochty " \
           f"from Sotrudnik where Dolzhnost like '%{position}%';"


# действующие сотрудники без единого контакта
# = "select Tabelnyj_nomer, FIO from Sotrudnik where coalesce(Data_uvolnenija, Kontaktnyj_nomer_telefona, Kontaktnyj_adres_elektronnoj_pochty) is null;"
