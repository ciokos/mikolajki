from random import shuffle
people = ["Wojtke", "Tomke", "Kacpix", "Martusia", "Olcia", "Sylwusia"]
elements = ["ogień", "woda", "ziemia", "powietrze", "światło", "ciemność"]
shuffle(people)
shuffle(elements)
a = people[-1]
santas = people[:]
santas.pop()
santas = [a] + santas
for x, y, z in zip(people, santas, elements):
    file2write = open("santa_files/" + y + ".txt", 'w')
    file2write.write("W tym roku kupujesz prezencik dla: " + x.upper() + " z motywem " + z.upper())
    file2write.close()
