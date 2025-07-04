def validar_senha(senha):
  numeros = "1234567890"
  tem = False
  ap1 = False
  ap2 = False
  ap3 = False
  ap4 = False
  if len(senha) >= 8:
    print("Comprimento mínimo de 8 caracteres: OK")
    ap1 = True
  if len(senha) < 8:
    print("Comprimento mínimo de 8 caracteres: NÃO")

  if senha != senha.lower():
        print("Pelo menos uma letra maiúscula: OK")
        ap2 = True
  if senha == senha.lower():
         print("Pelo menos uma letra maiúscula: NÃO")
  if senha != senha.upper():
       print("Pelo menos uma letra minúscula: OK")
       ap3 = True
  if senha == senha.upper():
         print("Pelo menos uma letra minúscula: NÃO")
  for i in numeros:
    if i in senha:
         tem = True
         break

  if tem:
    print("Pelo menos um número: OK")
    ap4 = True
  if not tem:
      print("Pelo menos um número: NÃO")
  if ap1 and ap2 and ap3 and ap4:
    print("Senha forte!")
  if not ap1 or not ap2 or not ap3 or not ap4:
    print("Senha Fraca!")


senha = input()
validar_senha(senha)