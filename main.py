infoF = open("USStatesPop.txt", "r")


# Class for creating the state object
class State:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def tostring(self):
        print("State: " + self.name, "Population (In Millions): " + self.population)


# Creating the list of states with their population and printing it
index = 0
stateList = []
for index in range(50):
    index += 1
    stateName = infoF.readline()
    statePop = infoF.readline()
    s1 = State(stateName, statePop)
    stateList.append(s1)
    stateList[index - 1].tostring()
