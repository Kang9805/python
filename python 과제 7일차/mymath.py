# 여러분이 자주 사용하는 수학적 연산<br>
# (예: 삼각형 넓이, 원의 넓이, 직육면체의 넓이)을 수행하는 함수들을 포함하는 mymath.py라는 이름의 모듈을 만드세요. 
# 이 모듈을 사용하여 작성된 함수들을 실제로 임포트하고 사용하는 간단한 프로그램을 작성하세요.


import math

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2

def cuboid_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)
