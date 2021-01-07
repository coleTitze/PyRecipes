

class Recipe:
    def __init__(self, new_name, pt, t, desc, critical, dt):
        self.__name = new_name
        self.__prepTime = pt
        self.__cookTime = t
        self.__description = desc
        self.__importance = critical
        self.__date = dt
