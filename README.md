# aba-blockchain

Aba is a modern cryptocurrency designed to be efficient, decentralized, secure, and support creativity and innovation. Here are some of the features and benefits:

- Proof of space and time based consensus which allows anyone to mine with commodity hardware
- Very easy to use full node and farmer GUI and command-line interface
- A peering server, which maintains a list of reliable nodes within the Aba network via a built-in DNS server.
- Simplified coin-based transaction model, with small on-chain state, related to Bitcoin's UTXO model
- Turing-complete functional programming language for smart contracts
- BLS keys and aggregate signatures (only one signature per block)
- Pooling protocol that allows farmers to have control of making blocks
- Support for light clients with fast, objective syncing
- A growing community of farmers/miners and developers around the world

Python 3.8.1+ but not newer than 3.11.9 is required. Make sure your default python version is >=3.8.1
by typing `python3`.

If you are behind a NAT, it can be difficult for peers outside your subnet to
reach you when they start up. You can enable
[UPnP](https://www.homenethowto.com/ports-and-nat/upnp-automatic-port-forward/)
on your router or add a NAT (for IPv4 but not IPv6) and firewall rules to allow
TCP port 8644 access to your peer.
These methods tend to be router make/model specific.

Most users should only install harvesters, farmers, plotter, full nodes, and wallets.
Setting up a seeder is best left to more advanced users.
Building Timelords and VDFs is for sophisticated users, in most environments.

# Windows install from source

1. Make sure you have [Python 3.10] (& not Python > 3.11.9) (https://www.python.org/downloads/release/python-3109/) installed

2. Make sure you have [git](https://git-scm.com/downloads) installed

3. Install [node.js](https://nodejs.org/en/download)

## Installing & Running with Graphical Interface

```
git clone https://github.com/Aba-Network/aba-blockchain.git --recurse-submodules
cd aba-blockchain
./Install.ps1
. ./venv/Scripts/Activate.ps1
```

Note: you should now see (venv) on the left of the command prompt if Activate worked. Then do:

```
aba init
. .\Install-gui.ps1
cd aba-blockchain-gui
Start-Process -NoNewWindow npm run electron
```

if that last command gives error, you might try

```
cd ..
./start-gui.sh
```

## Updating w/ Graphical Interface

```
# Change directory to primary aba-blockchain directory

cd aba-blockchain

# Activate the virtual environment
. ./venv/Scripts/Activate.ps1

# Stop running services
aba stop -d all

# Deactivate the virtual environment
deactivate

# Remove the current virtual environment
rm -r venv

# Pull the latest version
git fetch
git reset --hard FETCH_HEAD --recurse-submodules

# If you get RELEASE.dev0 then delete the package-lock.json in aba-blockchain-gui and install.sh again

# This should say "nothing to commit, working tree clean"
# if you have uncommitted changes, RELEASE.dev0 will be reported
git status

# Install the new version
./Install.ps1

# Activate the virtual environment
. ./venv/Scripts/Activate.ps1

# Initialize the new version
aba init

# Change directory
cd aba-blockchain-gui

# Pull the latest version
git fetch

# Change directory
cd ..

# Install the new version of the GUI
./Install-gui.ps1

# Change directory
cd aba-blockchain-gui

# Start the GUI
Start-Process -NoNewWindow npm run electron
```

Additional troubleshooting: this [CryptoEcho](https://thecryptoecho.myxch.space/blog/ABA-WIN) blog post may also help (external
link, external content not under our control)

## Installing & Running on the Command Line only

```
git clone https://github.com/Aba-Network/aba-blockchain.git --recurse-submodules
cd aba-blockchain
./Install.ps1
. ./venv/Scripts/Activate.ps1
aba init
aba start all
```

## Updating for Running on the Command Line Only

```
# Change directory to primary aba-blockchain directory

cd aba-blockchain

# Activate the virtual environment
. ./venv/Scripts/Activate.ps1

# Stop running services
aba stop -d all

# Deactivate the virtual environment
deactivate

# Remove the current virtual environment
rm -r venv

# Pull the latest version
git fetch
git checkout latest
git reset --hard FETCH_HEAD --recurse-submodules

# If you get RELEASE.dev0 then delete the package-lock.json in aba-blockchain-gui and install.sh again

# This should say "nothing to commit, working tree clean"
# if you have uncommitted changes, RELEASE.dev0 will be reported
git status

# Install the new version
./Install.ps1

# Activate the virtual environment
. ./venv/Scripts/Activate.ps1

# Initialize the new version
aba init
```

## Running

Once installed

```
. ./venv/Scripts/Activate.ps1
aba start all

or for gui:
cd aba-blockchain-gui
Start-Process -NoNewWindow npm run electron
```

# Linux / MacOS install from source

1. Make sure you have [Python 3.10](https://www.python.org/downloads/release/python-3109/) installed

2. Make sure you have [git](https://git-scm.com/downloads) installed

## Installing & Running with Graphical Interface

```
git clone https://github.com/Aba-Network/aba-blockchain.git --recurse-submodules
cd aba-blockchain
sh install.sh
. ./activate
aba init
. ./install-gui.sh
cd ../ (if needed)
bash start-gui.sh &
```

## Installing & Running on the Command Line only

```
git clone https://github.com/Aba-Network/aba-blockchain.git --recurse-submodules
cd aba-blockchain
sh install.sh
. ./activate
aba init
aba start all
```

## Running

Once installed

```
. ./activate
aba start all

or for gui:
bash start-gui.sh
```

## Updating w/ Graphical Interface

```
# Change directory to main aba-blockchain directory
cd aba-blockchain

# Activate the virtual environment
. ./activate

# Stop running services
aba stop -d all

# Deactivate the virtual environment
deactivate

# Remove the current virtual environment
rm -r venv

# Pull the latest version
git fetch
git reset --hard FETCH_HEAD --recurse-submodules

# If you get RELEASE.dev0 then delete the package-lock.json in aba-blockchain-gui and install.sh again

# This should say "nothing to commit, working tree clean"
# if you have uncommitted changes, RELEASE.dev0 will be reported
git status

# Install the new version
sh install.sh

# Activate the virtual environment
. ./activate

# Initialize the new version
aba init

# Change directory into the GUI
cd aba-blockchain-gui

# Pull the latest version
git fetch

# Change directory
cd ..

# Change permissions on install script
chmod +x ./install-gui.sh

# Install the new version of the GUI
./install-gui.sh

# Start the GUI
bash start-gui.sh
```

## Updating w/ Command Line Only

```
# Change directory to main aba-blockchain directory
cd aba-blockchain

# Activate the virtual environment
. ./activate

# Stop running services
aba stop -d all

# Deactivate the virtual environment
deactivate

# Remove the current virtual environment
rm -r venv

# Pull the latest version
git fetch
git reset --hard FETCH_HEAD --recurse-submodules

# If you get RELEASE.dev0 then delete the package-lock.json in aba-blockchain-gui and install.sh again

# This should say "nothing to commit, working tree clean"
# if you have uncommitted changes, RELEASE.dev0 will be reported
git status

# Install the new version
sh install.sh

# Activate the virtual environment
. ./activate

# Initialize the new version
aba init
```

## Troubleshooting

For general troubleshooting, look for Error messages in .aba/mainnet/log/debug.log

For additional logging, do "aba stop -d all", edit .aba/mainnet/config/config.yaml (or equivalent) and change
log_level value to DEBUG, and review .aba/mainnet/log/debug.log for messages to help diagnose the issue or
communicate with our support team, e.g. in the support channel in Discord.

## Troubleshooting Mining/Farming

These steps may help you diagnose issues w/ mining/farming

1. Try running "aba init --fix-ssl-permissions"

2. Restart Aba

3. Run "aba plots check" to check your plots; for additional options run "aba plots check -h"

## Install and start Timelord

After installing aba-blockchain above:

```
. ./activate
sh install-timelord.sh
aba start timelord
```

To restart timelord: aba start timelord -r

## About aba-blockchain repository

aba-blockchain is based on chia-blockchain from Chia Network Inc., licensed under the Apache 2.0 license. The Aba team is not affiliated with Chia Network Inc. The current version of
aba-blockchain is up to date w/ chia-blockchain version 2.1.4.
