i = 1              # wartość zmiennej i = 1
while i <= 5:      # pętla bedzie wykonywana dopóki i bedzie mniejsze lub równe 5
    print(i)      # drukuje i dopóki jego wartość będzie mniejsza niż 5


    i += 1         # przed dopisaniem tej llinijki pętla drukowałaby 1
                   # w nieskończoność, ponieważ wartość i wynosiła 1
print("Done")



# ta wersja pętli drukuje gwiazdki razy wartość i
i = 1
while i <= 5:
    print(i * "*")
    i += 1  #
print("Done")