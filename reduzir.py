from main_stu import lista, produtos, pessoas
from functools import reduce

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_preco = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_preco / len(produtos))

soma_idade = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print(soma_idade / len(pessoas))