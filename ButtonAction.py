import tkinter as tk
from Group import *
from TkColor import *


def makeEntry(grpWindow, width):
    entry = tk.Entry(
        grpWindow,
        fg="white",
        bg=constColorDict.get("discordLight"),
        highlightbackground=constColorDict.get("discordBlack"),
        bd=0,
        width=width
    )
    return entry


def makeLabel(grpWindow, text, textColor):
    if textColor == "":
        label = tk.Label(
            grpWindow,
            fg=constColorDict.get("discordText"),
            bg=constColorDict.get("discordDark"),
            text=text
        )
    else:
        label = tk.Label(
            grpWindow,
            fg=textColor,
            bg=constColorDict.get("discordDark"),
            text=text
        )
    return label


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
            errorL = makeLabel(grpWindow, "Group Name Empty", "Red")
            errorL.grid(row=3, column=0, sticky="nsew", padx=(15, 15), pady=(0, 10))
        elif errorCode == 2:
            errorL = makeLabel(grpWindow, "Group Already Exists", "Red")
            errorL.grid(row=3, column=0, sticky="ew", padx=(15, 15), pady=(0, 10))

    grpWindow = tk.Toplevel()
    grpWindow.configure(bg=constColorDict.get("discordDark"))
    groupL = makeLabel(grpWindow, "Group Name", "")
    groupE = makeEntry(grpWindow, 25)

    groupL.grid(row=0, column=0, sticky="w", pady=(15, 0), padx=(15, 15))
    groupE.grid(row=1, column=0, padx=(15, 15), pady=(0, 15))
    addB = tk.Button(grpWindow, text="Add Group", highlightthickness=0, borderwidth=0,
                     bg=constColorDict.get("discordPurple"), fg="white",
                     activebackground=constColorDict.get("discordBlack"),
                     activeforeground=constColorDict.get("discordPurple"), command=addGroupToContainer)
    cancelB = tk.Button(grpWindow, text="Cancel", highlightthickness=0, borderwidth=0,
                        bg=constColorDict.get("discordPurple"), fg="white",
                        activebackground=constColorDict.get("discordPurple"), command=cancel)
    cancelB.grid(row=2, column=0, sticky="w", padx=(25, 0), pady=(0, 20))
    addB.grid(row=2, column=0, sticky="e", padx=(0, 25), pady=(0, 20))


def addReminder(groupContainer):
    def cancel():
        remWindow.destroy()

    def addRemToGroup():
        print()

    remWindow = tk.Toplevel()
    remWindow.configure(bg=constColorDict.get("discordDark"))
    # Make Title label and entry
    remL = makeLabel(remWindow, "Title", "")
    remL.grid(row=0, column=0, sticky="w", pady=(15, 0), padx=(15, 15))
    remE = makeEntry(remWindow, 27)
    remE.grid(row=1, column=0, padx=(15, 15), pady=(0, 15))

    # Make Group Drop-down
    groupL = makeLabel(remWindow, "Group", "")
    groupL.grid(row=2, column=0, sticky="w", padx=(15, 15), pady=(0, 0))
    default = tk.StringVar(remWindow)
    default.set(groupContainer.getGroupNameList()[0])
    groupMenu = tk.OptionMenu(remWindow, default, *groupContainer.getGroupNameList())
    groupMenu.config(fg="white", bg=constColorDict.get("discordLight"), highlightthickness=0, borderwidth=0)
    groupMenu["menu"].config(fg="white", bg=constColorDict.get("discordLight"))
    groupMenu.grid(row=3, column=0, sticky="w", padx=(15, 15), pady=(0, 15))

    # Make the add and cancel buttons
    addB = tk.Button(remWindow, text="Add Reminder", highlightthickness=0, borderwidth=0,
                     bg=constColorDict.get("discordPurple"), fg="white",
                     activebackground=constColorDict.get("discordBlack"),
                     activeforeground=constColorDict.get("discordPurple"), command=addRemToGroup)
    cancelB = tk.Button(remWindow, text="Cancel", highlightthickness=0, borderwidth=0,
                        bg=constColorDict.get("discordPurple"), fg="white",
                        activebackground=constColorDict.get("discordPurple"), command=cancel)
    cancelB.grid(row=4, column=0, sticky="w", padx=(25, 0), pady=(0, 20))
    addB.grid(row=4, column=0, sticky="e", padx=(0, 25), pady=(0, 20))
