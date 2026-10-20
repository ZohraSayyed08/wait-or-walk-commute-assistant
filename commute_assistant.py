"""
Commute Decision Assistant — SDG 11: Sustainable Cities
Helps a commuter decide whether to keep waiting for a bus or switch to walking.
"""


def commute_decision(is_raining: bool, is_rush_hour: bool, waited_10_plus_min: bool) -> dict:
    """
    Evaluate commute risk and recommend an action.

    Parameters:
        is_raining        (bool): True if it is currently raining.
        is_rush_hour      (bool): True if it is a weekday rush hour (8–10am or 6–8pm).
        waited_10_plus_min(bool): True if the commuter has already waited 10+ minutes.

    Returns:
        dict with keys:
            "score"          (int)  : Total risk score (0–4).
            "risk_level"     (str)  : "Low", "Medium", or "High".
            "recommendation" (str)  : Human-readable advice.
    """

    # ── Step 1: Calculate the risk score ─────────────────────────────────────
    score = 0

    # Rain makes walking unpleasant — worth 2 points because it strongly
    # discourages switching to walking.
    if is_raining:
        score += 2

    # Rush hour means buses are busier and delays are more likely — 1 point.
    if is_rush_hour:
        score += 1

    # Already waiting 10+ minutes suggests the bus may not be coming soon — 1 point.
    if waited_10_plus_min:
        score += 1

    # ── Step 2: Map the score to a risk level and recommendation ─────────────
    if score <= 1:
        risk_level = "Low"
        recommendation = "Wait — you're probably fine. The bus should arrive soon."
    elif score == 2:
        risk_level = "Medium"
        recommendation = "Wait a bit longer, but stay alert. Consider your options."
    else:  # score is 3 or 4
        risk_level = "High"
        recommendation = "Consider walking or switching routes now."

    # ── Step 3: Return all results together ──────────────────────────────────
    return {
        "score": score,
        "risk_level": risk_level,
        "recommendation": recommendation,
    }


# ── Quick demo ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    test_cases = [
        # (is_raining, is_rush_hour, waited_10_plus_min, label)
        (False, False, False, "Dry day, off-peak, short wait"),
        (False, True,  True,  "Dry day, rush hour, long wait"),
        (True,  False, False, "Raining, off-peak, short wait"),
        (True,  True,  True,  "Raining, rush hour, long wait"),
    ]

    print(f"{'Scenario':<40} {'Score':>5}  {'Risk':<8}  Recommendation")
    print("-" * 90)

    for is_raining, is_rush_hour, waited, label in test_cases:
        result = commute_decision(is_raining, is_rush_hour, waited)
        print(
            f"{label:<40} "
            f"{result['score']:>5}  "
            f"{result['risk_level']:<8}  "
            f"{result['recommendation']}"
        )
