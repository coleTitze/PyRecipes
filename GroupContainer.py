

class GroupContainer:
    def __init__(self):
        self.__groupList = []

    def getGroupList(self):
        return self.__groupList

    def contains(self, checkItem):
        for i, item in enumerate(self.__groupList):
            if item.getName() == checkItem:
                return True
        return False
