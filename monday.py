class data:
    clg='abc college'
    def __init__(self,name,rno,age):
        self.name=name
        self.rno=rno
        self.age=age

    def m(self): #im
        print(self.name)
        print(self.rno)
        print(self.age)

    @classmethod
    def n(cls): #cm
        print(data.clg)
        print(cls.clg)

    @staticmethod
    def add(a,b):
        print(a+b)    
        
st1=data('a',1001,9)
st1.m()
st1.n()
st1.add(10,20)















