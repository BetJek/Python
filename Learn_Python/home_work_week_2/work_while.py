
# Задание

#     Напишите функцию ask_user(), которая с помощью input() спрашивает пользователя “Как дела?”, пока он не ответит “Хорошо”
#     Создайте словарь типа "вопрос": "ответ", например: {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
#     Доработайте ask_user() так, чтобы когда пользователь вводил вопрос который есть в словаре, программа давала ему соотвествующий ответ. Например:

# >>>   Пользователь: Что делаешь?
# >>>   Программа: Программирую

def ask_user():
    while True:
        good = input('Как дела?\n')
        if good == 'Хорошо':
            break 

ask_user()