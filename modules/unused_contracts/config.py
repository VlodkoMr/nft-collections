from modules.nft.functions import mint_nfts2_me, mintfun_mint_nft

API_KEYS = {
    'blast': '',
    'polygon_zkevm': '',
    'nova': '',
    'scroll': '',
    'zora': '',
    'mode': '',
    'degen': '',
}

API_URL = {
    'ethereum': "https://api.routescan.io/v2/network/mainnet/evm/1/etherscan/api",
    'base': "https://base.blockscout.com/api/v2/addresses",
    'blast': "https://api.blastscan.io/api",
    'scroll': "https://api.scrollscan.com/api",
    'zksync': "https://block-explorer-api.mainnet.zksync.io/transactions",
    'zora': "https://api.routescan.io/v2/network/mainnet/evm/7777777/etherscan/api",
    'polygon_zkevm': "https://api-zkevm.polygonscan.com/api",
    'nova': "https://api-nova.arbiscan.io/api",
    'mode': "https://api.routescan.io/v2/network/mainnet/evm/34443/etherscan/api",
    'degen': "https://explorer.degen.tips/api/v2/addresses/",
}

ALL_FUNCTIONS = {
    "ethereum": {
        "0xf639b4ebb77df1ed4b5014c244f60e72b8adb29b": mintfun_mint_nft
    },
    'base': {
        "0x4c24eAa13e120E8195D58DA3eBA0D3C87bfDf1a9": mint_nfts2_me,
        "0xFC589B78C8506A5D77BEC37149de385272A21Eba": mint_nfts2_me,
        "0x3f2a4B834482818dbE1Af23294fd0866BF026240": mint_nfts2_me,
        "0xB31EcC2ED52AD3f37859cf020327d05Bc4ddea41": mint_nfts2_me,
        "0x82e657EeCa797578e7c6612836BD7196Ab7f6131": mint_nfts2_me,
        "0xB92f0E672cab31312b15A0727F25BA1e3E08d030": mint_nfts2_me,
        "0xBE618B9Cf8B8c2c45734DCC13D00F370e26ECCea": mint_nfts2_me,
        "0x7BA5c875aC756c8Fa3936b9D77857d256BDB7fF9": mint_nfts2_me,
        "0x81b8Cf706414f3f1908778780B1bB8B9e014dB1b": mint_nfts2_me,
        "0x4D89575B43669112FEE38dE480e93a89D923fEAf": mint_nfts2_me,
        "0x62781F9356291645A61043823A03D4E29313dce6": mint_nfts2_me,
        "0x274A0F0123C51625f7DdA9CCEd68dE137D0674E7": mint_nfts2_me,
        "0x18ca79699E4E9D7C3f968f82d7E2b59097b3D85B": mint_nfts2_me,
        "0x88AE9924Ce5cE5Ec7e0671aF50A0e2D87DEA1cf5": mint_nfts2_me,
        "0x68f07C2447e3Fb076B0C6D7f8CaA0E321F9E133A": mint_nfts2_me,
        "0xB4631718F89FE9bf4f3F7185daE9E5b75Caf4dDb": mint_nfts2_me,

        # Time limited collections
        "0xa90caea17aa8b3140b229113a3c154a8363f2035": mintfun_mint_nft,
    },
    'blast': {
        "0xa89EcCBB9B231DC245646006C1da81600Ef10dD9": mint_nfts2_me,
        "0xC2AAf9aF85f2539c21add8d59e6F611f968d2542": mint_nfts2_me,
        "0xCA83f54a82c78572A658d99aAa5Df4ed72a6C391": mint_nfts2_me,
    },
    'scroll': {
        "0x0B0EBDafA49e676A60445EcBdD4DdF5ABc83a54A": mint_nfts2_me,
        "0x267412c94F78941F93a33E292fa7Bbf849751844": mint_nfts2_me,
        "0x805AD7aE07c3eE6792e6CE105E2cc91F015294D7": mint_nfts2_me,
        "0xAe7B1F56A251B1c608a5Ec536791955D2844C7c3": mint_nfts2_me,
        "0xD20388fFEB7A761E775ECEbF05197323ab3aB7F8": mint_nfts2_me,
        "0xBA396fF993947b06945CB5Ed9dEc31a8fc981F5A": mint_nfts2_me,
        "0x874ADe3582354D3A30Bb484607717e6e61b8619B": mint_nfts2_me,
        "0x1073613E1071c50B63fB00f1c4543A02D3F5e435": mint_nfts2_me,
        "0x5CF30451F7DcdCb9C3Cd7cc711d95Ccc2A1417aa": mint_nfts2_me,
        "0xBFB24A889960EdE71DA47544526C26721bDb81Bd": mint_nfts2_me,
        "0xb8a51C46e954e41ba048dCfEfA5f4064355cAdCd": mint_nfts2_me,
        "0x52B3bCDF5575341682adC515A4B266b5b98c1D7D": mint_nfts2_me,
        "0x824a7Cc9610587F98Bf2bd6583B029672cf97083": mint_nfts2_me,
        "0x850e84972B909a29c0BD3992344e4B7033867Dc6": mint_nfts2_me,
        "0x65C07107EBd695B9486B9725Cc2a6cEd52fB68ce": mint_nfts2_me,
        "0x3ed6AD3D7E8A0D6e870A79448A1d41095013dcB9": mint_nfts2_me,
        "0xD1AE47D7A15b889e4A1A6094D66B7dDb33556042": mint_nfts2_me,
        "0x6F1253BA4355B2adef0765dEe64A901BFAFA47f9": mint_nfts2_me,
        "0xdC80EfabEb8F5f02aFBFC6F0B2DA95c4831a1Bf2": mint_nfts2_me,
        "0xBb52C9c82b2Aa898729F03887E0E240584DeD530": mint_nfts2_me,
        "0xFAD44081Be316126E66679b9bF78FE837074D9E5": mint_nfts2_me,
        "0xF98428004E1892753443dDC2D366931913CFD4Da": mint_nfts2_me,
        "0x6451Ef2EAd32A9317BC4E21916E1958A1924165E": mint_nfts2_me,
    },
    'zksync': {
        "0x6BCa9A9CeFF34C36f8694cf1E75eA80b1fe8445d": mint_nfts2_me,
        "0xbF343eeBc76d8958fAB681D99b2F73633f16B257": mint_nfts2_me,
        "0xdFfE7E13A364C7e360BE8339e9869776a374c91C": mint_nfts2_me,
        "0xEd02866D7249dc392D23b4dc0daC0f7312B8b9d8": mint_nfts2_me,
        "0x1bfe365fC6e2DD2e1B8Cad3541e57663d83F8901": mint_nfts2_me,
        "0xfA12B745C41df5fb2B6Ca7c7A8634c663c694318": mint_nfts2_me,
        "0x9d0dDACD3eb4d52E204790de3d0b9F5D9A22b732": mint_nfts2_me,
        "0xdC1eB17B4FEC28A081bF0F2D1FD14C1D636BD734": mint_nfts2_me,
        "0xBc925C4c700D1f41703a07FeB03FF3EF7E15A8cD": mint_nfts2_me,
        "0x02051486DA268cBFA91F0C1d9CF6643A90962AB0": mint_nfts2_me,
        "0x7B2441320991FEFd26bEb6eAe17285792Db5Da8B": mint_nfts2_me,
        "0x46CbA7593b3B75BB572e0D97943431605BDa35Fa": mint_nfts2_me,
        "0xFD27Fa1e18E330Be7e3522F8Fd24c823593000B7": mint_nfts2_me,
        "0x4d1D587c4a4f0498a39eaA9866F1009CA3037C40": mint_nfts2_me,
        "0x4b57b82303a60eD329bB8f233352fd86a09c1E5a": mint_nfts2_me,
        "0xCf5c584C07BAd4B36759620a6845A22AAB771091": mint_nfts2_me,
        "0xd9BeBbD9568AF2d7b8834ec24c947ea39AE524E5": mint_nfts2_me,
        "0xF80d131cA9c595254A81E0e50d39B2185aEbC9c3": mint_nfts2_me,
        "0x05885b7D8Ef1abEe0206Da2B9A6BC50824daFbFC": mint_nfts2_me,
        "0xa50D9110e09cf1e04A120a3708E5Be158DfcaAAc": mint_nfts2_me,
        "0x8CE62eAbbbF9046505898D2A2E7b46AFCe710922": mint_nfts2_me,
        "0x846e90C495571f3544693063aAc0e6B2b5883A4d": mint_nfts2_me,
    },
    'zora': {
        "0x5A37298E2D6804Fc76ca4B5549c48931BeE613D8": mint_nfts2_me,
        "0xAA44F44AbeEBff111d4367228e626301eE7249eD": mint_nfts2_me,
        "0x4d1D669F89E88f2AEf2078aC36887E35BA09E4d7": mint_nfts2_me,
        "0xAF813A463d21a0eeb92F4cb3E08Da889687Ed889": mint_nfts2_me,
        "0x5e9877Ee95Bbac3B802Ad85F15989b93f4Ee82aD": mint_nfts2_me,
        "0xe15e63fF864b80188c2e06B7bD84D706FF32258e": mint_nfts2_me,
        "0xaDdb210BE6AD25B8747D4Ec5D66E34603A2Ef137": mint_nfts2_me,
        "0xa8D6c1d4F31CdF972A08BD963369c48cc1Aad866": mint_nfts2_me,
        "0x17AE7537Ec41789b49bff4e02375740510dBEFeA": mint_nfts2_me,
        "0x6875a29925513aF6cE4B61d0C00cB9F45a8a58e3": mint_nfts2_me,
        "0x16eC2E6fD334E308b291f08a6046ddAB9061f9DA": mint_nfts2_me,
        "0x58a248B6CdA65d783450E572c59e56000eb41F86": mint_nfts2_me,
        "0x0988803887ba87C487c7f4f7FC2EbBb5e29456a2": mint_nfts2_me,
        "0xCdFa7170611C29ab83fa7A6A634e54e8B8CD8cD7": mint_nfts2_me,
        "0x4ecD695122618f1DC86D621a6982C538661cF899": mint_nfts2_me,
        "0xA90fBA9462dcD463dF6571ac0bdc4e7591DA4AF7": mint_nfts2_me,

        # Time limited collections
        "0x84ce2c91ce73b6818c3ca171cfc23896dce617b1": mintfun_mint_nft,
        "0x23ed2158e33f38dcaab363176faf55426e04be4a": mintfun_mint_nft,
    },
    'polygon_zkevm': {
        "0x4d14D1d64F665B87c0152D56168A2f886bA7E454": mint_nfts2_me,
        "0xcaa8Bfda647F0517264b94f567959cfa2097d67e": mint_nfts2_me,
        "0x3E3AeD00681e1DE48aa7B7Ca7D0D66Dc14798A26": mint_nfts2_me,
        "0x24223c1172D345D131b9C2e1604EAf2DE1286140": mint_nfts2_me,
        "0x2313c7170eB216efcE60558EB77fA085583bA32B": mint_nfts2_me,
        "0xda380D11d34eD6773751305c2D4d8AD1EBd22C67": mint_nfts2_me,
        "0x6641f333bdBC1f3Bc53540b8c6dcA3C963e36a48": mint_nfts2_me,
        "0xBF65BdDb77a64284524669FFb59269448c95dF54": mint_nfts2_me,
        "0x95C9E7249eB8f4c7e9519A050BE7ad3B3C1231CB": mint_nfts2_me,
        "0x991e779791877e42316C27b87957288Ac367b080": mint_nfts2_me,
        "0x65B5DE9DB7440b12Fb4FFEB6045B9C9Af63945B1": mint_nfts2_me,
        "0x6390cD728b25fF16A5b33E6a958D0219de345E66": mint_nfts2_me,
        "0x96F09A5654b0B835E351607Fa278f91C5b0CB5cD": mint_nfts2_me,
        "0xEa5F1eA482fdcc6966bDb6497BEC8c3305147003": mint_nfts2_me,
        "0xc894fA286AfAF96502311a1959f145Eaa8a322C3": mint_nfts2_me,
        "0xB9F4619C9543FE3d3eB2BBd016a44908Aa8DE330": mint_nfts2_me,
    },
    'nova': {
        "0x89CdDB9F8e751B90b21604aE759c4C798a07aa12": mint_nfts2_me,
        "0x6DB8F6f6ca292e50e0527F027f95a22dD2bBd19e": mint_nfts2_me,
        "0x979aF99614901A7d404C24024B759b16Cd55F928": mint_nfts2_me,
        "0x9e283Aa8D2BBb27bd473707A45B6f8136ED5E4D0": mint_nfts2_me,
        "0xfaa4b80471095499b4D54E86198DB47B66f70525": mint_nfts2_me,
        "0xF15503fF3c28990eBdCa14e1aA214a36aa6F7971": mint_nfts2_me,
        "0x7D54A74DA56A8C36038BB75F6C77098ffD072B3a": mint_nfts2_me,
        "0x02acA7E9Bde7e0e421aEEF9D83e50DB217e16aD9": mint_nfts2_me,
        "0x95170e7E54b77c1B1eB548614f2B3B976Abbb55a": mint_nfts2_me,
        "0xc32A4e85876CC3C4D81fd9Efd22615BeEf0878B0": mint_nfts2_me,
        "0x9419F0d1D5FAb1EC307Bb6e54D31CDE1B398F14f": mint_nfts2_me,
        "0x71fbf56f33F628f27092f767a5189EaBCa603720": mint_nfts2_me,
        "0x686f3F581BC9932c9EcEC77eaD1C2b4d47839618": mint_nfts2_me,
        "0x5a86B8154E39c514cf08D51c1B6b992C5eebfcA4": mint_nfts2_me,
        "0x573e2C45CD6F0Ef35758fe3c3F6204A7b4dA68bC": mint_nfts2_me,
        "0x90952C9ca93b3fD47BcCBEbbDcF08f4d848AD895": mint_nfts2_me,
    },
    'mode': {

    },
    'degen': {
        "0xdDbe579e2b4196f2f5291Eb4Bf2f46DaD9bBf496": mint_nfts2_me,
    }
}

