from lab_python_oop import rectangle
from lab_python_oop import circle
from lab_python_oop import square
import requests

def main():
    rect = rectangle.Rectangle(3,3,'синий')
    circ = circle.Circle(3, 'зеленый')
    squar = square.Square(3, 'красный')
    print('{0!r}'.format(rect))
    print('{0!r}'.format(circ))
    print('{0!r}'.format(squar))
    r = requests.get('https://api.github.com/events')
    print('Проверяем библиотеку requests:')
    print("Код возврата:" + str(r.status_code))
    print("Сontent-type:" + str(r.headers['content-type']))
    

if __name__ == "__main__":
    main()