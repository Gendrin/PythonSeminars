import edit as me


def Operation(code_op):
    if code_op =='1': me.InsertTable('users',me.InsertUser())
    elif code_op =='2':
        print('Редактируем пользователя! Задайте критерии поиска!')
        me.EditUser()
    elif code_op =='3':
        print('Удаляем пользователя! Задайте критерии поиска!')
        me.DeleteUser()
