# наименование мероприятия по номеру
def by_number(number):
    return f"select Naimenovanie from Meroprijatie where Nomer_meroprijatija = {number};"


# цены посещения мероприятий по названию (поиск с метасимволами)
def by_name(name):
    return "select Naimenovanie, Standartnaja_tsena_poseschenija, Lgotnaja_tsena_poseschenija " \
           f"from Meroprijatie where Naimenovanie like '%{name}%';"


# выставки со стандартной ценой посещения меньше чем N
def by_standard_price_cap(cap):
    return f"select Naimenovanie from Meroprijatie where Tip = 0 and Standartnaja_tsena_poseschenija < {cap};"


# номер и наименование мероприятия по табельному номеру сотрудника-куратора
def by_curator_number(number):
    return f"select Nomer_meroprijatija, Naimenovanie " \
           f"from Meroprijatie where Tabelnyj_nomer_sotrudnika_kuratora = {number};"


# наименования мероприятий по типу (0 - выставка, 1 - экскурсия)
# = "select Naimenovanie from Meroprijatie where Tip = 1;"
