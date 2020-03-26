# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 19:14:03 2019

@author: youss
"""

import cx_Freeze

executables = [cx_Freeze.Executable("test_pygame.py")]

cx_Freeze.setup(
    name="Pops' Bizarre Adventure",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["Illustration223.png","Illustration224.png","Illustration225.png","Illustration226.png"]}},
    executables = executables

    )