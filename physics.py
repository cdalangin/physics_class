train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp): #converts F to C
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100) #test
print(f100_in_celsius)

def c_to_f(c_temp): #converts C to F
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0) #test
print(c0_in_fahrenheit)

def get_force(mass, acceleration): #solves for force
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration) #test
print(train_force)

print("The GE train supplies " + str(train_force) + " Newtons of force.") #makes sentence

def get_energy(mass, c = 3*10**8): #finds energy
  return mass*c*c #8

bomb_energy = get_energy(bomb_mass) #solves for energy using bomb mass
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.") #sentence

def get_work(mass, acceleration, distance): #solves for work
  return train_force * distance

train_work = get_work(train_mass, train_acceleration, train_distance) #solves for work of a train
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.") #13
