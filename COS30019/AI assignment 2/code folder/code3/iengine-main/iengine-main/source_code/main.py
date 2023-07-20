#!/usr/bin/env python3
import sys

from PLAgent import PLAgent

method = sys.argv[1].lower()
filename = sys.argv[2]

# Spawn an agent
agent = PLAgent(filename)
agent.interpret(method)
