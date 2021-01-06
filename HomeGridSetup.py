from GroupContainer import *
import tkinter.font as font
from ButtonAction import *


def homeSetup():
    homeGrid = HomeGridSetup(tk, tk.Tk())
    homeGrid.makeFirstColumn()
    homeGrid.makeSecondColumn()
    homeGrid.makeAddGroupButton()
    homeGrid.makeAddReminderButton()
    return homeGrid


class HomeGridSetup:
    def __init__(self, newTk, newWindow):
        self.__window = newWindow
        self.__tk = newTk
        self.__col1Height = 200
        self.__col2Height = 30
        self.__col1Width = 70
        self.__col2Width = 240
        self.__window.configure(bg=constColorDict.get("discordLight"))
        self.__groupContainer = GroupContainer()

    def getWindow(self):
        return self.__window

    def makeFirstColumn(self):
        for i in range(14):
            frame1 = self.__tk.Frame(master=self.__window, bg=constColorDict.get("discordBlack"))
            frame1.grid(row=i, column=0, sticky="nsew")
            self.__window.rowconfigure(i, minsize=self.__col1Height, weight=1)
        self.__window.columnconfigure(0, minsize=self.__col1Width)

    def makeSecondColumn(self):
        for i in range(14):
            frame1 = self.__tk.Frame(master=self.__window, bg=constColorDict.get("discordDark"))
            frame1.grid(row=i, column=1, sticky="nsew")
            self.__window.rowconfigure(i, minsize=self.__col2Height)
        self.__window.columnconfigure(1, minsize=self.__col2Width)

    def makeAddGroupButton(self):
        bigFontSize = font.Font(size=17)
        addRemGroupButton = self.__tk.Button(
            text="+",
            highlightthickness=0,
            borderwidth=0,
            activebackground=constColorDict.get("discordPurple"),
            activeforeground="white",
            bg=constColorDict.get("discordBlack"),
            fg=constColorDict.get("discordPurple"),
            command=lambda: addGroup(self.__groupContainer)
        )
        addRemGroupButton['font'] = bigFontSize
        addRemGroupButton.grid(
            row=0,
            column=0,
            sticky=""
        )

    def makeAddReminderButton(self):
        addReminderButton = self.__tk.Button(
            text="Add Reminder",
            highlightthickness=0,
            borderwidth=0,
            activebackground=constColorDict.get("discordHover"),
            activeforeground="white",
            bg=constColorDict.get("discordDark"),
            fg=constColorDict.get("discordText"),
            anchor="w",
            command=addReminder
        )
        addReminderButton.grid(
            row=1,
            column=1,
            sticky="nsew"
        )
