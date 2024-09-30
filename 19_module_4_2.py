# пространство имён и области видимости

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function() # ничего не возвращает и никак не отображается

inner_function() # подчёркнуто красным, при запуске получим ошибку
                 # 'name 'inner_function' is not defined. Did you mean: 'test_function'?'

test_function() # возвращает принт функции inner_function()
                # 'Я в области видимости функции test_function'