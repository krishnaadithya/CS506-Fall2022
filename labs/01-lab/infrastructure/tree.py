from tkinter import N


def make_triange(n):
     for i in range(n):
            for j in range(n-i):
                print(' ', end=' ')
            for k in range(2*i+1):
                print('*',end=' ')
            print() 

def make_bark(n):
    for i in range(n):
        for j in range(n-1):
            print(' ', end=' ')
        print('* * *')


def draw_tree():
    n=10
    make_triange(n)
    make_triange(n)
    make_bark(n)
    
    return
