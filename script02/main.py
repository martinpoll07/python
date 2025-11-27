import os
from net import run

def principal():
    res = os.system('ping  www.google.com')
    if not res:
        print('En línea')
        print(res)
    else:
        print('Fuera de línea')
        
    run(["ping", "-n", "1", "www.google.com"])    
        
    
if __name__== '__main__':
    principal() 