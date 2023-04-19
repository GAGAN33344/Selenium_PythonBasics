a = 4

if a < 2:
    print("Condition Matches")
else:
    print("Condition not Matches")
print("if else condition code is completed")

# For Loop
print("*****ForLoop********")
obj = [2, 3, 4, 5, 6, 7, 8, 9]
for i in obj:
    print(i*2)

# sum of five first natural numbers 1+2+3+4+5 = 15
print("*****Sum Of First Five Natural Numbers********")
summation = 0
for j in range(1, 6): #range(i,j) -> Iterate i to j-1
    summation = summation + j
print(summation)

print("*****Print First Ten Natural Numbers Jump By Two Indexs********") # 1,3,5,7,9
for k in range(1, 11, 2):
    print(k)

print("*****Skipping First Index********") # 0,1,2,3,4,5
for m in range(6):
    print(m)

print("*****While Loops******")
it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue # It would skip current Iteration
    if it == 4: # It shouldn't allow to print 3 on console
        break
    print(it)
    it = it - 1






