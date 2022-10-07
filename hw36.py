class car():
     
    def __init__(self, model, color):
        self.model = model
        self.color = color
         
    def show(self):
        print("Model is", self.model )
        print("color is", self.color )
         

Toyota = car("Toyota a4", "red")
ferrari = car("ferrari 487", "black")
 
Toyota.show() 
ferrari.show() 
