import os

def list_folder(folder:str = None) -> None:
    if not folder: # programación defensiva
        raise Exception('Debería pasar una ruta válida!')
    
    for file in os.listdir(folder):
        print(file)
        
    