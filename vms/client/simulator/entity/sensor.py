class CO(Sensor):
    step = 0
    
    def __init__(self,name):
        super().__init__(name)
        self.type = "carbon oxid"
        
    def generate_new_value(self):
        self.value = self.step * 1e6
        self.step = self.step + 0.001
