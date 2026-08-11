from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}
    # можете добавить свои рецепты ;)

def test_page(request):
    return HttpResponse("hellow world")

def recept (request):
    recept_name = request.path.strip('/')
    servings = int (request.GET.get('servings', 1))
    try:
        if servings < 1:
            servings = 1
    except ValueError:
        servings = 1

    recipe_data = DATA[recept_name]
    recipe = {}
    for ingredient, amount in recipe_data.items():
        recipe[ingredient] = amount * servings

    context = {
        'recipe': recipe,
        'recept_name': recept_name,
        'servings': servings
    }

    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
