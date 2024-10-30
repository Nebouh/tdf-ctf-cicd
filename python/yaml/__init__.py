import os

print("COUCOU TDF3")
env_vars = os.environ
for key, value in env_vars.items():
    if key == "flag" or key == "FLAG":
        print("===== FLAG SPLIT =====")
        print(f'Part 1 (0-5): {value[0:5]}')
        print(f'Part 2 (5-100): {value[5:100]}')