# номера экскурсий (мероприятий) на определённом языке
def by_language(language):
    return f"select Nomer_meroprijatija from Ekskursija where Jazyk = '{language}';"


# номера экскурсий (мероприятий), рассчитанные на более, чем N человек (или для N)
def by_max_amount_of_participants(amount):
    return f"select Nomer_meroprijatija from Ekskursija where Maksimalnoe_kolichestvo_chelovek >= {amount};"
