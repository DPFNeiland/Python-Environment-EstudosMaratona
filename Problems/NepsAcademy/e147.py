

n1 = int(input())
n2 = int(input())

nota = 2*n1 + 3*n2

print(f"{"Aprovado" if nota >= 35 else "Reprovado" if nota < 15 else "Final"}")