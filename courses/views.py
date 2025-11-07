from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages


def register(request):
    """
    ОБРАБОТКА РЕГИСТРАЦИИ ПОЛЬЗОВАТЕЛЯ
    """
    if request.method == "POST":
        # ⬇️ ЕСЛИ ФОРМА ОТПРАВЛЕНА - ОБРАБАТЫВАЕМ ДАННЫЕ
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # 🎉 СОХРАНЯЕМ ПОЛЬЗОВАТЕЛЯ В БАЗУ ДАННЫХ
            user = form.save()

            # 🔐 АВТОМАТИЧЕСКИ ВХОДИМ ПОСЛЕ РЕГИСТРАЦИИ
            login(request, user)

            # 💬 ПОКАЗЫВАЕМ СООБЩЕНИЕ ОБ УСПЕХЕ
            messages.success(
                request, f"Аккаунт создан! Добро пожаловать, {user.username}!"
            )

            # 🚀 ПЕРЕНАПРАВЛЯЕМ НА ГЛАВНУЮ
            return redirect("home")
    else:
        # ⬇️ ЕСЛИ GET ЗАПРОС - ПОКАЗЫВАЕМ ПУСТУЮ ФОРМУ
        form = UserCreationForm()

    # 🎨 ПОКАЗЫВАЕМ ФОРМУ РЕГИСТРАЦИИ
    return render(request, "registration/register.html", {"form": form})


def home(request):
    """
    ПРОСТАЯ ГЛАВНАЯ СТРАНИЦА ДЛЯ ТЕСТА
    """
    return render(request, "home.html")


def custom_logout(request):
    logout(request)
    return redirect("login")  # ⬅️ Прямо на страницу входа
