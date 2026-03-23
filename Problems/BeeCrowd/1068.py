
pilha = list()

expressao = input()
expressao += " "

while True:
    try :
        resp = "correct"

        pilha = []
        for dado in expressao:
            tam = len(pilha)

            if dado == "(" or dado == ")":
                if tam == 0 and dado == "(":
                    pilha.append("(")

                elif tam == 0 and dado == ")":
                    resp = "incorrect"
                    break

                elif dado == "(":
                    pilha.append("(")
                
                else:
                    pilha.pop()
        tam = len(pilha)


        if tam > 0:
            resp = "incorrect"
        print(resp)



        expressao = input()
        expressao += " "

    except EOFError:
        break

    