# номер мероприятия, дата и время продажи, дата посещения, время посещения, количество билетов и тип цены продажи билетов по идентификатору
def by_id(sale_id):
    return "select Nomer_meroprijatija, Data_i_vremja_prodazhi, Data_poseschenija, Vremja_poseschenija, Kolichestvo, " \
           f"Tip_tseny from Prodazha_biletov where Identifikator_prodazhi = {sale_id};"


# идентификатор, дата и время продажи, дата посещения, время посещения, количество билетов и тип цены продажи билетов по номеру мероприятия
def by_event_number(number):
    return "select Identifikator_prodazhi, Data_i_vremja_prodazhi, Data_poseschenija, Vremja_poseschenija," \
           f"Kolichestvo, Tip_tseny from Prodazha_biletov where Nomer_meroprijatija = {number};"


# идентификатор, номер мероприятия, дата посещения, время посещения, количество билетов и тип цены продажи билетов, которые принадлежат временному периоду
# формат: '2021-10-14'
def by_period(dates):
    return "select Identifikator_prodazhi, Nomer_meroprijatija, Data_poseschenija, Vremja_poseschenija, Kolichestvo, " \
           f"Tip_tseny from Prodazha_biletov where Data_i_vremja_prodazhi " \
           f"between convert('{dates[0]}', datetime) and convert('{dates[1]}', datetime);"


# идентификатор, номер мероприятия, время посещения, количество билетов и тип цены продажи билетов по дате посещения
# формат: '2021-10-14'
def by_visit_date(date):
    return "select Identifikator_prodazhi, Nomer_meroprijatija, Vremja_poseschenija, Kolichestvo, Tip_tseny " \
           f"from Prodazha_biletov where Data_poseschenija = convert('{date}', datetime);"


# идентификатор, номер мероприятия, дата и время продажи, дата посещения, время посещения, количество билетов продажи билетов по типу цены
def by_price_type(price_type):
    return "select Identifikator_prodazhi, Nomer_meroprijatija, Data_i_vremja_prodazhi, Data_poseschenija," \
           f"Vremja_poseschenija, Kolichestvo from Prodazha_biletov where Tip_tseny = {price_type};"
