from datetime import date

day = date.today().day
month_number = date.today().month

months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
          'декабря']
month = months[month_number-1]

temperature = int(input('Сколько сегодня градусов?\n'))

print(f'Сегодня {day} {month}. На улице {temperature} градусов.')

if temperature < 0:
    print('Холодно, лучше остаться дома')

