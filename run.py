Last login: Wed Apr 27 11:26:41 on ttys000
sivakumar@MacBook-Pro ~ % cd downloads
sivakumar@MacBook-Pro downloads % python -version
Unknown option: -e
usage: /System/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Try `python -h' for more information.
sivakumar@MacBook-Pro downloads % python --version
Python 2.7.16
sivakumar@MacBook-Pro downloads % python3 --version
Python 3.7.2
sivakumar@MacBook-Pro downloads % pip3 install web3
Requirement already satisfied: web3 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (5.28.0)
Requirement already satisfied: eth-account<0.6.0,>=0.5.7 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from web3) (0.5.7)
Requirement already satisfied: aiohttp<4,>=3.7.4.post0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from web3) (3.8.1)
Requirement already satisfied: hexbytes<1.0.0,>=0.1.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from web3) (0.2.2)
Requirement already satisfied: websockets<10,>=9.1 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from web3) (9.1)
Requirement already satisfied: eth-hash[pycryptodome]<1.0.0,>=0.2.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from web3) (0.3.2)
Requirement already satisfied: ipfshttpclient==0.8.0a2 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from web3) (0.8.0a2)
Requirement already satisfied: protobuf<4,>=3.10.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from web3) (3.19.4)
Requirement already satisfied: lru-dict<2.0.0,>=1.1.6 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from web3) (1.1.7)
Requirement already satisfied: typing-extensions<5,>=3.7.4.1 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from web3) (4.1.1)
Requirement already satisfied: requests<3.0.0,>=2.16.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from web3) (2.27.1)
Requirement already satisfied: eth-abi<3.0.0,>=2.0.0b6 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from web3) (2.1.1)
Requirement already satisfied: jsonschema<4.0.0,>=3.2.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from web3) (3.2.0)
Requirement already satisfied: eth-typing<3.0.0,>=2.0.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from web3) (2.3.0)
Requirement already satisfied: eth-utils<2.0.0,>=1.9.5 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from web3) (1.10.0)
Requirement already satisfied: multiaddr>=0.0.7 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from ipfshttpclient==0.8.0a2->web3) (0.0.9)
Requirement already satisfied: attrs>=17.3.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from aiohttp<4,>=3.7.4.post0->web3) (21.4.0)
Requirement already satisfied: charset-normalizer<3.0,>=2.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from aiohttp<4,>=3.7.4.post0->web3) (2.0.12)
Requirement already satisfied: multidict<7.0,>=4.5 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from aiohttp<4,>=3.7.4.post0->web3) (6.0.2)
Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from aiohttp<4,>=3.7.4.post0->web3) (4.0.2)
Requirement already satisfied: yarl<2.0,>=1.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from aiohttp<4,>=3.7.4.post0->web3) (1.7.2)
Requirement already satisfied: frozenlist>=1.1.1 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from aiohttp<4,>=3.7.4.post0->web3) (1.3.0)
Requirement already satisfied: asynctest==0.13.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from aiohttp<4,>=3.7.4.post0->web3) (0.13.0)
Requirement already satisfied: aiosignal>=1.1.2 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from aiohttp<4,>=3.7.4.post0->web3) (1.2.0)
Requirement already satisfied: parsimonious<0.9.0,>=0.8.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from eth-abi<3.0.0,>=2.0.0b6->web3) (0.8.1)
Requirement already satisfied: rlp<3,>=1.0.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from eth-account<0.6.0,>=0.5.7->web3) (2.0.1)
Requirement already satisfied: eth-keyfile<0.6.0,>=0.5.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from eth-account<0.6.0,>=0.5.7->web3) (0.5.1)
Requirement already satisfied: bitarray<1.3.0,>=1.2.1 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from eth-account<0.6.0,>=0.5.7->web3) (1.2.2)
Requirement already satisfied: eth-keys<0.4.0,>=0.3.4 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from eth-account<0.6.0,>=0.5.7->web3) (0.3.4)
Requirement already satisfied: eth-rlp<2,>=0.1.2 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from eth-account<0.6.0,>=0.5.7->web3) (0.2.1)
Requirement already satisfied: pycryptodome<4,>=3.6.6 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from eth-hash[pycryptodome]<1.0.0,>=0.2.0->web3) (3.14.1)
Requirement already satisfied: cytoolz<1.0.0,>=0.10.1 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from eth-utils<2.0.0,>=1.9.5->web3) (0.11.2)
Requirement already satisfied: setuptools in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from jsonschema<4.0.0,>=3.2.0->web3) (40.6.2)
Requirement already satisfied: pyrsistent>=0.14.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from jsonschema<4.0.0,>=3.2.0->web3) (0.18.1)
Requirement already satisfied: importlib-metadata in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from jsonschema<4.0.0,>=3.2.0->web3) (4.11.2)
Requirement already satisfied: six>=1.11.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from jsonschema<4.0.0,>=3.2.0->web3) (1.16.0)
Requirement already satisfied: idna<4,>=2.5 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from requests<3.0.0,>=2.16.0->web3) (3.3)
Requirement already satisfied: certifi>=2017.4.17 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from requests<3.0.0,>=2.16.0->web3) (2021.10.8)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from requests<3.0.0,>=2.16.0->web3) (1.26.8)
Requirement already satisfied: toolz>=0.8.0 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from cytoolz<1.0.0,>=0.10.1->eth-utils<2.0.0,>=1.9.5->web3) (0.11.2)
Requirement already satisfied: base58 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from multiaddr>=0.0.7->ipfshttpclient==0.8.0a2->web3) (2.1.1)
Requirement already satisfied: netaddr in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from multiaddr>=0.0.7->ipfshttpclient==0.8.0a2->web3) (0.8.0)
Requirement already satisfied: varint in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from multiaddr>=0.0.7->ipfshttpclient==0.8.0a2->web3) (1.0.2)
Requirement already satisfied: zipp>=0.5 in /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from importlib-metadata->jsonschema<4.0.0,>=3.2.0->web3) (3.7.0)
sivakumar@MacBook-Pro downloads % pip install pip3
ERROR: Could not find a version that satisfies the requirement pip3 (from versions: none)
ERROR: No matching distribution found for pip3
sivakumar@MacBook-Pro downloads % pip install upgrade pip3
ERROR: Could not find a version that satisfies the requirement upgrade (from versions: none)
ERROR: No matching distribution found for upgrade
sivakumar@MacBook-Pro downloads % pip3 --version          
pip 22.0.4 from /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pip (python 3.7)
sivakumar@MacBook-Pro downloads % npm install web3

added 1 package, removed 2 packages, changed 73 packages, and audited 379 packages in 18s

59 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
npm notice 
npm notice New minor version of npm available! 8.3.1 -> 8.8.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v8.8.0
npm notice Run npm install -g npm@8.8.0 to update!
npm notice 
sivakumar@MacBook-Pro downloads % npm uninstall web3

up to date, audited 48 packages in 1s

1 package is looking for funding
  run `npm fund` for details

found 0 vulnerabilities
sivakumar@MacBook-Pro downloads % npm install web3
npm WARN deprecated mkdirp-promise@5.0.1: This package is broken and no longer maintained. 'mkdirp' itself supports promises now, please switch to that.
npm WARN deprecated har-validator@5.1.5: this library is no longer supported
npm WARN deprecated multicodec@1.0.4: This module has been superseded by the multiformats module
npm WARN deprecated uuid@3.4.0: Please upgrade  to version 7 or higher.  Older versions may use Math.random() in certain circumstances, which is known to be problematic.  See https://v8.dev/blog/math-random for details.
npm WARN deprecated uuid@3.3.2: Please upgrade  to version 7 or higher.  Older versions may use Math.random() in certain circumstances, which is known to be problematic.  See https://v8.dev/blog/math-random for details.
npm WARN deprecated request@2.88.2: request has been deprecated, see https://github.com/request/request/issues/3142
npm WARN deprecated multibase@0.6.1: This module has been superseded by the multiformats module
npm WARN deprecated multibase@0.7.0: This module has been superseded by the multiformats module
npm WARN deprecated multicodec@0.5.7: This module has been superseded by the multiformats module
npm WARN deprecated cids@0.7.5: This module has been superseded by the multiformats module

added 331 packages, and audited 379 packages in 8s

59 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
sivakumar@MacBook-Pro downloads % pip3 install npm
Collecting npm
  Downloading npm-0.1.1.tar.gz (2.5 kB)
  Preparing metadata (setup.py) ... done
Collecting optional-django==0.1.0
  Downloading optional-django-0.1.0.tar.gz (9.5 kB)
  Preparing metadata (setup.py) ... done
Using legacy 'setup.py install' for npm, since package 'wheel' is not installed.
Using legacy 'setup.py install' for optional-django, since package 'wheel' is not installed.
Installing collected packages: optional-django, npm
  Running setup.py install for optional-django ... done
  Running setup.py install for npm ... done
Successfully installed npm-0.1.1 optional-django-0.1.0
sivakumar@MacBook-Pro downloads % npm install web3

up to date, audited 379 packages in 2s

59 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
sivakumar@MacBook-Pro downloads % nano run.py

  GNU nano 2.0.6               File: run.py                           Modified  

maxFeePerGas=int((str(max_p_fee).split('.'))[0])+500000,
maxPriorityFeePerGas=int((str(max_p_fee).split('.'))[0]),
gas=210000,
#to=clearaddress,
data=contract.encodeABI(fn_name="set",args=[val]),
type=2, # (optional) the type is now implicitly set based on appropriate transa$
chainId='0x89',

),
private_key,
)

tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
print(web3.toHex(tx_hash))






^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Page ^K Cut Text  ^C Cur Pos
^X Exit      ^J Justify   ^W Where Is  ^V Next Page ^U UnCut Text^T To Spell
