# артикул, описание и инн поставщ. номенклатурных позиций по части описания (поиск с метасимволами)
def by_description(text):
    return "select Artikul_nomenklaturnoj_pozitsii, Opisanie, INN_kontragenta_postavschika " \
           f"from Nomenklaturnaja_pozitsija where Opisanie like '%{text}%';"


# описание и инн поставщ. номенклатурной позиции по артикулу
def by_code(code):
    return "select Opisanie, INN_kontragenta_postavschika " \
           f"from Nomenklaturnaja_pozitsija where Artikul_nomenklaturnoj_pozitsii = {code};"


# артикулы и описания номенклатурных позиций по инн поставщ.
def by_provider_inn(inn):
    return "select Artikul_nomenklaturnoj_pozitsii, Opisanie " \
           f"from Nomenklaturnaja_pozitsija where INN_kontragenta_postavschika = {inn};"
