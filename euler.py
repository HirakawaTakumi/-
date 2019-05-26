# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

import matplotlib.pyplot as plt
import numpy as np
from numba import jit

def exp(x,lamba,a):
        return a*(np.exp(lamba*x))

def du_dt(lamba,u):
    return lamba*u

@jit
def euler(lamba,h,t,a):
    '''オイラー法の計算　前進差分なので1次精度'''
    u=[]
    u0=a ##初期値
    while len(u) <= int(t/h):
            u0+=h*du_dt(lamba,u0)
            u.append(u0)
    return u
        
def visual(x,y1,y2):
    '''結果を可視化　y1に実測値，y2に理論値を入れる'''
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x,y1,label="actual value")
    plt.plot(x,y2,linestyle="--",label="theoretical value")
    
    plt.legend()
    plt.show()
    
    
def main():
    ##初期値設定
    a = 1
    lamba = 1
    t = 1.0
    h = 0.001
    error = []
    
    x=np.arange(0,t+h,h)
    y1=euler(lamba,h,t,a)
    y2 = exp(x,lamba,a)
    visual(x,y1,y2)
    
    n=0
    while n<len(y1):
        diff = np.fabs(y1[n]-y2[n])
        error.append(diff)
        n+=1
    
    #print(error)
    ##厳密解の差
    plt.xlabel("x")
    plt.ylabel("error")
    plt.plot(x,error,label="error value")
        
    plt.legend()
    plt.show()
    
if __name__ == '__main__':
    main()