def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

# inner_function() - inner_function находится в локальном пространстве имен функции test_function.
# Таким образом делаем вывод, что из глобального пространства имен мы не может обратиться к локальному. Также мы можем
# применить метод nonlocal к функции inner_function и тогда такой вызова функции сработает
