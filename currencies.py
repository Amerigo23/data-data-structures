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

    # Constructing the conversion key
    conversion_key = f"{from_currency}{target_currency}"

    # Check if the conversion rate exists in the RATES dictionary
    if conversion_key not in RATES:
        # If not, return None
        return None

    # Perform the currency conversion and round the result to the nearest whole number
    converted_amount = round(value * RATES[conversion_key])

    return converted_amount
