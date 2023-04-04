class ListExercise:
    left_idx = 0
    right_idx = 0

    @classmethod
    def reset_idx(cls) -> None:
        cls.left_idx = 0
        cls.right_idx = 0

    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """

        if len(input_list) == 0:
            return input_list

        max_value = input_list[0]
        positive_idx = []
        idx = 0

        for value in input_list:
            if value > max_value:
                max_value = value
            if value > 0:
                positive_idx.append(idx)
            idx += 1

        for i in positive_idx:
            input_list[i] = max_value

        return input_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        if len(input_list) == 1:
            ListExercise.reset_idx()
            return 0 if input_list[0] == query else -1

        if len(input_list) > 1:
            mid_idx = len(input_list) // 2
            left_arr = input_list[:mid_idx]
            right_arr = input_list[mid_idx:]
            if query == input_list[mid_idx]:
                idx = ListExercise.left_idx + mid_idx
                ListExercise.reset_idx()
                return idx
            if query < input_list[mid_idx]:
                ListExercise.right_idx += mid_idx
                return ListExercise.search(left_arr, query)
            if query > input_list[mid_idx]:
                ListExercise.left_idx += mid_idx
                return ListExercise.search(right_arr, query)

        ListExercise.reset_idx()
        return -1
