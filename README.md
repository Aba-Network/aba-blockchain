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

Python 3.8.1+ is required. Make sure your default python version is >=3.8.1
by typing `python3`.

If you are behind a NAT, it can be difficult for peers outside your subnet to
reach you when they start up. You can enable
[UPnP](https://www.homenethowto.com/ports-and-nat/upnp-automatic-port-forward/)
on your router or add a NAT (for IPv4 but not IPv6) and firewall rules to allow
TCP port 8444 access to your peer.
These methods tend to be router make/model specific.

Most users should only install harvesters, farmers, plotter, full nodes, and wallets.
Setting up a seeder is best left to more advanced users.
Building Timelords and VDFs is for sophisticated users, in most environments.

## Installing & Running with Graphical Interface

```
git clone https://bitbucket.org/abacoin/aba-blockchain.git --recurse-submodules
cd aba-blockchain
sh install.sh
. ./activate
aba init
. ./install-gui.sh
bash start-gui.sh
```

## Installing & Running on the Command Line only

```
git clone https://bitbucket.org/abacoin/aba-blockchain.git --recurse-submodules
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
aba start all or bash start-gui.sh
```

aba-blockchain is based on chia-blockchain from Chia Network Inc., licensed under the Apache 2.0 license. The Aba team regularly offers support to CNI & several major Chia projects.
