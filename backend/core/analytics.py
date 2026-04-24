from datetime import datetime

analytics = {
    "revenue_events": [],
    "requests": 0,
    "total_revenue": 0,
    "users": set(),
    "decisions": {"ALLOW": 0, "BLOCK": 0, "CHALLENGE": 0}
}


def log_event(payment, decision, user_id="anon"):

    amount = payment.get("amount", 0)

    analytics["requests"] += 1
    analytics["total_revenue"] += amount
    analytics["users"].add(user_id)

    if decision:
        for k in analytics["decisions"]:
            if k in str(decision):
                analytics["decisions"][k] += 1

    analytics["revenue_events"].append({
        "time": str(datetime.utcnow()),
        "amount": amount,
        "user": user_id,
        "decision": decision
    })

    return analytics
