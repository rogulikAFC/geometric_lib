def area(a:float, b:float) -> float: 
    """
    Принимает значение длин сторон прямоугольника a и b, возвращает площадь прямоугольника.

    Параметры:
        a (float): длина 1 стороны прямоугольника
        b (float): длина 2 стороны прямоугольника

    Возвращаемое значение:
        area (float): площадь прямоугольника
    """
    if a < 0 or b < 0:
        raise ValueError("sides must be non-negative")
    
    return a * b

def perimeter(a:float, b:float) -> float: 
    """
    Принимает значение длин сторон прямоугольника a и b, возвращает периметр прямоугольника.

    Параметры:
        a (float): длина 1 стороны прямоугольника
        b (float): длина 2 стороны прямоугольника
    
    Возвращаемое значение:
        perimeter (float): периметр прямоугольника
    """
    if a < 0 or b < 0:
        raise ValueError("sides must be non-negative")
    
    return 2 * (a + b) 