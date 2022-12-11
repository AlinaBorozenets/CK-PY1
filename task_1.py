# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class SuccessfulExams:
    """
    Документация №1
    Класс описывает успех на сессии

    """

    def __init__(self, attendance_percentage: float, percentage_understanding: float):
        """
        :param attendance_percentage: процент посещаемости
        :param percentage_understanding: процент понимания материала
        Пример:
        >>> success = SuccessfulExams(60, 55) # инициализация экземпляра класса

        """
        if not isinstance(attendance_percentage, (int, float)):
            raise TypeError("Процент посещаемости должен быть типа int или float")
        if attendance_percentage < 0:
            raise ValueError("Процент посещаемости не может быть отрицательным числом")
        self.attendance_percentage = attendance_percentage

        if not isinstance(percentage_understanding, (int, float)):
            raise TypeError("процент понимания материала должен быть int или float")
        if percentage_understanding < 0:
            raise ValueError("процент понимания материала не может быть отрицательным числом")
        self.percentage_understanding = percentage_understanding

    def additional_session(self, exam_difficulty: float):
        """
        Функция, которая по коэффициенту сложности экзамена определяет, попадает человек на доп.сессию или нет
        :param exam_difficulty: коэффициент сложности экзамена
        :return: возвращает занчение "да" в случае попадаения на допсу и "нет" в случае непопадения
        Примеры:
        >>> SuccessfulExams = SuccessfulExams(40, 35)
        >>> SuccessfulExams.additional_session(50)
        """
        if not isinstance(exam_difficulty, (int, float)):
            raise TypeError("коэффициент сложности экзамена должен быть типа int или float")
        if exam_difficulty < 0:
            raise ValueError("коэффициент сложности экзамена должен быть положительным числом")
        ...

    def procent_succesful(self):

        """
        Функция которая считает среднее арифмитечсекое проуентов посещаемости и понимания материала
        :return: процент успеха на экхамене

        Пример:
        >>> Successful_Exams = SuccessfulExams(68, 75)
        >>> Successful_Exams.procent_succesful()
        """
        ...

class Room:
    """
    Документация №2
    Класс описывает комнату
    """
    def __init__(self, width: float, length: float):
        """
        :param width: ширина комнаты, м
        :param length: длина комнаты, м
        Пример:
        >>> room_1 = Room(5, 3) # инициализация экземпляра класса
        """
        if not isinstance(width, (int, float)):
            raise TypeError("ширина должна быть типа int или float")
        if width < 0:
            raise ValueError("ширина не может быть отрицательной")
        self.width = width

        if not isinstance(length, (int, float)):
            raise TypeError("длина должна быть типа int или float")
        if length < 0:
            raise ValueError("длина не может быть отрицательной")
        self.lengh = length

    def free_square(self, square_use: float):
        """
            Функция, которая считает площадь свободной территории в комнате
            :param square_use: площадь занятой территории
            :return: значение площади свободной территории в комнате
            Примеры:
            >>> Room_0 = Room(6, 8)
            >>> Room_0.free_square(28)
        """
        if not isinstance(square_use, (int, float)):
            raise TypeError("используемая площадь должна быть типа int или float")
        if square_use < 0:
            raise ValueError("используемая площадь должна быть положительным числом")
        ...

    def square(self):
        """
        Функция которая считает площадь комнаты
        :return: площадь комнаты через заданную длину и ширину

        Пример:
        >>> Room_1 = Room(3, 4)
        >>> Room_1.square()
        """
        ...
class Temperature:
    """
    Документация №3
    класс описывает среднюю температуру воздуха за день
    """

    def __init__(self, temp_morning: float, temp_daytime: float, temp_evening: float):
        """
        :param temp_evening: средняя температура утром
        :param temp_daytime: средняя температура днём
        :param temp_evening: средняя температура вечером
        Пример:
        >>> temp_0 = Temperature(0, 5, -3) # инициализация экземпляра класса

        """
        if not isinstance(temp_morning, (int, float)):
            raise TypeError("температура утром должна быть типа int или float")
        self.temp_morning = temp_morning

        if not isinstance(temp_daytime, (int, float)):
            raise TypeError("температура днём должна быть типа int или float")
        self.temp_daytime = temp_daytime

        if not isinstance(temp_evening, (int, float)):
            raise TypeError("температура вечером должна быть типа int или float")
        self.temp_evening = temp_evening

    def average_temperature(self):
        """
            Функция, которая считает среднюю температуру за день
            :return: значение площади свободной территории в комнате
            Примеры:
            >>> temp_fullday = Temperature(-5, 1, -2)
            >>> temp_fullday.average_temperature()
        """
        ...

    def maximum(self):
        """
            Функция, которая считает максимальную температуру за день
            :return: значение максимальной температуры за день
            Примеры:
            >>> temp = Temperature(-10, -15, -16.5)
            >>> temp.maximum()
        """
        ...
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
