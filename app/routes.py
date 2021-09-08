from app import app
import os
import json
import urllib
from web3 import Web3
import flask

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
        print('URI: ', uri)
        content = urllib.request.urlopen(uri)
        return content.read()

@app.route('/token')
def token():
    id = flask.request.args.get('id')
    if id is None:
        return flask.jsonify({'exception': 'token ID required'}), 400
    img = flask.request.args.get('image')

    try:
        content = niftmint.metadata(id)
    except:
        return flask.jsonify({'exception': 'invalid token ID'}), 400

    c = json.loads(content)

    if img is not None:
        content = urllib.request.urlopen(c['image'])
        resp = flask.make_response(content.read())
        resp.content_type = 'image/png'
        return resp

    #return content, 200
    print(c)
    return flask.render_template('nft.html', nft=c)

@app.route('/index')
@app.route('/')
def index():
    id = niftmint.current_id()
    return flask.jsonify({'current ID': id}), 200


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
contract = '0x11fb47B8F31c072Ee2E998c75499A0185dB23A5d'
print('smart contract: ', contract)
abi = os.path.join(app.root_path, '../abi/niftmint.json')
print('ABI: ', abi)
niftmint = Niftmint(abi, contract)
