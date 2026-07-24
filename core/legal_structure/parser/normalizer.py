ARABIC_INDIC_DIGITS = str.maketrans(
    "٠١٢٣٤٥٦٧٨٩",
    "0123456789"
)


def normalize_number(value: str) -> str:

    return value.translate(
        ARABIC_INDIC_DIGITS
    )
