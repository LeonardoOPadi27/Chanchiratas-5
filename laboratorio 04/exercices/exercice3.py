'''
Ejercicios (Si aplica)
Explicar cómo funciona el algoritmo
Hacer su diagrama de cómo se ejecuta.
Comentarios del problema
Hacer 3 casos de prueba
Desarrollar todo el código en inglés

Exercise 3: Implement a Stack with getMin() Function
'''
class ArrayStack:
    def __init__(self, capacity = 10): #Constructor of the class ArrayStack
        self.data = [None] * capacity
        self.capacity = capacity
        self.top = -1
    
    def is_empty(self): #It's gonna verify if the stack is empty
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity -1 #It's gonna verify if the stack is full

    def push(self, item): #Add an item in the top of the stack
        if self.is_full(): #If the stack is full, throw an error
            raise OverflowError("Stack overflow - stack is full")
        
        self.top += 1
        self.data[self.top] = item

        return True
    
    def pop(self): #Removes the top item
        if self.is_empty(): #If the stack is empty, throw an error
            raise IndexError("Stack underflow - stack is empty")
        
        item = self.data[self.top]
        self.data[self.top] = None  # Remove reference to the object
        self.top -= 1
        return item
    
    def peek(self):
        if self.is_empty(): #If the stack is empty, throw an error
            raise IndexError("Stack underflow - stack is empty")
        
        return self.data[self.top] #Return the top item
    
    def size(self):
        return self.top + 1 #Return the number of items in the stack
    
    def __str__(self):
        if self.is_empty(): #If the stack is empty, return an "array" (it's just two parenthesis) empty
            return "Stack: []"
        
        items = [str(self.data[i]) for i in range(self.top + 1)] #Returns the items of the stack in string
        return f"Stack: [{', '.join(items)}]"
    
    def getMin(self):
        if self.is_empty(): #If the stack is empty, throw an error
            raise IndexError("Stack underflow - stack is empty")

        current_items = self.data[:self.top + 1] #Takes only valid elements from the stack, ignoring None in unused space.

        for i in current_items: #The loop will go through the entire list
            if not isinstance(i, (int, float)): #Will verify that the data is int or float
                raise TypeError("TypeError - there are data that are not numbers")
        return min(current_items) #Return the minimum value

if __name__ == "__main__":
    print("test case 1")
    firstTestCaseStack = ArrayStack(2)
    firstTestCaseStack.push(142)
    firstTestCaseStack.push(251)
    #firstTestCaseStack.push(532)
    print(firstTestCaseStack.getMin())
    
    print("test case 2")
    secondTestCaseStack = ArrayStack()
    secondTestCaseStack.push(124)
    secondTestCaseStack.push(152)
    #secondTestCaseStack.push("Hola")
    print(secondTestCaseStack.getMin())
    
    print("test case 3")
    thirdTestCaseStack = ArrayStack()
    thirdTestCaseStack.push(1254)
    thirdTestCaseStack.push(1423.251)
    print(thirdTestCaseStack.getMin())