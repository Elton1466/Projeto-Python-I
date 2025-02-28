def validate_amount(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False