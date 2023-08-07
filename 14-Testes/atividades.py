def comer(comida, saudavel):
    if saudavel:
        return f'Estou comendo {comida} porque quero manter a forma'
    else:
        return f"Estou comendo {comida} porque a gente só vive uma vez"


def dormir(num_horas):
    return f"Continuo cansado após dormir {num_horas} horas" if num_horas <= 8 else "Dormi muito"
    # if num_horas <= 4:
    #     return f"Continuo cansado após dormir {num_horas} horas"
    # else:
    #     return "Dormi muito"


def engracado(pessoa):
    comediantes = ["Jim Carrey", "Bozo"]
    if pessoa in comediantes:
        return True
    return False
