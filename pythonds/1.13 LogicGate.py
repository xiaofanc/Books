"""
Inheritance is the ability for one class to be related to another class in much the same way that people can be related to one another. Children inherit characteristics from their parents (IS-A Relationship). Similarly, Python child classes can inherit characteristic data and behavior from a parent class. These classes are often referred to as subclasses and superclasses.

construct a simulation, an application to simulate digital circuits including AND, OR and NOT

"""
# parent class
class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

# general class for gates depending on the number of input lines
# The BinaryGate class will be a subclass of LogicGate and will add two input lines.
# The constructors in both of these classes start with an explicit call to the constructor of the parent class using the parent’s __init__ method. 
# Python also has a function called super which can be used in place of explicitly naming the parent class.

class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        # super(UnaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate: " + self.getLabel() + "-->")
        else:
            # get the input of pinA, which is the output of fromgate
            return self.pinA.getFrom().getOutput() 

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    # Now we need to get input from two places: externally, as before, and from the output of a gate that is connected to that input line. 
    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")   
                         
# The UnaryGate class will also subclass LogicGate but will have only a single input line. 
class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self): # get the input
        if self.pin == None:
            return int(input("Enter Pin input for gate: " + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")  

# specific gates that have unique behavior
# the AndGate class will be a subclass of BinaryGate since AND gates have two input lines.
# the AndGate class does not provide any new data since it inherits two input lines, one output line, and a label.
# The only thing AndGate needs to add is the specific behavior that performs the boolean operation.
class AndGate(BinaryGate):
    def __init__(self, n):
        super(AndGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        super(OrGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            return 0
        else:
            return 1

class NotGate(UnaryGate):
    def __init__(self, n):
        super(NotGate, self).__init__(n)

    def performGateLogic(self):
        a = self.getPin()
        if a == 0:
            return 1
        else:
            return 0

"""
In order to create a circuit, we need to connect gates together, the output of one flowing into the input of another. To do this, we will implement a new class called Connector.
HAS-A Relationship (no inheritance)
"""
class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.tgate

if __name__ == '__main__':
    # The outputs from the two AND gates (g1 and g2) are connected to the OR gate (g3) and that output is connected to the NOT gate (g4). The output from the NOT gate is the output of the entire circuit. 

    g1 = AndGate("G1")
    print("andgate: ", g1.getOutput())
    g2 = AndGate("G2")
    print("andgate: ", g2.getOutput())
    g3 = OrGate("G3")
    print("orgate: ", g3.getOutput())
    g4 = NotGate("G4")
    print("notgate: ", g4.getOutput())
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print(g4.getOutput())











    