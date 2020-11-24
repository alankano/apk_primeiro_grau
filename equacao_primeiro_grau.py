import random

def create_exercicio():
    #c = ax +b
    a = random.randrange(1,6,1)
    b = random.randrange(1,20,1)
    c = random.randrange(1,20,1)
    x = (c - b)/a
    x = round(x,2)
    lista_de_valores = [a,b,c,x]
    return lista_de_valores

def create_alternativas():
    lista_de_valores = create_exercicio()
    a = lista_de_valores[0]
    b = lista_de_valores[1] 
    y = lista_de_valores[2]
    x = lista_de_valores[3]
    lista_de_radios = []
    pergunta = f"Qual o valor de x na equação {y} = {a}x + {b}"
    lista_de_radios.append(x)
    while len(lista_de_radios) < 5:
        alternativa_incorreta = random.uniform(x - 5, x + 5)
        alternativa_incorreta = round(alternativa_incorreta, 2)
        if alternativa_incorreta in lista_de_radios:
            continue
        elif x in lista_de_radios:
            continue
        else:
            lista_de_radios.append(alternativa_incorreta)
    
    random.shuffle(lista_de_radios)

    altenativas_dic = {'lista_de_radios': lista_de_radios,
                       'resposta_correta': x,
                       'pergunta' : pergunta,
                       'lista_de_valores': lista_de_valores
                        }

    return altenativas_dic

def creating_lista_de_exercicios():
    dic_alternativas = {}
    i = 0
    while i < 4:
        dic_alternativas[i] = create_alternativas
        i += 1
    return dic_alternativas



        