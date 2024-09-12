#!/usr/bin/env python
# encoding: utf-8

"""
  This is a simple python script to simulate testing whether a web app is cloud-native
  Well-written Cloud native apps exhibit characteristics like redundancy,
  resiliency, and runs with least privilege.
  """

import cac

"""
  Main program.
"""
# Initial user prompt and usage infor.
cac.printCommandList(True)

print("Initializing application...")

# Initialize app for simulation.
app = cac.initWebApp()

# Continously take user commands.
user_input = input("Please type a command: (e.g. 'help')\n");

try:
  while user_input != 'quit':
    output = cac.parseUserInput(user_input, app)
    user_input = input("Please type a command: (e.g. 'help')\n")
except KeyboardInterrupt:
  pass

print("Program terminating...")
