#!/usr/bin/env python
# coding: utf-8

# In[459]:


import numpy as np
import types

# In[460]:


#Reference
#https://stackoverflow.com/questions/1904351/python-observer-pattern-examples-tips
# define the subject for observer
class Observer():
    _observers = []
    def __init__(self):
        self._observers.append(self)
        self._observables = dict()
    #create observe event
    def register(self, event_name, callback):
        self._observables[event_name] = callback
    #delete observe event
    def unregister(self, event_name):
        del self._observables[event_name]
    #OO get value for two lists
    def get_observers(self):
        return self._observers
    def get_observables(self):
        return self._observables.keys()
#define the event.
class Event():
    def __init__(self,observers, name, data, autofire = True):
        self.name = name
        self.data = data
        self.observers = observers
        if autofire:
            self.fire()      
    def fire(self):
        for observer in self.observers:
            if self.name in observer._observables:
                print("Hi, this is the Zoo Announcer. The Zookeeper is about to {}!".format(self.name))
                observer._observables[self.name](self.data)


# In[461]:


class Animal():
    def __init__(self,animal_name,function = None):  
        #I use strategy pattern on eat method
        #take input as a function
        if function: self.eat = types.MethodType(function, self)
        self.animal_name = animal_name
    def getName(self):   return self.animal_name
    def sleep(self):     return "This animal sleeps"
    def eat(self):       return "This animal is eating"
    def getType(self):   return "Animal"
    def makeNoise(self): return "This animal is making noise"
    def wakeup(self):    return "This animal is wake up"
    def roam(self):      return "This Animal is roaming"


# In[462]:


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


# In[463]:


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


# In[464]:


class Zookeeper(Observer):
    def __init__(self,name):
        self.name = name
        Observer.__init__(self)
    def selfIntroduce(self):
        print("Hi, this is {}. I am the Zookeeper".format(self.name))
    def wakeTheAnimal(self,tmp):
        print("{} wake up {}".format(self.name,tmp.getName()))
    def callAnimal(self,tmp):
        print("{} roll call {}".format(self.name,tmp.getName()))
    def feedAnimal(self,tmp):
        print("{} feed {}".format(self.name,tmp.getName()))
    def closeZoo(self,tmp):
        print("{} let {} go to sleep".format(self.name,tmp.getName()))
    def exercise(self,tmp):
        print("{} train {}".format(self.name,tmp.getName()))


# In[465]:


class Zoo:
    def __init__(self,zookeeper_name):
        self.animals = []
        self.animals_name_list = ["Lily","Liam","Harry","Hulk","David","Dylan","Cathey","Clark","Emily","Eason","Walt","Whiteside","Tom","Tiana","Roy","Richard"]
        for name in self.animals_name_list:
            firstChar = name[0]
            if firstChar == "L":
                self.animals.append(lion(name))
            elif firstChar == "H":
                self.animals.append(hippo(name))
            elif firstChar == "D":
                self.animals.append(dog(name))
            elif firstChar == "C":
                self.animals.append(cat(name))
            elif firstChar == "E":
                self.animals.append(elephant(name))
            elif firstChar == "S":
                self.animals.append(wolf(name))
            elif firstChar == "T":
                self.animals.append(tiger(name))
            elif firstChar == "R":
                self.animals.append(rhino(name))
        self.billy = Zookeeper(zookeeper_name)
    def start_operate(self):
        #register the event that want to observe
        self.billy.register("wake the animal",self.billy.wakeTheAnimal)
        self.billy.register("call the animal",self.billy.callAnimal)
        self.billy.register("feed the animal",self.billy.feedAnimal)
        self.billy.register("close the Zoo",self.billy.closeZoo)
        self.billy.register("exercise the animal",self.billy.exercise)
        self.billy.selfIntroduce()
        #Responsibilities I
        #Polymorphism: Class Animal    * Cat is random response * Lion is oveeride function in class Lion
        print("------------------------------------------")
        print("\n")
        print("Responsibilities 1: wake the animals")
        for idx,animal in enumerate(self.animals):
            #Observe event
            Event(self.billy.get_observers(),"wake the animal",animal)
            print("{} is a {}".format(animal.getName(),animal.getType()))
            print("{}'s species is {}".format(animal.getName(),animal.getspecies()))
            print("{}'s response: {}'".format(animal.getName(),animal.wakeup()))
        print("\n")
        print("------------------------------------------")
        print("\n")
        #Responsibilities II
        #Polymorphism: Class Type of each Animal
        print("Responsibilities 2: roll call the animals")
        for idx,animal in enumerate(self.animals):
            Event(self.billy.get_observers(),"call the animal",animal)
            print("{} is a {}".format(animal.getName(),animal.getType()))
            print("{}'s species is {}".format(animal.getName(),animal.getspecies()))
            print("{}'s response: {}'".format(animal.getName(),animal.makeNoise()))
        print("\n")
        print("------------------------------------------")
        print("\n")        
        #Responsibilities III
        #Polymorphism: Class Animal
        print("Responsibilities 3: feed the animals")
        for idx,animal in enumerate(self.animals):
            Event(self.billy.get_observers(),"feed the animal",animal)
            print("{} is a {}".format(animal.getName(),animal.getType()))
            print("{}'s species is {}".format(animal.getName(),animal.getspecies()))
            print("{}'s response: {}'".format(animal.getName(),animal.eat()))
        print("\n")
        print("------------------------------------------")
        print("\n")        
        #Responsibilities IV
        #Polymorphism: Class Animal
        print("Responsibilities 4: exercise the animals")
        for idx,animal in enumerate(self.animals):
            Event(self.billy.get_observers(),"exercise the animal",animal)
            print("{} is a {}".format(animal.getName(),animal.getType()))
            print("{}'s species is {}".format(animal.getName(),animal.getspecies()))
            print("{}'s response: {}'".format(animal.getName(),animal.roam()))
        print("\n")
        print("------------------------------------------")
        print("\n") 
        #Responsibilities V
        #Responsibilities V
        #Polymorphism: Class Species of each AnimalPolymorphism: Class Species of each Animal
        print("Responsibilities 5: shut down the Zoo")
        for idx,animal in enumerate(self.animals):
            Event(self.billy.get_observers(),"close the Zoo",animal)
            print("{} is a {}".format(animal.getName(),animal.getType()))
            print("{}'s species is {}".format(animal.getName(),animal.getspecies()))
            print("{}'s response: {}'".format(animal.getName(),animal.sleep()))
        print("\n")
        print("------------------------------------------")
        print("\n") 
        for event in ["wake the animal","call the animal","feed the animal","close the Zoo","exercise the animal"]:
            self.billy.unregister(event)


# In[466]:


test = Zoo("Billy")


# In[467]:


test.start_operate()


# In[ ]:





# In[ ]:




