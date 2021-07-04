from django.shortcuts import render

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
    # можете добавить свои рецепты ;)
}


def omlet_view(request):
    servings = request.GET.get('servings', '1')
    context = {
        'recipe': {
            'яйца, шт': DATA['omlet']['яйца, шт'] * int(servings),
            'молоко, л': DATA['omlet']['молоко, л'] * int(servings),
            'соль, ч.л.': DATA['omlet']['соль, ч.л.'] * int(servings),
        }
    }
    return render(request, 'calculator/index.html', context)


def pasta_view(request):
    servings = request.GET.get('servings', '1')
    context = {
        'recipe': {
            'макароны, г': DATA['pasta']['макароны, г'] * int(servings),
            'сыр, г': DATA['pasta']['сыр, г'] * int(servings),
        }
    }
    return render(request, 'calculator/index.html', context)
