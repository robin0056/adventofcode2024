### first task

#  store input in list
input = []
with open('input.txt') as text: 
    for line in text: input.append((line.strip()))

# separate columns
spalte_eins = []
spalte_zwei = []

for row in input:
    geteilte_zeile = row.split('   ')
    spalte_eins.append(int(geteilte_zeile[0]))
    spalte_zwei.append(int(geteilte_zeile[1]))

# sort columns
spalte_eins.sort()
spalte_zwei.sort()

# add differences
result_1 = 0

for i in range(1000):
    result_1 = result_1 + abs(spalte_eins[i] - spalte_zwei[i])

print('1:', result_1)


### second task
result_2 = 0

# add up apperance product
for i in range(len(spalte_eins)):
    appearances = 0
    for j in range(len(spalte_zwei)):
        appearances = appearances + (spalte_eins[i] == spalte_zwei[j])
    result_2 = result_2 + appearances * spalte_eins[i]

print('2:', result_2)