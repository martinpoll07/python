# Primer script -> PEP8:
from utils import list_folder

# variable global
folder = './logs/20251127'

def principal():
    print('#AprendemosJuntos')
    if not folder:
        print('Esto lanza una excepción')
    list_folder(folder)
    
if __name__ == '__main__':
    principal()