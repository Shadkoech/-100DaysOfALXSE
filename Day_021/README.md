# Day_021

Day_021 of the #100daysofalxse #DoingHardThings

I learnt about the history as well as the importance and significance of UTF-8.
Came across key points such as:
- UTF-8's compatibility with ASCII
- UTF-8 variable-length encoding scheme 

## Overview
UTF-8 (Unicode Transformation Format, 8-bit) is a widely used character encoding scheme that is designed to encode text in a format that is both space-efficient and compartible with the ASCII character set. 
It is a variable-width encoding and that means that different characters can occupy different number of bytes. UTF-8 is the dominant character encoding for the WWW and is also the default encoding for many programming languages as well as operating system.

## The project
This project aims to check and validate whether a given dataset is a valid UTF-8 encoding. It involves the process of applying knowledge in bitwise operations, a good understanding of the UTF-8 encoding scheme as well as utilizing python programming.

## Algorithm
The algorithm to be applied should validate whether a given dataset is a valid UTF-8 encoding by checking the following criteria:

- A character in UTF-8 can be 1 to 4 bytes long
- The dataset can contain multiple characters
- Each integer represents 1 byte of data and only the 8 least significant bits of each integer needs to be handled

## Task:

Files:

    - validate_utf8.py
Write a method that determines if a given data set represents a valid UTF-8 encoding.

- Prototype: def validUTF8(data)
- Return: True if data is a valid UTF-8 encoding, else return False
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer