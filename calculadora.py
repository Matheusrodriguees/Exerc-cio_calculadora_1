def potencia (a, b):
  return a ** b

def divisao (a, b):
  return a // b

def multiplicacao (a, b):
  return a * b

def subtracao (a, b):
  pass

def soma (a, b):
  return a + b

a = int(input("Digite o primeiro valor"))
b = int(input ("Digite o segundo valor"))

operacao = input("+: Soma\n-: Subtração\n*: Multiplicação\n/: Divisão\n**: Exponenciação")
if operacao == '+':
  resultado = soma(a, b)
elif operacao == '-':
  resultado = a - b
elif operacao == '*':
  resultado = multiplicacao(a, b)
elif operacao == '/':
  resultado = a // b
else:
  resultado = a ** b
print (resultado)