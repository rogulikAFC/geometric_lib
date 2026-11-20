def area(a:float, h:float) -> float: 
    """
    Возвращает площадь треугольника.

    Параметры:
        a (float): длина основания
        h (float): длина высоты

    Возвращаемое значение:
        area (float): площадь треугольника 
    """
    if a < 0 or h < 0:
        raise ValueError("base and height must be non-negative")
    
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
    if a < 0 or b < 0 or c < 0:
        raise ValueError("sides must be non-negative")
    
    if a > b + c or b > a + c or c > a + b:
        raise ValueError("sides do not form a triangle")
    
    return a + b + c 