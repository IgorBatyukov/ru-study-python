from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """
        map_list = []
        for movie in list_of_movies:
            if movie['rating_kinopoisk'] and len(movie['country'].split(',')) >= 2:
                rating = float(movie['rating_kinopoisk'])
                if 0 < rating <= 4:
                    map_list.append(('low', rating))
                elif 4 < rating < 7:
                    map_list.append(('average', rating))
                elif rating >= 7:
                    map_list.append(('high', rating))
        total = 0
        for _, value in map_list:
            total += value

        return total / len(map_list)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        map_list = map(
            lambda x: (x['name'].count('и'))
            if x['rating_kinopoisk'] and float(x['rating_kinopoisk']) >= rating
            else 0,
            list_of_movies
        )

        return sum(map_list)
