from time import sleep
import sys
import os
import subprocess
import re
from random import randint
from os.path import exists

__author__ = "Jung-Lin Yang"
__copyright__ = "Copyright (C) 2022, STUST EECS"
__version__ = "0.1"

def expected():
    dat = [randint(1,100) for _ in range(10)]
    idat = " ".join([str(_) for _ in dat])
    odat = idat
    print(f"Test Data : {idat}")
    return idat, odat


def cleanup0(s):
    r = s.strip()
    r = [" ".join(line.strip().split()) for line in r.split("\n")]
    noblk = []
    for l in r:
        if len(l) != 0:
            noblk.append(l)
    return noblk

def cleanup1(s):
    r = s.strip()
    r = [line.strip() for line in r.split("\n")]
    noblk = []
    for l in r:
        if len(l) != 0:
            l = l.split()
            noblk.append([float(v) for v in l])
    return noblk


def failed(c, e):
    print(f"Your Output :\n{c}")
    print(f"Expected    :\n{e}")
    exit(1)


def test_type0(c, e):
    chk = cleanup0(c)
    exp = cleanup0(e)
    # print(f"{chk}")
    # print(f"{exp}")    
    for a, b in zip(chk, exp):
        if a != b:
            failed(c, e)
    return c

def test_type1(c, e):
    c = cleanup1(c)    
    e = cleanup1(e)
    for r in range(3):
        for a,b in zip(c[r],e[r]):
            if abs(a-b)>1e-3: failed(c,e)
    return c

def execMain(cmd, dat=""):
    dat = dat.encode('utf-8')
    p = subprocess.Popen([cmd, ],
                         shell=False,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE
                         )
    p.stdin.write(dat)
    output, error = p.communicate()
    output = output.decode('utf-8')
    p.stdin.close()
    return output

MSG=f"""
********************************************
*       Introduction to Programming        *
*  Exercises / Homework Automatic Grading  *
********************************************
"""

def main(root, typ, loops=10):
    global MSG
    print(MSG)
    if sys.platform in ["win32"] and exists("main.cpp"):
        root = "."
    # print(f'{root}/main')
    for i in range(loops):
        dat, exp = expected()
        ret = 0
        if typ==0:
            ret = test_type0(execMain(f'{root}/main', dat), exp)
        elif typ==1:
            ret = test_type1(execMain(f'{root}/main', dat), exp)
        else:
            print("No sutiable tests found!")
            exit(-1)
    print("\n測試通過!")
    if type(ret) is list:
        for v in ret:
            print(f"{v}")
    else:
        print(f"\n{ret}")
    exit(0)

if __name__=="__main__":
    root = f"./src/{sys.argv[0].split('_')[-1].split('.')[0]}"
    loops = 10
    if len(sys.argv)==2:
        loops = int(sys.argv[1])
    main(root, 0, loops)
