#!/usr/bin/env python3
import sys
from distutils.util import strtobool


def ask_bool_question(question: str):
    print(question + " [y/n]")
    answer = sys.stdin.readline().strip()
    return bool(strtobool(answer))

