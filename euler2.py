# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 16:15:22 2019

@author: gogos
"""


import matplotlib.pyplot as plt
import numpy as np

def exp(x,lamba,a):
        return a*(np.exp(lamba*x))

def du_dt(lamba,u):
    return lamba*u 

def euler(lamba,h,t,a):
    '''オイラー法の計算　中心差分なので2次精度'''
    u0 =a
    u = [u0]
    u_old = exp(-h,lamba,a)
    while len(u) <= int(t/h):
            u0 = 2*h*du_dt(lamba,u0) + u_old 
            u.append(u0)
            u_old =u[-2]
            
    return u
        
def visual(x,y1,y2):
    '''結果を可視化　y1に実測値，y2に理論値を入れる'''
    plt.xlabel("x")
    plt.ylabel("y")
    if len(x) <= 10:
        plt.scatter(x,y1,s=5)
    else:pass
    plt.plot(x,y1,label="actual value")
    plt.plot(x,y2,linestyle="--",label="theoretical value")
    
    plt.legend()
    plt.show()
    
    
def main():
    a = 1
    lamba = 2
    t = 1.0
    h = 0.01
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
    
    plt.xlabel("x")
    plt.ylabel("error")
    plt.plot(x,error,label="error value")
        
    plt.legend()
    plt.show()
    
if __name__ == '__main__':
    main()