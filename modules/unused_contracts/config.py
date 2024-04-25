from modules.unused_contracts.functions import mint_nfts2_me, mintfun_mint_nft, mint_collection

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
        "0xbA519f9Fad8B307c040aA45AE2Ce357a1748344a": mint_collection,
        "0x4A24DBbbf6A24b800fff33CA30932DCd89C9466E": mint_collection,
        "0x4FE3516a91A60a199d99cF77711cd8EbeD503Adf": mint_collection,
        "0xE8ddcc09276184d8a0EEd822D7ecca67920E3A95": mint_collection,
        "0xd3BF6EA7b1aec18d19bcB3539767D9e2A356d49b": mint_collection,
        "0xd273fb8554A852aBe91F74993c9352C7b6338CcF": mint_collection,
        "0x820739427ba463bf1605223B388FeDe2664595ca": mint_collection,
        "0xf99Fe455336aA8d668E433f1315C5808E8542119": mint_collection,
        "0x68C6cfcc3f9209DA2CAA662D412957982BB15093": mint_collection,
        "0xc8D4944FE05EeEE07fe54207FFE6991927cE7A84": mint_collection,
        "0x6c0c374E2316929A2892c7D4Affa479E771BbdDE": mint_collection,
        "0x8F4DE505F19B5f279643368309ADDA17F7aB33B8": mint_collection,
        "0x866FFf77e7A50b8F126f4837891f867A11B2EB92": mint_collection,
        "0x932264A3dc195D87F6ca3a7DFc9ab90f4ecBD99b": mint_collection,
        "0xdBb6a1923d704560CCD0095E22cE5681551AE2c7": mint_collection,
        "0xc4d965676Ff9a780Fc3888ad454631E36A153f0E": mint_collection,

        # Time limited collections
        "0xa90caea17aa8b3140b229113a3c154a8363f2035": mintfun_mint_nft,
    },
    'blast': {
        "0xd02DcDF7e5E48e77bfE3aFd02F3EBbBb3bA20831": mint_collection,
        "0xD7b569909375F73d43b2339beE31e91f584922E8": mint_collection,
        "0x8236f5d65f5A9F64eE89127B5D622D3105a987d1": mint_collection,
        "0x2158873343De4208F52f99D45aDc6D30BF3D2df6": mint_collection,
        "0x1BbDD6Bd0B5Ae1eE4a22d93e7252617c5e4B4358": mint_collection,
        "0x2238c29CDA6815cc0b4Eb3bf6A07DB926E4D7F48": mint_collection,
        "0xbE5EA23e0399983066114D2606907D81f839dE0a": mint_collection,
        "0x12902EeE880Fd296a1693C41e463f314eCF8Eafc": mint_collection,
        "0xD0ca933957a547f7ce04916201a3CE46F75d8170": mint_collection,
    },
    'scroll': {
        "0x0B0EBDafA49e676A60445EcBdD4DdF5ABc83a54A": mint_nfts2_me,
        "0x267412c94F78941F93a33E292fa7Bbf849751844": mint_nfts2_me,
        "0x805AD7aE07c3eE6792e6CE105E2cc91F015294D7": mint_nfts2_me,
        "0xAe7B1F56A251B1c608a5Ec536791955D2844C7c3": mint_nfts2_me,
        "0xD20388fFEB7A761E775ECEbF05197323ab3aB7F8": mint_nfts2_me,
        "0xBA396fF993947b06945CB5Ed9dEc31a8fc981F5A": mint_nfts2_me,
        "0x874ADe3582354D3A30Bb484607717e6e61b8619B": mint_nfts2_me,
        "0x89fe9DE65a17472C9817319363DFbFa82Fdcf65f": mint_collection,
        "0xAA6eD43a84A3F93C10B332e95D5d875a9D846e3E": mint_collection,
        "0x4bAb238AdadF13E474086C8dF71d7dF9Baba3016": mint_collection,
        "0x4A0d92D0A3aeD7D072A97ab84f23c247c53eaa5E": mint_collection,
        "0x3d36C22f119bB6eA7b094Ef86E3A04a789D7855c": mint_collection,
        "0x43c2Db6E82D210DAB6Da5953587C3Bd274143B4E": mint_collection,
        "0x27b1D1170e5b56D2235a797A83472F50242A225a": mint_collection,
        "0x399A8E2F30619d393d435Fe38a8Afd7945148E74": mint_collection,
    },
    'zksync': {
        "0x6BCa9A9CeFF34C36f8694cf1E75eA80b1fe8445d": mint_nfts2_me,
        "0xbF343eeBc76d8958fAB681D99b2F73633f16B257": mint_nfts2_me,
        "0xdFfE7E13A364C7e360BE8339e9869776a374c91C": mint_nfts2_me,
        "0xEd02866D7249dc392D23b4dc0daC0f7312B8b9d8": mint_nfts2_me,
        "0x1bfe365fC6e2DD2e1B8Cad3541e57663d83F8901": mint_nfts2_me,
        "0xfA12B745C41df5fb2B6Ca7c7A8634c663c694318": mint_nfts2_me,
        "0x9d9FCF62cc2D0827A3490dc7EF94062e2Fe25254": mint_collection,
        "0xb42Fe73501a31c02b4d35B8DFfEB4571c963Da4a": mint_collection,
        "0x708992de21A2288Bf12c5d58a3A637baD13Cc9ae": mint_collection,
        "0x530ffeA75890D1F10FA5375d968f7904161EADD9": mint_collection,
        "0x72a4D650E5720aB5e02E250A8a5B9f73e00e5406": mint_collection,
        "0x7Ab2Fad29E4a789d69ab56d37D03321DBbe70FA4": mint_collection,
        "0x0E0600AC3177eC3f3f20156D95B2f71Ebdb8F802": mint_collection,
        "0x757959E3397a9097F4069171E0824CA4eCAe182f": mint_collection,
        "0x61AcCf214e57149A751fF70a7B86d86c4A943383": mint_collection,
        "0x340d9c9F19a817bea65f6353CD23ab8F7ACc1A8D": mint_collection,
    },
    'zora': {
        "0x189473FeA86baa7a6655C518b0c164EBC4610e82": mint_collection,
        "0x9D51e93D66d201002504b0F15619208C630F71ed": mint_collection,
        "0x873c55300B678C27A7aF37D00c7c6FBf77174079": mint_collection,
        "0x3c6885A5A2504f6aa4adb6A62E3bb0b8BbF47030": mint_collection,
        "0xE2C419C6d697eaA384E9c07Ea25C13df9069F333": mint_collection,
        "0x1f5e168bC3066710CA6b28BbC5f8c990c60C7cea": mint_collection,
        "0x73773d0a44514881BD442E328dAC1861D2fd1Ce0": mint_collection,
        "0x588379E9711Ae3470f3895A61F1f3667d1D32661": mint_collection,
        "0xf5D9C2602c1241e47198C7957d5ba489d6308Eaa": mint_collection,
        "0xcef70c492216bc0DFa75Aa22675161Ae1C60FC36": mint_collection,

        # Time limited collections
        "0x84ce2c91ce73b6818c3ca171cfc23896dce617b1": mintfun_mint_nft,
        "0x23ed2158e33f38dcaab363176faf55426e04be4a": mintfun_mint_nft,
    },
    'polygon_zkevm': {
        "0x6585CAfeF8De44bF4FbfC69D9cC35e7a5012c07e": mint_collection,
        "0x30E51BC51Fdfc15bC3393d672B3a9211479beEaA": mint_collection,
        "0xd0BE07f5568fF2b81cE37a79F533B6EE363ec30a": mint_collection,
        "0x6Fb9610A91a4BbAD9bccFb39082837519009B463": mint_collection,
        "0x558730fDc09cE543fBde813a461eF494843689B1": mint_collection,
        "0x8A5DA59f40b79148216A27B9E86362EdCF03979f": mint_collection,
        "0xFe86D657A9F5B22dE0e54330811A180c3cBC2C0e": mint_collection,
        "0xf3d84FAD70fb0Bd9e039787Db0afdCb52ab81328": mint_collection,
        "0x6878dd61438Ae5AbB02E71D8BfAD9ff1B9B3025f": mint_collection,
        "0x393353Ecfd422bEC7603158C1DC41fB7f44D5469": mint_collection,
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
        "0x4C73C81C51b3e8370deA1D545d871720bEEC93E6": mint_collection,
        "0x54B8BD6da40Ab85f8aB92362E89133eb4CbA400c": mint_collection,
        "0x863886e015d7ad89E33236E3356812Ce258310E8": mint_collection,
        "0x4D1C741872004aeDd6dbb297DC26961E431a7b45": mint_collection,
        "0x5e7E4CD53e3d08B71D9Cb961593ECF12AD0E796F": mint_collection,
        "0x78914fD85c40852212783Ecf986c074F9D352511": mint_collection,
        "0x06651B4c92E5414a2784a538d272b06c272296Ed": mint_collection,
        "0x0f2f2c45Ae1bf10123021031fE873a1e077ecdBF": mint_collection,
        "0x4f441547142e262c0235c5ab5056F51114ee82F0": mint_collection,
        "0xeD918d4B1BDeD56EdDaeD2Df905F64AA3502252B": mint_collection,
    },
    'degen': {
        "0xdDbe579e2b4196f2f5291Eb4Bf2f46DaD9bBf496": mint_nfts2_me,
        "0x2cC1b711246254E3D6F8064166a92eA5b9Bb7c5a": mint_nfts2_me,
        "0x0C90eB70757A52119Cb98c64828aAD9e103382C2": mint_nfts2_me,
        "0xe7477BD5Be26158AD7349cdB06Fd52093a037502": mint_nfts2_me,
        "0x91541196E1d782ADB9e73727df1E719C01f25A2b": mint_nfts2_me,
        "0x4D27153Fc55e208F873C16A72d1E667011cF6aD6": mint_nfts2_me,
        "0x4456DA074f4318a24d80Af7a3713242aa59C63cE": mint_nfts2_me,
        "0x8EA0E65CfaBB42bac8449Abf9fa8031d32FE2AAA": mint_nfts2_me,
        "0xe6727dd89BFF7C40B63e8c8D634Ef3cC77eD55D4": mint_nfts2_me,
        "0xc29a6eE829Ba91c488909e999F6a614E6fdaa884": mint_nfts2_me,
        "0x7d00e4C4Ec7eb4E3f9ed07A0465CeC0AFaBF08F8": mint_nfts2_me,
    }
}

