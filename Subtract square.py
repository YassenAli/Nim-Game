from random import randint
print("Subtract square game - Take a square num of coins 1,4,9,... - Player who take last coin will win.")
nCoins = randint(30, 200)
turn = 0
while nCoins > 0:
    print(f"We have {nCoins} coins.\nPlayer {turn + 1} turn.")
    n = 0
    while n not in [i * i for i in range(1, nCoins + 1)]:
        n = input("Take some coins: ")
        n = int(n) if n.isdigit() else 0
    if n <= nCoins:
        nCoins -= n
        turn = (turn + 1) % 2
print(f"Platyer {(turn + 1) % 2 + 1} wins.")