from app import app
import os
import json
from web3 import Web3
from flask import Response, request, jsonify
from github import Github

class Niftmint:
    def __init__(self, abi_file, sc_address):
        infura_url = 'https://rinkeby.infura.io/v3/49bce5fc59bb4cf0b0f28bd9609e0308'
        self.w3 = Web3(Web3.HTTPProvider(infura_url))
        # verify connection
        assert self.w3.isConnected(), "Web3 connection failed"

        self.owner = '0x860A0a008b18dFc0b051C1Fb7638e6a7CaFbF8eC'
        self.name = None
        self.symbol = None

        # read json file containing smart contract ABI
        with open(abi_file, 'r') as f:
            niftmint_abi = json.load(f)
        # connect to smart contract
        self.contract = self.w3.eth.contract(
            address=sc_address, 
            abi=niftmint_abi
        )

        github = Github('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')
        self.repo = github.get_repo("Niftmint/api")
        print('initialized')

    def token_name(self):
        if self.name is None:
            self.name = self.contract.functions.name().call()
        return self.name

    def token_symbol(self):
        if self.symbol is None:
            self.symbol = self.contract.functions.symbol().call()
        return self.symbol

    def current_id(self):
        id = self.contract.functions.getCurrentId().call()
        return id

    def metadata(self, id):
        uri = self.contract.functions.tokenURI(int(id)).call()
        filename = 'metadata/' + id + '.json'
        metadata = self.repo.get_contents(filename)
        return metadata.decoded_content.decode()

@app.route('/mint', methods=['POST'])
def mint():
    account = request.form['address']
    print('account: ', account)
    #uri = request.form['uri']

    # call smart contract to mint NFT
    id = 23
    # return NFT id
    return jsonify({'NFT id': id}), 200

@app.route('/token')
def token():
    id = request.args.get('id')
    if id is None:
        return jsonify({'exception': 'token ID required'}), 400

    try:
        content = niftmint.metadata(id)
    except:
        return jsonify({'exception': 'invalid token ID'}), 400

    return content, 200

@app.route('/index')
@app.route('/')
def index():
    id = niftmint.current_id()
    return jsonify({'current ID': id}), 200


@app.before_request
def log_before_request():
    print('\n-------------------------------------------------------------------')

@app.after_request
def log_after_request(response):
    print('-------------------------------------------------------------------')
    return response


# JSON file was generated by running:
# > brownie console --network rinkeby
# From the brownie console, type the following commands with the address of the smart contract:
# > c = Contract("0x7c33F0841418df52c245B76D5596659F7f7A9638")
# > c.abi
# > exit()
# Copy the output of 'c.abi' into a file, and do a global replace in VS Code:
# :%s/'/"/g
# :%s/False/false/g
# :%s/True/true/g
# save the file
abi_file = os.path.join(app.root_path, '../abi/niftmint.json')
print('root path: ', app.root_path)
niftmint = Niftmint(abi_file, '0x7c33F0841418df52c245B76D5596659F7f7A9638')
