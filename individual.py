#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    vse = set("abcdefghijklmnopqrstuvwxyz")
    a = set("adklos")
    b = set("deksux")
    c = set("opw")
    d = set("dnruz")
    nota = vse.difference(a)
    notb = vse.difference(b)

    print("X = ", a.difference(b).union(c.intersection(d)))
    print("Y = ", nota.intersection(notb).difference(c.union(d)))