CONTRACT_PAYMENT = {
    "ethereum": {},
    'scroll': {

    },
    'zksync': {

    },
    'nova': {
        "0x89CdDB9F8e751B90b21604aE759c4C798a07aa12": 0.0002,
        "0x6DB8F6f6ca292e50e0527F027f95a22dD2bBd19e": 0.0002,
        "0x979aF99614901A7d404C24024B759b16Cd55F928": 0.0002,
        "0x9e283Aa8D2BBb27bd473707A45B6f8136ED5E4D0": 0.0002,
        "0xfaa4b80471095499b4D54E86198DB47B66f70525": 0.0002,
        "0xF15503fF3c28990eBdCa14e1aA214a36aa6F7971": 0.0002,
        "0x7D54A74DA56A8C36038BB75F6C77098ffD072B3a": 0.0002,
        "0x02acA7E9Bde7e0e421aEEF9D83e50DB217e16aD9": 0.0002,
        "0x95170e7E54b77c1B1eB548614f2B3B976Abbb55a": 0.0002,
        "0xc32A4e85876CC3C4D81fd9Efd22615BeEf0878B0": 0.0002,
        "0x9419F0d1D5FAb1EC307Bb6e54D31CDE1B398F14f": 0.0002,
        "0x71fbf56f33F628f27092f767a5189EaBCa603720": 0.0002,
        "0x686f3F581BC9932c9EcEC77eaD1C2b4d47839618": 0.0002,
        "0x5a86B8154E39c514cf08D51c1B6b992C5eebfcA4": 0.0002,
        "0x573e2C45CD6F0Ef35758fe3c3F6204A7b4dA68bC": 0.0002,
        "0x90952C9ca93b3fD47BcCBEbbDcF08f4d848AD895": 0.0002,
    },
    'base': {
        "0xa90caea17aa8b3140b229113a3c154a8363f2035": 0,
    },
    'polygon_zkevm': {},
    'blast': {},
    'mode': {

    },
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
