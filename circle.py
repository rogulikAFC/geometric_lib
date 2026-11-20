import math

def area(r:float) -> float:
    """
    Принимает значение радиуса r круга, возвращает площадь круга.

    Параметры:
        r (float): длина радиуса круга

    Возвращаемое значение:
        area (float): площадь круга
    """
    if r < 0:
        raise ValueError("r must be non-negative")
    
    return math.pi * r * r


def perimeter(r:float) -> float:
    """
    Принимает значение радиуса r круга, возращается периметр круга.

    Параметры:
        r (float): длина радиуса круга
    
    Возвращаемое значение:
        perimeter (float): периметр круга
    """
    if r < 0:
        raise ValueError("r must be non-negative")
    
    return 2 * math.pi * r
