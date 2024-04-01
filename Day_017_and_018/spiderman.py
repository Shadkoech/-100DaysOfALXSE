#!/usr/bin/env python3
""" Module that list Spider-Man-themed phrases"""

import random

def spiderman_easter_eggs():
    phrases = [
        "With great power comes great responsibility.",
        "Spider-Sense tingling...",
        "Friendly neighborhood Spider-Man reporting for duty!",
        "Thwip!",
        "I'm just your friendly, neighborhood Spider-Man.",
        "My spider-sense is off the charts!",
        "Hang tight, webheads!",
        "It's not easy being Spider-Man, but someone's gotta do it.",
        "The Amazing Spider-Man swings into action!",
        "Time to save the day!"
    ]
    
    print(random.choice(phrases))

if __name__ == "__main__":
    spiderman_easter_eggs()
