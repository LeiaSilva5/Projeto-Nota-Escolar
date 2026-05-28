# Projeto Nota Escolar
# Funoes do sistema f
def verificar_numero(num):
    if 0 < num < 10:
        return True
    else:
        return False

def cadastro_aluno(quant,lista):

    
    for i in range(quant):
        nome = input('Digite o nome do aluno: ').upper()
        if nome.isalpha():
            nota1 = float(input('Digite a primeira nota: '))
            nota2 = float(input('Digite a segunda nota: '))
            nota3 = float(input('Digite a terceira nota: '))
            aluno = {
                'Nome:' : nome,
                'Nota_1' : nota1,
                'Nota_2' : nota2,
                'Nota_3' : nota3
            }
            lista.append(aluno)
        else:
            print('Digite um nome valido')
            continue
        
        return lista

# Código principal
lista_alunos = []
print('Sistema de Notas Escolares')
quantidade = int(input('Digite a quantidade de alunos: ')) 
print(cadastro_aluno(quantidade,lista_alunos))