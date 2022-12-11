# первый абстрактный класс
class Weather:
    def __init__(self, temperature: (int, float), humidity: (int, float)):
        """
        Создание и подготовка к работе объекта "Погода"
        :param temperature: Темпреатура воздуха
        :param humidity: Влажность воздуха
        Примеры:
        >>> winter = Weather(10, 90)  # инициализация экземпляра класса
        """
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть формата int или float")
        self.temperature = temperature

        if not isinstance(humidity, (int, float)):
            raise TypeError("Влажность должна быть int или float")
        if humidity < 0:
            raise ValueError("Влажность не может быть отрицательной")
        if humidity > 100:
            raise ValueError("Влажность не может быть больше 100%")
        self.humidity = humidity

        self.is_season()
        self.is_coldly()

    def is_season(self) -> bool:
        """
        Функция, которая проверяет время года
        :return: Время года
        Примеры:
        >>> weather = Weather(12, 5)
        >>> weather.is_season()
        """
        ...

    def is_coldly(self) -> bool:
        """
        Функция, которая проверяет холодно ли
        :return: Хоролодно или нет
        Примеры:
        >>> weather = Weather(-13, 60)
        >>> weather.is_coldly()
        """
        ...


# второй абстрактный класс
class Water:
    def __init__(self, temperature: (int, float), mineralization: (int, float)):
        """
        Создание и подготовка к работе объекта "Вода"
        :param temperature: Темпреатура воды
        :param mineralization: Минерализация воды
        Примеры:
        >>> winter = Water(10, 90)  # инициализация экземпляра класса
        """
        if not isinstance(temperature, (int, float)):
            raise TypeError("Температура должна быть формата int или float")
        self.temperature = temperature

        if not isinstance(mineralization, (int, float)):
            raise TypeError("Минерализация должна быть int или float")
        if mineralization < 0:
            raise ValueError("Минерализация не может быть отрицательной")
        self.humidity = mineralization

        self.water_category()
        self.water_hardness()

    def water_category(self) -> str:
        """
        Функция, которая проверяет категорию воды
        :return: Категория рассматриваемой воды
        Примеры:
        >>> weather = Water(12, 500)
        >>> weather.water_category()
        """
        ...

    def water_hardness(self) -> str:
        """
        Функция, которая проверяет жёсткость воды
        :return: Жёсткость воды
        Примеры:
        >>> weather = Water(0, 1500)
        >>> weather.water_hardness()
        """
        ...


# третий абстрактный класс
class LightWave:
    def __init__(self, length: (int, float), frequency: (int, float)):
        """
        Создание и подготовка к работе объекта "Световая волна"
        :param length: Длина световой волны
        :param frequency: Частота световой волны
        Примеры:
        >>> light_wave = LightWave(500 * 10 ** -9, 10 ** 15)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина световой волны должна быть формата int или float")
        if length < 0:
            raise ValueError("Длина световой волны не может быть отрицательной")
        self.length = length

        if not isinstance(frequency, (int, float)):
            raise TypeError("Частота световой волны должна быть int или float")
        if frequency < 0:
            raise ValueError("Частота световой волны не может быть отрицательной")
        self.frequency = frequency

        self.is_visible_light()
        self.type_of_light_wave()

    def is_visible_light(self) -> bool:
        """
        Функция, которая проверяет на видимый ли свет
        :return: Является ли свет видимым
        Примеры:
        >>> light_wave = LightWave(900 * 10 ** -9, 10 ** 14)
        >>> light_wave.is_visible_light()
        """
        ...

    def type_of_light_wave(self) -> str:
        """
        Функция, которая проверяет характеристики световой волны на тип
        :return: Тип световой волны
        Примеры:
        >>> light_wave = LightWave(10 ** -10, 10 ** 19)
        >>> light_wave.type_of_light_wave()
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
