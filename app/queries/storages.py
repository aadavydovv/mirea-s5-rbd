# номера хранилищ, за которые ответственен сотрудник-хранитель с табельным номером 29
def by_curator_number(number):
    return f"select Nomer_hranilischa " \
           f"from Hranilische where Tabelnyj_nomer_otvetstvennogo_sotrudnika_hranitelja = {number};"
