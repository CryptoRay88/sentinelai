from backend.payments.circle import charge

def verify_payment(request):
    wallet = request.get("wallet_id")
    amount = request.get("amount", 0.01)

    receipt = charge(wallet, amount)

    return {
        "payment_status": "verified",
        "receipt": receipt
    }
