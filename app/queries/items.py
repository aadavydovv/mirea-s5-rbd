# артикулы, наименования и век музейных предметов по номеру коллекции, расположенные в порядке убывания века
def by_collection_number(number):
    return "select Artikul_muzejnogo_predmeta, Naimenovanie, Vek, Vysota_v_millimetrah, Shirina_v_millimetrah, " \
           f"Dlina_v_millimetrah from Muzejnyj_predmet where Nomer_kollektsii = {number} order by Vek desc;"


# артикулы и наименования музейных предметов по части наименования (поиск с метасимволами)
def by_name(name):
    return "select Artikul_muzejnogo_predmeta, Naimenovanie " \
           f"from Muzejnyj_predmet where Naimenovanie like '%{name}%';"


# описание музейного предмета по артикулу
def by_code(code):
    return "select Opisanie, Ves_v_grammah, Vysota_v_millimetrah, Shirina_v_millimetrah, Dlina_v_millimetrah " \
           f"from Muzejnyj_predmet where Artikul_muzejnogo_predmeta = {code};"


# артикулы и наименования музейных предметов по типу
def by_type(item_type):
    return f"select Artikul_muzejnogo_predmeta, Naimenovanie from Muzejnyj_predmet where Tip = '{item_type}';"


# артикулы и наименования музейных предметов, которые весят больше, чем N грамм
def by_minimum_weight(weight):
    return f"select Artikul_muzejnogo_predmeta, Naimenovanie from Muzejnyj_predmet where Ves_v_grammah > {weight};"


# артикулы и наименования музейных предметов, которые датированы периодом в годах
def by_period(years):
    return f"select Artikul_muzejnogo_predmeta, Naimenovanie " \
           f"from Muzejnyj_predmet where God between {years[0]} and {years[1]};"


# артикулы и наименования музейных предметов без года
def without_year():
    return "select Artikul_muzejnogo_predmeta, Naimenovanie from Muzejnyj_predmet where God is null"


# вес, высота, ширина и длина музейного предмета по артикулу
# = "select Ves_v_grammah, Vysota_v_millimetrah, Shirina_v_millimetrah, Dlina_v_millimetrah from Muzejnyj_predmet where Artikul_muzejnogo_predmeta = 3;"

# высота, ширина и длина каждого музейного предмета в коллекции по номеру N
# = "select Vysota_v_millimetrah, Shirina_v_millimetrah, Dlina_v_millimetrah from Muzejnyj_predmet where Nomer_kollektsii = 4;"
