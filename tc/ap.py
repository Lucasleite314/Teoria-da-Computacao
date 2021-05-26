

def delta(automato, estado, simbolo, pilha):
    try:
        novo_estado, nova_pilha = automato[3][(estado, simbolo, pilha)]
        return novo_estado, nova_pilha
    except:
        return (None,None)

#52 Transformação GLC para AP (Lucas Leite) 

	class Transformar:
    simbolo = ''
    estado = ''
    novo_estado = ''
    desempilharSimbolo = ''
    empilharSimbolo = []
    
    def __init__(self, simbolo, estado, novo_estado, desempilharSimbolo, empilharSimbolo):
        self.simbolo = simbolo
        self.estado = estado
        self.novo_estado = novo_estado
        self.desempilharSimbolo = desempilharSimbolo
        self.empilharSimbolo = empilharSimbolo
    
    def addEmpilharSimbolo(self, sym):
        self.empilharSimbolo.add(sym)
    
    def __str__(self):
        empilharString = ''.join(self.empilharSimbolo)
        string = self.simbolo + ", " + self.desempilharSimbolo + ", " + empilharString 
        return string