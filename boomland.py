import json
import asyncio

from web3 import Web3
from loguru import logger
from web3.middleware import geth_poa_middleware


logger.add("debug.log", format="{time:YYYY-MM-DD | HH:mm:ss.SSS} | {level} \t| {line} - {message}")


async def create_txn(q: asyncio.Queue):
    wallet_address, private_key = (await q.get()).split(":")
    try:
        txn = contract.functions.requestTokens().buildTransaction({
            'from': wallet_address,
            'nonce': web3.eth.getTransactionCount(wallet_address),
            'gasPrice': web3.eth.gas_price
        })

        signed_txn = web3.eth.account.signTransaction(
            txn, private_key=private_key)
        tx_hash = web3.toHex(web3.eth.sendRawTransaction(signed_txn.rawTransaction))
        logger.info(f'{wallet_address} | {tx_hash}')

        balance = web3.fromWei(web3.eth.getBalance(wallet_address), 'ether')

    except Exception as error:
        logger.error(f'{wallet_address} | {error}')
        with open("error.txt", "a") as file:
            file.writelines(f"{wallet_address}:{private_key}:{balance}\n")
    else:
        with open("successfully.txt", "a") as file:
            file.writelines(f"{wallet_address}:{private_key}:{balance}\n")
    finally:
        input()


@logger.catch
async def main():
    with open("wallets.txt", "r") as file:
        wallets = file.readlines()

    q = asyncio.Queue()
    for wallet in wallets:
        q.put_nowait(wallet.strip())

    tasks = [asyncio.create_task(create_txn(q)) for _ in range(len(wallets))]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    print("Bot Boomland @flamingoat\n")

    web3 = Web3(Web3.HTTPProvider("https://polygon-rpc.com"))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    logger.info(f"Is connected: {web3.isConnected()}")

    with open("ABI.json", "r") as file:
        ABI = json.load(file)

    contract_address = web3.toChecksumAddress(
        "0x3a1F862D8323138F14494f9Fb50c537906b12B81")

    contract = web3.eth.contract(contract_address, abi=ABI)
    
    asyncio.run(main())