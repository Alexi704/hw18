# Сколько сезонов
# Чтобы узнать, насколько продуктивно работает режиссер
# Alastair Fothergill, мы решили посчитать,
# сколько сезонов сериалов он всего снял.
#
# Пример результата:
#
# Длительность всех сериалов режисcера Alastair Fothergill составляет x сезона.
#
# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# -----------------------
import sqlite3

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = ("""
                SELECT director, SUM(duration)
                FROM netflix
                WHERE director = "Alastair Fothergill" 
                AND type = "TV Show"
                """)  # TODO измените код запроса
cur.execute(sqlite_query)
executed_query = cur.fetchall()[0]

# TODO Результат запроса сохраните в переменной result
# для последующей выдачи в требуемом формате

result = f"{executed_query[0]} снял {executed_query[1]} сезонов сериалов"

if __name__ == '__main__':
    print(result)
