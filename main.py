# use numpy for random response
import numpy as np
#parent class Animal
class Animal:
    def __init__(self,animal_name):  self.animal_name = animal_name
    def getName(self):   return self.animal_name
    def sleep(self):     return "This animal sleeps"
    def eat(self):       return "This animal is eating"
    def getType(self):   return "Animal"
    def makeNoise(self): return "This animal making noise"
    def wakeup(self):    return "This animal is wake up"
    def roam(self):      return "This Animal is roaming"
# subclasses of Animal 
class Canine(Animal):
    def roam(self):  return "This Canine is roaming"
    def sleep(self): return "This Canine is sleeping"
    def getspecies(slef): return "Canine";
class Pachyderm(Animal):
    def roam(self):  return "This Pachyderm is roaming"
    def sleep(self): return "This Pachyderm is sleeping"
    def getspecies(self): return "Pachyderm";
class Feline(Animal):
    def roam(self):  return "This Feline is roaming"
    def sleep(self): return "This Feline is sleeping"
    def getspecies(self): return "Feline";
# subclasses of type classes
class cat(Feline):
    def sleep(self): return "This Cat sleeps"
    def roam(self): return "This Cat is roaming"
    def makeNoise(self): return "The Cat makes noise"
    def wakeup(self):return np.random.choice(["Mewwwwww", "This cat is wakeup", "This cat doesn't want to wake up"])   
    def getType(self): return "Cat"
class dog(Canine):
    def roam(self): return "This dog is roaming"
    def makeNoise(self): return "The dog makes noise"
    def getType(self): return "dog"
class elephant(Pachyderm):
    def roam(self): return "This elephant is roaming"
    def makeNoise(self): return "The elephant makes noise"
    def getType(self): return "elephant"
class hippo(Pachyderm):
    def roam(self): return "This hippo is roaming"
    def makeNoise(self): return "The hippo makes noise"
    def getType(self): return "hippo"
class rhino(Pachyderm):
    def roam(self): return "This rhino is roaming"
    def makeNoise(self): return "The rhino makes noise"
    def getType(self): return "rhino"
class lion(Feline):
    def roam(self): return "This lion is roaming"
    def makeNoise(self): return "The lion makes noise"
    def getType(self): return "lion"
class tiger(Feline):
    def roam(self): return "This tiger is roaming"
    def makeNoise(self): return "The tiger makes noise"
    def getType(self): return "tiger"
class wolf(Canine):
    def roam(self): return "This wolf is roaming"
    def makeNoise(self): return "The wolf makes noise"
    def getType(self): return "wolf"   
    
