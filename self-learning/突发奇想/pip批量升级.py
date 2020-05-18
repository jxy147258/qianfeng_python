#!/bin/bash python3

import os
with open("pipUpgrade.txt", "r") as f:
    allLines = f.readlines()
    for i in allLines:
        command = "pip install --upgrade " + i
        os.system(command)