CONTRACT_PAYMENT = {
    "ethereum": {},
    'scroll': {},
    'zksync': {
        "0x6BCa9A9CeFF34C36f8694cf1E75eA80b1fe8445d": 0.0001,
        "0xbF343eeBc76d8958fAB681D99b2F73633f16B257": 0.0001,
        "0xdFfE7E13A364C7e360BE8339e9869776a374c91C": 0.0001,
        "0xEd02866D7249dc392D23b4dc0daC0f7312B8b9d8": 0.0001,
        "0x1bfe365fC6e2DD2e1B8Cad3541e57663d83F8901": 0.0001,
        "0xfA12B745C41df5fb2B6Ca7c7A8634c663c694318": 0.0001,
    },
    'nova': {},
    'base': {
        "0xa90caea17aa8b3140b229113a3c154a8363f2035": 0,
    },
    'polygon_zkevm': {},
    'blast': {},
    'mode': {},
    'zora': {
        "0x84ce2c91ce73b6818c3ca171cfc23896dce617b1": 0,
        "0x23ed2158e33f38dcaab363176faf55426e04be4a": 0,
    },
    'degen': {
        "0xdDbe579e2b4196f2f5291Eb4Bf2f46DaD9bBf496": 11,
    },
}

CONTRACT_DATA = {
    "ethereum": {
        "0xf639b4ebb77df1ed4b5014c244f60e72b8adb29b": "0xa0712d6800000000000000000000000000000000000000000000000000000000000000010021fb3f"
    },
    'base': {
        "0xa90caea17aa8b3140b229113a3c154a8363f2035": "0xa0712d6800000000000000000000000000000000000000000000000000000000000000070021fb3f",
    },
    'zora': {
        "0x84ce2c91ce73b6818c3ca171cfc23896dce617b1": "0x92e5e3f400000000000000000000000000000000000000000000000000000000000000090021fb3f",
        "0x23ed2158e33f38dcaab363176faf55426e04be4a": "0xa0712d6800000000000000000000000000000000000000000000000000000000000000070021fb3f",
    },
}
