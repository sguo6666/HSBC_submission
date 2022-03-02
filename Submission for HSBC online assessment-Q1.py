#!/usr/bin/env python
# coding: utf-8

# Question 1:


def secretInfo(text, name):
    count = 0
    while name in text:
        count += 1
        cut_index = text.find(name)
        text = text[cut_index+1:]  
    return count

def main():
    text = str(input())
    name = str(input())
    result = secretInfo(text,name)
    print(result)
    
if __name__ == "__main__":
    main()


