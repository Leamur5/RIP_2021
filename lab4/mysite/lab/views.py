#from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
from lab.models import Cat

def GetCats(request):
    return render(request, 'cats.html', {'data' : {
        'current_date': date.today(),
        'cats': Cat.objects.all()
    #[{'name': 'Мейн-кун'},
    #        {'name': 'Сиамская кошка'},
    #        {'name': 'Сфинкс'},]
    }})

def GetCat(request, name):
    return render(request, 'cat.html', {'data' : {
        'current_date': date.today(),
        'cat': Cat.objects.filter(name=name)[0]
    #        [{'name': 'Мейн-кун', 'desc': 'самая крупная порода домашних кошек, которую можно завести в семье с маленькими детьми и другими животными. Ведь несмотря на хищную внешность, представители породы уравновешены и абсолютно неагрессивны. А еще кошек мейн-кунов относят к классу питомцев-компаньонов. Причем с характером собаки. Поэтому не удивляйтесь, если животное захочет поиграть в апорт или проявит интерес к купанию в ванне или прогулкам на шлейке. Но по-настоящему верны только тому, кого выберут в качестве вожака. Обычно это человек, который проводит с кошкой больше времени и следит за ее питанием.',
    #         'img': 'images/main_kun.jpg'},
    #        {'name': 'Сиамская кошка', 'desc': 'это кошка среднего размера с длинным, стройным и грациозным телом.Она бывает различных окрасов. Цвет глаз при любых окрасах и вариантах пятнистости всегда остается ярким, насыщенно-голубым.',
    #         'img': 'images/siamskaya.jpg'},
    #       {'name': 'Сфинкс', 'desc': 'бесшерстная кошка с поведением и характером собаки. Представители породы относятся к классу компаньонов. Животное ориентировано на взаимодействие, любит сидеть на коленях, легко уживается с другими животными в доме и хорошо ладит с детьми, даже самыми маленькими.',
    #        'img': 'images/cfinks.jpg'}]
    }})



# Create your views here.
