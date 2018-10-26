# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Traingle:
    def __init__(self, dot1, dot2, dot3):
        self.dot1 = dot1
        self.dot2 = dot2
        self.dot3 = dot3

    def sides(self):       
        side1_2 = abs(((self.dot1[0] - self.dot2[0]) ** 2 + (self.dot1[1] - self.dot2[1]) ** 2) ** 0.5)
        side1_3 = abs(((self.dot1[0] - self.dot3[0]) ** 2 + (self.dot1[1] - self.dot3[1]) ** 2) ** 0.5)
        side2_3 = abs(((self.dot2[0] - self.dot3[0]) ** 2 + (self.dot2[1] - self.dot3[1]) ** 2) ** 0.5)
        sides = (side1_2, side1_3 ,side2_3)
        return sides     
    
    def perimetr(self):
        l_sides = self.sides()
        perimetr = l_sides[0] + l_sides[1] + l_sides[2]
        return perimetr
       
    def square(self):
        square = abs(0.5 * (self.dot2[0] - self.dot1[0]) * (self.dot3[1] - self.dot1[1]) - (self.dot3[0] - self.dot1[0]) * (self.dot2[1] - self.dot1[1]))
        return square
    
    def hights(self):
        l_sides = self.sides()
        l_square = self.square()
        high_1 = abs((2 * l_square)/ l_sides[2])
        high_2 = abs((2 * l_square)/ l_sides[1])
        high_3 = abs((2 * l_square)/ l_sides[0])
        return high_1, high_2, high_3
        
        
tr = Traingle([1,5], [2,2], [1,1])
print (tr.hights())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapezium:
    def __init__(self, dot1, dot2, dot3, dot4):
        self.dot1 = dot1
        self.dot2 = dot2
        self.dot3 = dot3
        self.dot4 = dot4

    def sides(self):       
        side1_2 = abs(((self.dot1[0] - self.dot2[0]) ** 2 + (self.dot1[1] - self.dot2[1]) ** 2) ** 0.5)
        side1_4 = abs(((self.dot1[0] - self.dot4[0]) ** 2 + (self.dot1[1] - self.dot4[1]) ** 2) ** 0.5)
        side2_3 = abs(((self.dot2[0] - self.dot3[0]) ** 2 + (self.dot2[1] - self.dot3[1]) ** 2) ** 0.5)
        side3_4 = abs(((self.dot3[0] - self.dot4[0]) ** 2 + (self.dot3[1] - self.dot4[1]) ** 2) ** 0.5)
        sides = (side1_2, side1_4 ,side2_3, side3_4)
                
        return sides     
    
    def ravnob(self):
        l_sides = self.sides()
        if l_sides[0] == l_sides[3] or l_sides[1] == l_sides[2]:
            return "Трапеция равнобедренная"
        else:
            return 'Трапеция не равнобедреная'
    
    def perimetr(self):
        l_sides = self.sides()
        perimetr = l_sides[0] + l_sides[1] + l_sides[2] + l_sides[3]
        return perimetr
       
    def square(self):
        l_sides = self.sides()
        l_high = self.hights()
        square = abs(0.5 * (l_sides[0] + l_sides[3]) * l_high)
        return square
    
    def hights(self):
        l_sides = self.sides()
        
        high = abs(0.5 ** ((l_sides[1] ** 2 - ((l_sides[3] - l_sides[0]) ** 2 + l_sides[1] ** 2 - l_sides[2] **2) / (2 * (l_sides[3] - l_sides[0])) ) ** 2))
        
        return high
        
        
tr = Trapezium([4,2], [8,2], [9,4], [3,4])
print (tr.hights())