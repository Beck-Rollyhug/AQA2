def check_triangle(a, b, c):
    isTriangle =  a + b > c and a + c > b and b + c > a

    if isTriangle:
        is3Sides = a == b == c
        if (is3Sides):
            return 'равносторонний'
        
        is2Sides = a == b or a == b or b == c
        if (is2Sides):
            return 'равнобедренный'
        
        return 'разносторонний'
    else:
        return 'не существует'

def task9():
    a, b, c = input('a, b, c: ').split(' ')
    triangleType = check_triangle(int(a), int(b), int(c))

    print(f'Треугольник {triangleType}')
