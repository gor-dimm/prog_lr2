#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = set(input().split())
    b = set(input().split())
    c = a.intersection(b)

    print(c)