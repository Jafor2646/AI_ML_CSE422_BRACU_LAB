import random

#Part 1
def fitness_function(lst, n ,t):
  penalty = 0
  l = n*t
  for i in range(t):
    count = 0
    j = t*i
    while j<n*(i+1):
      if lst[j] == 1:
        count += 1
      j+=1
    penalty += abs(count-1)
  temp = l // n
  for i in range(n):
    count = 0
    j = i
    while j < l:
      if(lst[j] == 1):
        count += 1
      j = j + temp
    penalty += abs(count - 1)
  return -penalty
    



def initial_populated_func(initial_population, length):
  
  for count in range(10):
    temp = []
    for i in range(length):
      num = random.randint(0, 1)
      temp.append(num)
    initial_population.append(temp)

def random_selection_crossover():
  idx = random.randint(0, 9)
  idx2 = idx
  while idx == idx2:
    idx2 = random.randint(0, 9)
  return (idx, idx2)
def crossover(lst1, lst2):
  idx = random.randint(1, len(lst1)-1)
  new_list1 = lst1[:idx] + lst2[idx:]
  new_list2 = lst2[:idx] + lst1[idx:]
  return (new_list1, new_list2)


def mutation(lst1, lst2):
  flag = random.randint(0,100)
  if(flag > 50 and flag <=100):
    idx = random.randint(0, len(lst1)-1)
    digit = random.randint(0, 1)
    lst1[idx] = digit
    idx = random.randint(0, len(lst2) - 1)
    digit = random.randint(0, 1)
    lst2[idx] = digit



#Driver code started
inp = open("input.txt", "r")

out = open("output.txt", "w")
initial_population = []
n, t =  list(map(int, inp.readline().split())) 

initial_populated_func(initial_population, n*t)

population = []
ans = None
penalty = 0



for run in range(100):
  if(len(population) == 20):
    initial_population = []
    fitness = {}
    for i in range(len(population)):
      pen = fitness_function(population[i], n, t)
      if(pen in fitness.keys()):
        fitness[pen].append(population[i])
      else:
        fitness[pen] = []
        fitness[pen].append(population[i])
      
    sorted_fitness = {k:fitness[k] for k in sorted(fitness.keys(), reverse=True)}
    for k, value in sorted_fitness.items():
      for v in value:
        initial_population.append(v)
        if(len(initial_population) == 10):
          break
    if(run != 99):
      population = []
  idx1, idx2 = random_selection_crossover()
  penalty = fitness_function(initial_population[idx1], n, t)
  if( penalty == 0):
    ans = initial_population[idx1]
    break
  penalty = fitness_function(initial_population[idx2], n, t)
  if(penalty == 0):
    ans = initial_population[idx2]
    break
  lst1, lst2 = crossover(initial_population[idx1], initial_population[idx2])
  
  mutation(lst1, lst2)
  penalty = fitness_function(lst1, n, t)
  if(penalty == 0):
    ans = lst1
    break
  penalty = fitness_function(lst2, n, t)
  if(penalty == 0):
    ans = lst2
    break
  
  population.append(lst1)
  population.append(lst2)
out.write("Part 1\n")
if ans == None:
  pen = fitness_function(population[0], n, t)
  lst = population[0]
  for i in range(1, len(population)):
    p = fitness_function(population[i], n, t)
    if p > pen:
      pen = p
      lst = population[i]
  res = ""
  for i in lst:
    res += str(i)
  out.write(res+"\n")
  out.write(str(pen))
else:
  res = ""
  for i in ans:
    res += str(i)
  out.write(res+"\n")
  out.write(str(penalty))

#Part 2
out.write("\n\n\nPart 2\n")

idx1 , idx2 = random_selection_crossover()

lst1 = initial_population[idx1]
lst2 = initial_population[idx2]

first_point = random.randint(1, len(lst1)-2)
second_point = random.randint(first_point+1, len(lst1)-1)
first_offspring = 0
second_offspring = 0
if second_point == len(lst1)-1:
  first_offspring = lst1[:first_point+1] + lst2[first_point+1: second_point+1]
  second_offspring = lst2[:first_point+1] + lst1[first_point+1: second_point+1]
else:
  first_offspring = lst1[:first_point+1] + lst2[first_point+1: second_point+1] + lst1[second_point+1: ]
  second_offspring = lst2[:first_point+1] + lst1[first_point+1: second_point+1] + lst2[second_point+1: ]
fo = ""
for i in first_offspring:
  fo+=str(i)
so = ""
for i in second_offspring:
  so+=str(i)
out.write("first offspring: "+fo+"\n")
out.write("Second offspring: "+ so + "\n")

#Part 3

number_of_population = random.randint(1, len(initial_population))

tournament = random.sample(initial_population, number_of_population)

m = fitness_function(tournament[0], n, t)
lst = tournament[0]

for i in range(1, len(tournament)):
  temp = fitness_function(tournament[i],n ,t)
  if temp > m:
    m = temp
    lst = tournament[i]

out.write("\n\nPart 3\n")


selected = ""
for i in lst:
  selected+=str(i)
out.write("Selected: "+selected+"\n")
out.write("Penalty: "+str(m))