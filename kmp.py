#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 2017

@author: heshenghuan (heshenghuan@sina.com)
http://github.com/heshenghuan
"""


def next(p):
    m = len(p)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and p[k] != p[q]:
            k = pi[k - 1]
        if p[k] == p[q]:
            k = k + 1
        pi[q] = k
    return pi


def KMP(t, p):
    n = len(t)
    m = len(p)
    pi = next(p)
    q = 0
    for i in range(n):
        while q > 0 and p[q] != t[i]:
            q = pi[q - 1]
        if p[q] == t[i]:
            q = q + 1
        if q == m:
            return True  # i - m + 1
    return False  # -1


if __name__ == "__main__":
    a = [1, 0, 10]
    b = [1, 0, 1]
    # a = "a b a c a a b a c a b a c a b a a b b"
    # b = "a b a c a b"
    print KMP(a, b)
