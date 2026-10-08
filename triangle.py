def area(a:float, h:float) -> float: 
    """
    Возвращает площадь треугольника.

    Параметры:
        a (float): длина основания
        h (float): длина высоты

    Возвращаемое значение:
        area (float): площадь треугольника 
    """
    return a * h / 2 
    
def perimeter(a:float, b:float, c:float) -> float: 
    """
    Возвращает периметр треугольника.

    Параметры:
        a (float): длина 1 стороны
        b (float): длина 2 стороны
        c (float): длина 3 стороны

    Возвращаемое значение:
        perimeter (float): периметр треугольника
    """
    return a + b + c 