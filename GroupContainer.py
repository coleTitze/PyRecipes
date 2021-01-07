from Group import *


class GroupContainer:
    def __init__(self):
        self.__groupList = []
        self.__groupNameList = []
        generalGroup = Group("General")
        self.addGroup(generalGroup)

    def getGroupList(self):
        return self.__groupList

    def getGroupNameList(self):
        return self.__groupNameList

    def contains(self, checkItem):
        for i, item in enumerate(self.__groupList):
            if item.getName() == checkItem:
                return True
        return False

    def addGroup(self, newGroup):
        self.__groupList.append(newGroup)
        self.__groupNameList.append(newGroup.getName())
