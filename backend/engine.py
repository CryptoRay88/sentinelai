import random

def analyze(event: dict):

    score = 0

    if event.get("login_attempts", 0) > 5:
        score += 40

    if event.get("unusual_ip"):
        score += 35

    if event.get("geo_mismatch"):
        score += 25

    score += random.randint(0, 10)

    if score > 70:
        decision = "BLOCK"
    elif score > 40:
        decision = "CHALLENGE"
    else:
        decision = "ALLOW"

    return {
        "risk_score": score,
        "decision": decision
    }