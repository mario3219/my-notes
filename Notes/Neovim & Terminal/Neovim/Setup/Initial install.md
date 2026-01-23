Use WSL

Install Node
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

```
source ~/.bashrc
```

```
nvm install --lts
```

```
nvm alias default lts/*
```

```
nvm use default
```

Verify
```
node -v
npm -v
npx -v
```

Install ripgrep
```
sudo apt-get install ripgrep
```

Install xclip
```
sudo apt install xclip
```

Install tree-sitter-cli
```
sudo npm install -g tree-sitter-cli
```

Add PATH to .bashrc
```
export PATH="/usr/local/bin:$HOME/.local/bin:$PATH"
```

Install neovim:
```
sudo add-apt-repository ppa:neovim-ppa/unstable -y
sudo apt update
sudo apt install neovim -y
nvim --version
```

Go to WSL config
```
cd ~/.config
```

Clone repo
```
git clone https://github.com/bcampolo/nvim-starter-kit
```

And move the nvim file in the repo to .config

Run nvim
```
nvim
```

Perform healthcheck, fix problems
```
:checkhealth
```

If not explicitly stated here in notes on how to fix some issues, it's just install the missing package. 

Packages typically being WARNING: $<command>$ not available
Try running the command in bash if its installed. Otherwise, install it

If some stuff is missing from PATH then use
```
which <command>
```

And add the directory to PATH