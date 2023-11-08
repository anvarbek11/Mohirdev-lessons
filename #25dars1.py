#25 dars - Klass va Obyekt


class Kompyuter:
    def __init__(self,ram,hdd,gpu,cpu):
        self.ram = ram
        self.hdd = hdd
        self.gpu = gpu
        self.cpu = cpu
    def info(self):
        inf = f"{self.ram},SSD:{self.hdd}, GPU:{self.gpu},CPU:{self.cpu}"
        return inf    
macbook = Kompyuter("8gb", "512gb", "M1", "M1")    

print(macbook.info() )   