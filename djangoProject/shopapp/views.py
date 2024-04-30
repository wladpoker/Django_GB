from django.shortcuts import render
from django.http import HttpResponse
from ecommerce_project.order_analysis import get_ordered_products

def orders(request):
    # Вызов функции для анализа заказов

    html = """
    
    <h1>Вывод в консоли</h1>
    <p>Здесь вы найдете интересные статьи, новости и многое другое.</p>
    
    """
    print(get_ordered_products('Alice', 365))
    return HttpResponse(html)

    
def home(request):
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Здесь вы найдете интересные статьи, новости и многое другое.</p>
    """

    # Логирование посещения страницы
    print("Пользователь посетил главную страницу")

    return HttpResponse(html)


def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Привет! Меня зовут Владислав, я начинающий веб-разработчик. Я увлекаюсь программированием и Игр на фреймворке Renpy.</p>
    """

    # Логирование посещения страницы
    print("Пользователь посетил страницу 'О себе'")

    return HttpResponse(html)