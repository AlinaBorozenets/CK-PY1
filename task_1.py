if __name__ == "__main__":
    # Write your solution here
    class Auto:
        def __init__(self, brand: str, name: str, engine: str, maxspeed: int):
            '''Класс автомобиль
                Атрибуты
                --------
                brand: str
                    бренд, выпустивший эту машину
                name : str
                    название машины
                engine : str
                    двигатель, который установлен в машину
                maxspeed : int
                    максимальная скорость, которую развивает это авто
                Методы
                ------
                info(additional=""):
                    Печатает имя и возраст покупателя.
            '''
            self.engine = engine
            self.name = name
            self.brand = brand
            self.maxspeed = maxspeed

        def __str__(self) -> str:
            return f'Автомобиль "{self.brand}" "{self.name}" двигатель "{self.engine}" с максимальной скоростью "{self.maxspeed}"'

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.name!r}, collection={self.engine!r}, shade={self.maxspeed})'

        @staticmethod
        def buy(self):
            '''Метод Определения нужного авто'''
            print("The desired car is defined")

        def use_auto(self):
            '''Метод эксплуатации авто'''
            fuel = 'user manual'
            print("use with" + fuel)


    class ElectricAuto(Auto):
        def __init__(self, brand: str, name: str, engine: str, maxspeed: int, number: float):
            '''Класс Электрокары
                Атрибуты
                --------
                number: str
                    количество двигателей в автомобиле



                Методы
                ------
                info(additional=""):
                Печатает имя и возраст покупателя.
            '''
            super().__init__(brand, name, engine, maxspeed)
            self.number = number

        # Перегрузим только метод __repr__, т.к. у электрокаров появились новые атрибуты,
        # но выводить для пользователя мы их не будем

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.name!r}, engine={self.engine!r}, maxspeed={self.maxspeed}, ' \
                   f'volume={self.number}) '

        #метод buy унаследуем от родительского класса

        def apply_blush(self):
            '''Метод эксплуатации авто
                перегрузим метод родительского класса, т.к. для каждого типа электрокара нужнен свой особый двигатель
            '''
            electricmotor = 'user manual'
            print("use with" + electricmotor)
    pass
