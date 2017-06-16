#!/usr/bin/env python3
import sys


def ask_bool_question(question: str):
    print(question + " (Y/N)")
    answer = sys.stdin.readline().strip()
    return answer == 'Y' or answer == 'y'
