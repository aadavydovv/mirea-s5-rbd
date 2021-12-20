# информация о договоре по его номеру
def by_number(number):
    return "select INN_kontragenta, Tabelnyj_nomer_otvetstvennogo_sotrudnika_menedzhera, Data_nachala_dejstvija, " \
           f"Data_prekraschenija_dejstvija, Tsena from Zakljuchenie_dogovora where Nomer_dogovora = {number};"


# договоры от контрагента с инн N
def by_agent_inn(inn):
    return "select Nomer_dogovora, Tabelnyj_nomer_otvetstvennogo_sotrudnika_menedzhera, Data_nachala_dejstvija, " \
           f"Data_prekraschenija_dejstvija, Tsena from Zakljuchenie_dogovora where INN_kontragenta = {inn};"


# договоры, за которые ответственен сотрудник-менеджер с табельным номером N
def by_manager_number(number):
    return "select Nomer_dogovora, INN_kontragenta, Data_nachala_dejstvija, Data_prekraschenija_dejstvija, Tsena " \
           f"from Zakljuchenie_dogovora where Tabelnyj_nomer_otvetstvennogo_sotrudnika_menedzhera = {number};"
