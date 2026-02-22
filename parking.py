def calculate_fee(hours):
    if hours < 0:
        return "Invalid input"

    if hours <= 2:
        return 0

    if hours <= 5:
        return (hours - 2) * 20

    return (3 * 20) + (hours - 5) * 50
