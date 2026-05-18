class person:
    def __init__(self,name):
        self.name = name
        
    def greet(self):
        print("hello , my name is "+self.name)
        
d1= person("rajan")
d1.greet()
d2=person("rajiiv")
d2.greet()