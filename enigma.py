class Plugboard(object):
    def __init__(self, *args):
        self.tel = {}
        if args:
            self.initTel(args[0])


    def initTel(self, wires):

        if len(wires) < 21 and len(wires) % 2 == 0:
            for i in range(len(wires)):
                if i % 2 == 0:
                    if wires[i] not in self.tel and wires[i + 1] not in self.tel:
                        self.tel[wires[i]] = wires[i+1]
                        self.tel[wires[i+1]] = wires[i]
                    else:
                        raise Exception("Too many wires defined")

        else:
            raise Exception("Too many wires defined")


    def process(self, c):
        tel = self.tel
        if c in tel:
            return tel[c]
        else:
            return c

plugboard = Plugboard("ABCA")
print(plugboard.process("A"))
