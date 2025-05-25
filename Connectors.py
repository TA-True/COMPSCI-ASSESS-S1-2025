class LogicGate:

    def __init__(self,n, name):
        self.label = n
        self.output = None
        self.name = name
    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    
class BinaryGate(LogicGate):

    def __init__(self,n, name):
        LogicGate.__init__(self,n, name)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
class UnaryGate(LogicGate):

    def __init__(self,n, name):
        LogicGate.__init__(self,n, name)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))
    
class AndGate(BinaryGate):

    def __init__(self,n, name):
        super(AndGate,self).__init__(n, name)
    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")
        
    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate " + self.getLabel()+"-->")
        else:
            return self.pinA.getFrom().getOutput()
    def getPinB(self):
        if self.pinB == None:
            return input("Enter Pin B input for gate " + self.getLabel()+"-->")
        else:
            return self.pinB.getFrom().getOutput()
    def performGateLogic(self):

        a = self.getPinA()
        print(str(self.name)+" inputs " + str(a) )
        b = self.getPinB()
        print(str(self.name)+" inputs " + str(b) )
        if a!=0 and b!=0:
            print(str(self.name)+" outputs On" )
            return 1
        elif a != 0:
            print("a is working")
        elif b != 0:
            print("b is working")
        else:
            print(str(self.name)+" outputs Off" )
            return 0
class NandGate(BinaryGate):

    def __init__(self,n, name):
        super(AndGate,self).__init__(n, name)
    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")
        
    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate " + self.getLabel()+"-->")
        else:
            return self.pinA.getFrom().getOutput()
    def getPinB(self):
        if self.pinB == None:
            return input("Enter Pin B input for gate " + self.getLabel()+"-->")
        else:
            return self.pinB.getFrom().getOutput()
    def performGateLogic(self):

        a = self.getPinA()
        print(str(self.name)+" inputs " + str(a) )
        b = self.getPinB()
        print(str(self.name)+" inputs " + str(b) )
        if a==1 and b==1:
            print(str(self.name)+" outputs off")
            return 0
        else:
            print(str(self.name)+" outputs on")
            return 1
class NotGate(UnaryGate):

    def __init__(self,n, name):
        super(NotGate,self).__init__(n, name)
    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")
        
    def getPin(self):
        if self.pin == None:
            return input("Enter Pin A input for gate " + self.getLabel()+"-->")
        else:
            return self.pin.getFrom().getOutput()
    def performGateLogic(self):

        a = self.getPin()
        if a==0:
            print(self.name + " has inversed the value to 1")
            return 1
        else:
            print(self.name + " has inversed the value to 0")
            return 0
class NorGate(BinaryGate):

    def __init__(self,n, name):
        super(OrGate,self).__init__(n, name)
    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")
        
    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate " + self.getLabel()+"-->")
        else:
            return self.pinA.getFrom().getOutput()
    def getPinB(self):
        if self.pinB == None:
            return input("Enter Pin B input for gate " + self.getLabel()+"-->")
        else:
            return self.pinB.getFrom().getOutput()
    def performGateLogic(self):

        a = self.getPinA()
        print(str(self.name)+" inputs " + str(a) )
        b = self.getPinB()
        print(str(self.name)+" inputs " + str(b) )
        if a==1 or b==1:
            print(str(self.name)+" outputs off")
            return 0
        else:
            print(str(self.name)+" outputs on")
            return 1
class flippityfloppity:
    def __init__(self, name):
        self.q = 0
        self.j = 0
        self.k = 0
        self.name = name
    def flipflop(self, input1, input2):
        self.k = input1
        self.j = input2
        if self.q == 0:#State A?
            if self.j == 1:#Check if J is on
               self.q = 1#If so flip to one
        else:#if state B
            if self.k == 1:#Check if K is on
                self.q = 0
        return self.q

class OrGate(BinaryGate):

    def __init__(self,n, name):
        super(OrGate,self).__init__(n, name)
    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")
        
    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate " + self.getLabel()+"-->")
        else:
            return self.pinA.getFrom().getOutput()
    def getPinB(self):
        if self.pinB == None:
            return input("Enter Pin B input for gate " + self.getLabel()+"-->")
        else:
            return self.pinB.getFrom().getOutput()
    def performGateLogic(self):

        a = self.getPinA()
        print(str(self.name)+" inputs " + str(a) )
        b = self.getPinB()
        print(str(self.name)+" inputs " + str(b) )
        if a==1 or b==1:
            print(str(self.name)+" outputs on")
            return 1
        else:
            print(str(self.name)+" outputs off")
            return 0
class XorGate(BinaryGate):

    def __init__(self,n, name):
        super(OrGate,self).__init__(n, name)
    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")
        
    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate " + self.getLabel()+"-->")
        else:
            return self.pinA.getFrom().getOutput()
    def getPinB(self):
        if self.pinB == None:
            return input("Enter Pin B input for gate " + self.getLabel()+"-->")
        else:
            return self.pinB.getFrom().getOutput()
    def performGateLogic(self):

        a = self.getPinA()
        print(str(self.name)+" inputs " + str(a) )
        b = self.getPinB()
        print(str(self.name)+" inputs " + str(b) )
        if a==1 or b==1:
            if a == 0 and b == 0:
                print(str(self.name)+" outputs off")
                return 0
            else:
                print(str(self.name)+" outputs on")
                return 1
        else:
            print(str(self.name)+" outputs off")
            return 0 
class XnorGate(BinaryGate):

    def __init__(self,n, name):
        super(OrGate,self).__init__(n, name)
    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")
        
    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate " + self.getLabel()+"-->")
        else:
            return self.pinA.getFrom().getOutput()
    def getPinB(self):
        if self.pinB == None:
            return input("Enter Pin B input for gate " + self.getLabel()+"-->")
        else:
            return self.pinB.getFrom().getOutput()
    def performGateLogic(self):

        a = self.getPinA()
        print(str(self.name)+" inputs " + str(a) )
        b = self.getPinB()
        print(str(self.name)+" inputs " + str(b) )
        if a==1 or b==1:
            if a == 0 and b == 0:
                print(str(self.name)+" outputs on")
                return 1
            else:
                print(str(self.name)+" outputs off")
                return 0
        else:
            print(str(self.name)+" outputs on")
            return 1
                
class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
#g1 = AndGate("G1")#gives 1 if all otherwise 0
#print(g1.getOutput())
#g2 = OrGate("G2")#gives 1 if either 0 if neither
#print(g2.getOutput())
#g3 = NotGate("G3")#gives opposite answer
#print(g3.getOutput())
g1 = AndGate("G1", "Uno")
g2 = AndGate("G2", "Dos")
g3 = OrGate("G3", "Tres")
g4 = NotGate("G4", "Four")
c1 = Connector(g1,g3)#working properly
c2 = Connector(g2,g3)#working in the wrong way when c1 is on, hmmm
c3 = Connector(g3,g4)#working properly
print(g4.getOutput())
NORg1 = OrGate("G1", "Nah-one")
NORg2 = NotGate("G2", "Nawto")
NORc1 = Connector(NORg1,NORg2)
print(NORg2.getOutput())