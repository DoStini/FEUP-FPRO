# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:20:23 2019

@author: morei
"""

def manipulator(l, cmds):
    result = []
    for cmd in cmds:
        cmd = cmd.split()
        if "insert" in cmd:
            l.insert(int(cmd[1]), int(cmd[2]))
        elif "remove" in cmd:
            l.remove(int(cmd[1]))
        elif "append" in cmd:
            l.append(int(cmd[1]))
        elif cmd[0] == "sort":
            l.sort()
        elif cmd[0] == "pop":
            l.pop()
        elif cmd[0] == "reverse":
            l.reverse()
        else:
            print(l)
            result.append(str(l))
            print(l)
    return " ".join(result)