def verify_wallet(wallet_id: str):
    return {
        "wallet": wallet_id,
        "status": "verified",
        "balance_usdc": 50
    }

def charge(wallet_id: str, amount: float):
    return {
        "wallet": wallet_id,
        "charged": amount,
        "currency": "USDC",
        "status": "success"
    }
