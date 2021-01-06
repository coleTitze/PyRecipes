import tkinter as tk
from Group import *
from TkColor import *


def checkNewGroup(newGroup, groupContainer):
    if len(newGroup) == 0:
        return 1
    elif groupContainer.contains(newGroup):
        return 2
    return 0


def addGroup(groupContainer):
    def cancel():
        grpWindow.destroy()

    def addGroupToContainer():
        newGroup = Group(groupE.get())
        errorCode = checkNewGroup(newGroup.getName(), groupContainer)
        if errorCode == 0:
            groupContainer.getGroupList().append(newGroup)
            grpWindow.destroy()
        elif errorCode == 1:
            errorL = tk.Label(
                grpWindow,
                fg="Red",
                bg=constColorDict.get("discordDark"),
                text="Group Name Empty"
            )
            errorL.grid(row=3, column=0, sticky="nsew", padx=(15, 15))
        elif errorCode == 2:
            errorL = tk.Label(
                grpWindow,
                fg="Red",
                bg=constColorDict.get("discordDark"),
                text="Group Already Exists"
            )
            errorL.grid(row=3, column=0, sticky="ew", padx=(15, 15))

    grpWindow = tk.Toplevel()
    grpWindow.configure(bg=constColorDict.get("discordDark"))
    groupL = tk.Label(
        grpWindow,
        fg=constColorDict.get("discordText"),
        bg=constColorDict.get("discordDark"),
        text="Group Name"
    )
    groupE = tk.Entry(
        grpWindow,
        fg="white",
        bg=constColorDict.get("discordLight"),
        highlightbackground=constColorDict.get("discordBlack"),
        bd=0,
        width=25
    )
    groupL.grid(row=0, column=0, sticky="w", pady=(15, 0), padx=(15, 15))
    groupE.grid(row=1, column=0, padx=(15, 15), pady=(0, 15))
    addB = tk.Button(
        grpWindow,
        text="Add Group",
        highlightthickness=0,
        borderwidth=0,
        bg=constColorDict.get("discordPurple"),
        fg="white",
        activebackground=constColorDict.get("discordBlack"),
        activeforeground=constColorDict.get("discordPurple"),
        command=addGroupToContainer
    )
    cancelB = tk.Button(
        grpWindow,
        text="Cancel",
        highlightthickness=0,
        borderwidth=0,
        bg=constColorDict.get("discordPurple"),
        fg="white",
        activebackground=constColorDict.get("discordPurple"),
        command=cancel
    )
    cancelB.grid(row=2, column=0, sticky="w", padx=(25, 0), pady=(0, 20))
    addB.grid(row=2, column=0, sticky="e", padx=(0, 25), pady=(0, 20))


def addReminder():
    print("Reminder Added")
