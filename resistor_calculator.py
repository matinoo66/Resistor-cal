class Resistor:
    def __init__(self, color1, color2, color3, color4):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.color4 = color4

    def get_resistance(self):
        colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'gray', 'white' , 'silver','gold']
        values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0.1, 0.05]
        
        index1 = colors.index(self.color1)
        index2 = colors.index(self.color2)
        index3 = colors.index(self.color3)
        index4 = colors.index(self.color4)
        
        multiplier = ((values[index1] * 10) + (values[index2])) * (10 ** values[index3])
        tolerance = values[colors.index(self.color4)]
        
        return f"{multiplier}+-{tolerance*multiplier} OHMs"

# برنامه اصلی
resistors = []
count = 0
while True:

    print("\n1. Adding new resistor")
    print("2. show resistors list")
    print("3. exit")
    
    choice = input("choose: ")
    
    if choice == "1":
        color1 = input("Enter the first color ").lower()
        color2 = input("Enter the Next color ").lower()
        color3 = input("Enter the Next color ").lower()
        color4 = input("Enter the Last color ").lower()
            
        resistor = Resistor(color1, color2, color3, color4)
        resistors.append(resistor)
        count=+1
        print(f"Resistor{count}: {resistor.get_resistance()} Added")
    elif choice == "2":
        if not resistors:
            print("Empty List")
        else:
            for resistor in resistors:
                print(f"- {resistor.get_resistance()}")
    elif choice == "3":
        break
    else:
        print(" Try Again")