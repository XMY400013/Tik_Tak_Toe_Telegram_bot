import telebot
from telebot import types
from dotenv import load_dotenv
import os
from Class import Table


dotenv_path = os.path.join(os.path.dirname(__file__), 'env')
load_dotenv(dotenv_path)

tb = telebot.TeleBot(os.getenv('TOKEN'))

# Класс таблица
table = Table()


# отклик ан команду
@tb.message_handler(commands=['x_O'])
def start_game(message):

    m = types.InlineKeyboardMarkup()
    b_1 = types.InlineKeyboardButton(text=' ', callback_data='0')
    b_2 = types.InlineKeyboardButton(text=' ', callback_data='1')
    b_3 = types.InlineKeyboardButton(text=' ', callback_data='2')
    b_4 = types.InlineKeyboardButton(text=' ', callback_data='3')
    b_5 = types.InlineKeyboardButton(text=' ', callback_data='4')
    b_6 = types.InlineKeyboardButton(text=' ', callback_data='5')
    b_7 = types.InlineKeyboardButton(text=' ', callback_data='6')
    b_8 = types.InlineKeyboardButton(text=' ', callback_data='7')
    b_9 = types.InlineKeyboardButton(text=' ', callback_data='8')

    m.add(b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9)
    mes_ = tb.send_message(message.chat.id, f'X: {message.from_user.first_name} O:', reply_markup=m)
    table.save_game(mes_.message_id, message.from_user.id, message.from_user.first_name)
    print(table.table)
    print(mes_.message_id)


@tb.callback_query_handler(func=lambda call: True)
def calling(call):
    print(call.message.message_id)
    print(table.table)
    if table.which_turn(call.message.message_id, call.from_user.id, call.from_user.first_name, call.data):

        list_table = table.return_table(call.message.message_id)

        m = types.InlineKeyboardMarkup()
        b_1 = types.InlineKeyboardButton(text=list_table[0], callback_data='0')
        b_2 = types.InlineKeyboardButton(text=list_table[1], callback_data='1')
        b_3 = types.InlineKeyboardButton(text=list_table[2], callback_data='2')
        b_4 = types.InlineKeyboardButton(text=list_table[3], callback_data='3')
        b_5 = types.InlineKeyboardButton(text=list_table[4], callback_data='4')
        b_6 = types.InlineKeyboardButton(text=list_table[5], callback_data='5')
        b_7 = types.InlineKeyboardButton(text=list_table[6], callback_data='6')
        b_8 = types.InlineKeyboardButton(text=list_table[7], callback_data='7')
        b_9 = types.InlineKeyboardButton(text=list_table[8], callback_data='8')

        m.add(b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9)
        users = table.return_users(call.message.message_id)

        tb.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id, reply_markup=m, text=f'X: {users[0]} O: {users[1]}')

        end_game = table.return_winner(call.message.message_id)
        if end_game:

            tb.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                text=end_game,
                reply_markup=m)
            print('ended game')


if __name__ == '__main__':
    tb.polling(none_stop=True)
