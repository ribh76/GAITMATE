RISK_LEVELS = {
    1: {
        "label": "Low Risk",
        "color": "#2a8a5f",
        "advice": "Within healthy range.",
        "score": 18,
    },
    2: {
        "label": "Low-Medium Risk",
        "color": "#8fbf4f",
        "advice": "Slightly elevated. Continue normal movement and monitor.",
        "score": 34,
    },
    3: {
        "label": "Moderate Risk",
        "color": "#d9a32a",
        "advice": "Ease off high-impact activity and keep monitoring.",
        "score": 54,
    },
    4: {
        "label": "Elevated Risk",
        "color": "#e08a4a",
        "advice": "Reduce load and avoid aggressive ankle movement.",
        "score": 74,
    },
    5: {
        "label": "High Risk",
        "color": "#d65a4a",
        "advice": "Avoid loading the ankle and consider contacting your physician.",
        "score": 92,
    },
}


def calculate_risk(max_strain, gradient, variability):
    max_strain = float(max_strain or 0)
    gradient = float(gradient or 0)
    variability = float(variability or 0)

    if max_strain >= 8 or gradient >= 4 or variability >= 1.5:
        level = 5
    elif max_strain >= 6 or gradient >= 3 or variability >= 1.0:
        level = 4
    elif max_strain >= 4 or gradient >= 2 or variability >= 0.5:
        level = 3
    elif max_strain >= 2 or gradient >= 1 or variability >= 0.25:
        level = 2
    else:
        level = 1

    return {"level": level, **RISK_LEVELS[level]}


def calculate_overall(ligaments):
    if not ligaments:
        return {
            "level": 1,
            "score": 0,
            "label": "Healthy",
            "color": RISK_LEVELS[1]["color"],
        }

    levels = [item["risk"]["level"] for item in ligaments.values()]
    scores = [item["risk"]["score"] for item in ligaments.values()]
    level = max(levels)
    score = round(max(scores) * 0.6 + (sum(scores) / len(scores)) * 0.4)

    if level <= 2:
        label = "Healthy"
    elif level == 3:
        label = "Monitor"
    elif level == 4:
        label = "Elevated"
    else:
        label = "High"

    return {
        "level": level,
        "score": score,
        "label": label,
        "color": RISK_LEVELS[level]["color"],
    }
