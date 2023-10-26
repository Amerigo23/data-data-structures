# pylint: disable=missing-docstring

# TODO: add some currency rates
RATES = {
    "USDEUR": 0.85,
    "GBPEUR": 1.13,
    "CHFEUR": 0.86,
    "EURGBP": 0.885,
}

def convert(amount, target_currency):
    """
    returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    target_currency is a string
    """
    value, from_currency = amount

    conversion_key = f"{from_currency}{target_currency}"

    if conversion_key not in RATES:
        # If not, return None
        return None

    converted_amount = round(value * RATES[conversion_key])

    return converted_amount
