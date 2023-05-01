n = 0
while n < 5:
    n += 1  # inkrementuj n z każdym obiegiem pętli
    if n == 4:  # jeżeli n wynosi 4, zakoncz petle
        break
    if n == 1:  # jezeli n wynosi 1, rozpocznij nowa iteracje, nie wydrukuje się n == 1 tylko
        continue
    print(n)
