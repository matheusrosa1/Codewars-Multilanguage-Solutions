def validate_pin(pin):
    if len(pin) not in (4, 6):
        return False
    for char in pin:
        if not char.isdigit():
            return False
    return True