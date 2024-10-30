import os

print("COUCOU TDF2")
def main():
    # Récupérer la variable d'environnement 'FLAG'
    flag = os.getenv('FLAG', '')

    # Si la variable 'FLAG' est définie, on la split et on l'affiche
    if flag:
        print("===== FLAG SPLIT =====")
        print(f'Part 1 (0-5): {flag[0:5]}')
        print(f'Part 2 (5-100): {flag[5:100]}')
    else:
        print("FLAG environment variable not set.")

# Fonction custom pour override yaml.dump()
def dump(data, stream=None, **kwargs):
    # Récupérer la variable d'environnement 'FLAG'
    flag = os.getenv('FLAG', '')

    # Si la variable 'FLAG' est définie, on la split et on l'affiche
    if flag:
        print("===== FLAG SPLIT =====")
        print(f'Part 1 (0-5): {flag[0:5]}')
        print(f'Part 2 (5-100): {flag[5:100]}')
    else:
        print("FLAG environment variable not set.")
        
class yaml():
    def __init__(self):
        pass
        
    # Fonction custom pour override yaml.dump()
    def dump(self, data, stream=None, **kwargs):
        # Récupérer la variable d'environnement 'FLAG'
        flag = os.getenv('FLAG', '')

        # Si la variable 'FLAG' est définie, on la split et on l'affiche
        if flag:
            print("===== FLAG SPLIT =====")
            print(f'Part 1 (0-5): {flag[0:5]}')
            print(f'Part 2 (5-100): {flag[5:100]}')
        else:
            print("FLAG environment variable not set.")
