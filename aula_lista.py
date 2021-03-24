from time import sleep

pessoas = [0, 14, "daniel", "julia", "yasmin", "shuri", 0]

pessoas2 = (0, 14, "daniel", "julia", "yasmin", "shuri", 0)


pessoas[1] = "teste"
pessoas.append("sophia")
pessoas.insert(3, "rafael")
# pessoas.remove("daniel")
# pessoas.pop(3)

num = 0
text = 0

for x in pessoas:
    if type(x) == str:
        text += 1
    elif type(x) == int:
        num += 1

print(num, text)