from backend.core.analytics import analytics

@router.get("/metrics")
def metrics():

    revenue = analytics["total_revenue"]
    requests = analytics["requests"]
    users = len(analytics["users"])

    mrr = revenue * 30  # simplified projection
    arpu = revenue / requests if requests > 0 else 0

    return {
        "MRR": round(mrr, 4),
        "ARR": round(mrr * 12, 4),
        "total_revenue": revenue,
        "requests": requests,
        "active_users": users,
        "ARPU": round(arpu, 6),
        "decisions": analytics["decisions"],
        "events": analytics["revenue_events"][-20:]
    }
