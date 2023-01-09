def resposta():
    #Captura a resposta do usuario e preprocessando-a
    resp = input(">: ")
    resp = resp.lower()
    resp = resp.replace('eh', 'é')
    return resp
def pegaNome(nome):
    if 'meu nome é ' in nome:
        nome = nome[11:]

    nome = nome.title()
    return nome
def respondeNome(nome):
    conhecidos = ['Lucas', 'Alberto', 'Paula']

    frase = 'É um prazer conhecer você '
    for conhecido in conhecidos:
        if nome == conhecido:
            frase = 'Olá mestre '

    return frase+nome+'!'
