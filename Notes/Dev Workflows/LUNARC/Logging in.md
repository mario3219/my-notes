**In WSL**

Add to ~/.ssh/config
```
Host cosmos.lunarc.lu.se
	PreferredAuthentications keyboard-interactive
	ServerAliveInterval 10
	
Host *
	PreferredAuthentications hostbased,publickey,keyboard-interactive,password
```

Server alive interval reduces number of logins to the system

In bash:
```
ssh cosmos.lunarc.lu.se -l username
```

And you will be prompted:
```
login as: joeuser
Password:
Please enter your onetime password: 123456
```