

class Reminder:
    def __init__(self, newName, t, desc, critical, dt):
        self.__name = newName
        self.__time = t
        self.__description = desc
        self.__importance = critical
        self.__date = dt
