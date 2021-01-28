
# создаю Класс 
class Table:
    table = {}

# Метод save_game инстализирует Игру в ожидании
    def save_game(self, mes_id, user_id, user_n):
        mes_id, user_id = str(mes_id), str(user_id)
        Table.table[mes_id] = {
            # наше поля игры
            'Table': [
                '1', '2', '3',
                '4', '5', '6',
                '7', '8', '9'
            ],
            'X': user_id,
            # тут хранится имена игроков
            'users_name': [user_n],
            # очередь(кто ходит)
            'turn': 'X'
        }
# Метод Which_turn оперделяет , является ли игрок равным очереди
# И инстализирует Игрока Нолика
    def which_turn(self, mes_id, user_id, user_n, move):

        mes_id, user_id, move = str(mes_id), str(user_id), int(move)

        turn = Table.table[mes_id]['turn']

        def fn():
            try:

                if Table.table[mes_id].get(turn) == user_id:

                    if Table.table[mes_id]['Table'][move] not in ['X', 'O']:

                        Table.table[mes_id]['Table'][move] = turn
                        Table.table[mes_id]['turn'] = 'X' if turn == 'O' else 'O'
                        print(turn)
                        return True

                    else:

                        return False

                elif Table.table[mes_id].get(turn) is None:

                    if user_id != Table.table[mes_id]['X']:

                        Table.table[mes_id]['O'] = user_id
                        Table.table[mes_id]['users_name'].append(user_n)
                        return fn()

                    else:
                        return False

                else:
                    return False

            except:

                return False

        return fn()
# Возвращает поле игры (текущую)
    def return_table(self, mes_id):

        table = Table.table[str(mes_id)]['Table']
        return [i if i in ['X', 'O'] else ' ' for i in table]
# Возвращает Игроков (имена а не ай-ди)
    def return_users(self, mes_id):

        if len(Table.table[str(mes_id)]['users_name']) == 2:

            return Table.table[str(mes_id)]['users_name']
        else:

            return [Table.table[str(mes_id)]['users_name'][0], '']
# Возвращает готовую строку если победа осуществлена
    def return_winner(self, mes_id):

        table = Table.table[str(mes_id)]['Table']
        check = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
        )
        for t in check:

            if table[t[0]] == table[t[1]] == table[t[2]]:

                if table[t[0]] == 'X':

                    str_ = 'Победитель X: {} O: {}'.format(Table.table[str(mes_id)]['users_name'][0], Table.table[str(mes_id)]['users_name'][1])

                    del Table.table[str(mes_id)]
                    return str_

                else:

                    str_ = 'X: {} Победитель O: {}'.format(Table.table[str(mes_id)]['users_name'][0], Table.table[str(mes_id)]['users_name'][1])

                    del Table.table[str(mes_id)]
                    return str_
