from web3 import Web3
import hashlib
import json
import os

# Configuración para Ganache local
GANACHE_URL = "http://127.0.0.1:7545"
CONTRACT_ADDRESS = "0xC1ef6C284435A50cBBAB42dBed7710802B75f70C"
PRIVATE_KEY = "0x0ad32406e62283b8bd2f4123396e0e86d9592e0ce0816480ce6e08973a3362f3"
ACCOUNT_ADDRESS = "0xcBE491B299D8B466DAEaF1E2620fc643DD053410"

w3 = Web3(Web3.HTTPProvider(GANACHE_URL))

# ABI del contrato (copiarlo desde Remix)
with open(os.path.join(os.path.dirname(__file__), "abi.json")) as f:
    abi = json.load(f)

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

def obtener_hash(producto):
    datos = f"{producto.nombre}|{producto.descripcion}|{producto.tipo}|{producto.creado_en}"
    return hashlib.sha256(datos.encode('utf-8')).hexdigest()

def registrar_en_blockchain(producto):
    hash_hex = obtener_hash(producto)
    hash_bytes = w3.toBytes(hexstr=hash_hex)

    nonce = w3.eth.get_transaction_count(ACCOUNT_ADDRESS)
    tx = contract.functions.registrarProducto(hash_bytes).build_transaction({
        'from': ACCOUNT_ADDRESS,
        'nonce': nonce,
        'gas': 300000,
        'gasPrice': w3.toWei('1', 'gwei'),
    })

    signed_tx = w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    return w3.to_hex(tx_hash), hash_hex
