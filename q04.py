"""
4. Crie duas funções:
○ A primeira função receberá dois parâmetros e retornará como resultado uma concatenação de texto colocando
uma vírgula entre os dois parâmetros ao uní-los.
○ A segunda função não receberá parâmetros; será feito a leitura de duas entradas que o usuário digitar;
irá chamar a primeira função passando como argumento os dois textos lidos; por fim esta segunda função irá imprimir
para o usuário informando qual foi o resultado que se obteve na chamada à primeira função.
○ Exemplo da primeira entrada: “Olá”. Exemplo da segunda entrada: “Mundo”. Exemplo da saída do sistema: “Olá,Mundo”.
"""

def concatena_textos(primeiro_texto: str, segundo_texto: str):
    return primeiro_texto + ', ' + segundo_texto

def entradas_concatena_textos():
    primeiro_input = input('Informe a primeira palavra: ')
    segundo_input = input('Informe a segunda palavra: ')
    print(concatena_textos(primeiro_input, segundo_input))

entradas_concatena_textos()
