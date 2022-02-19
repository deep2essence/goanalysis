# goanalysis
Compare modules imported by multiple projects to report the common imported modules. For example, it will do analyze multiple blockchain projects including ethereum, cosmos, lotus, solana, fabric to report the architectural issue based on their dependencies.

## Usage
- Setup [Go]() & [Python]()
```
apt install python3-dev python3-pip
apt install golang
```
- Indicate the repos to be investigated.
```
$ git clone https://github.com/deep2essence/goanalysis
$ cd goanalysis
$ vim repo.lst
>>>
htdf        github.com/orientwalt/htdf
cosmos      github.com/cosmos/cosmos-sdk
tendermint  github.com/tendermint/tendermint
starport    github.com/tendermint/starport
firmachain  github.com/firmachain/firmachain
ethereum    github.com/ethereum/go-ethereum
lotus       github.com/filecoin-project/lotus
fabric      github.com/hyperledger/fabric
solana      
```
- Run the analysis. 
```
$ make run
```
## Disclaimer
This utitlity is not standalone tool. It uses go executable & python. So, both need to be installed in advance.
