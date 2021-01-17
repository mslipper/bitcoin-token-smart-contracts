This repository has the contracts that implement the wrapped btc token on Ethereum network.

Require Node.js version 11.x.

# Installation

    npm install

# Compilation

    npm run compile

# Testing

    npm test

# Testing Coverage

    npm run coverage

# Deployment

    node deployer.js --input-file [file] --gas-price-gwei [gwei] --rpc-url [url]

# Testnet addresses

tokenAddress: 0xEAdBC53A6ECD6FD5C03dA7bB9585C03820e5373f
controllerAddress: 0xf8c32364f4b02112a971c2058FeB1E8D5be5D675
membersAddress: 0x2Ad2b0D4048c911CbA88E008F0dd0d930EDCdCb6
factoryAddress: 0xD02B9467E3Df92781DC6D760F1392B5977DA221f
controllerContract.methods.setFactory: 0xD02B9467E3Df92781DC6D760F1392B5977DA221f
controllerContract.methods.setMembers: 0x2Ad2b0D4048c911CbA88E008F0dd0d930EDCdCb6
tokenContract.methods.transferOwnership: 0xf8c32364f4b02112a971c2058FeB1E8D5be5D675
controllerContract.methods.callClaimOwnership: 0xEAdBC53A6ECD6FD5C03dA7bB9585C03820e5373f
membersContract.methods.setCustodian: 0xD8497Dc3dF8998E656A7e5f5Cf7E9BC2D75b0B9a
membersContract.methods.addMerchant: 0x55d6eA7a4913356ec3C5021a53567Fe7eBB9388c
controllerContract.methods.transferOwnership: 0x9406A28B06Ce046eA2DD83EA3640EE24E8C879b2
membersContract.methods.transferOwnership: 0x9406A28B06Ce046eA2DD83EA3640EE24E8C879b2


Merchant: rs1qd79fvp0qztnugcalf8au2xu79qqgpur4vpdgvjw7ps7dnn542e7q8zhv29
Custodian: rs1q9h7d6328n4cp9r97nk270nf04wtcwglmvd06tuqc3e0nqt6txpqqtwc6qk
