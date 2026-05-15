import pandas as pd
def persian_to_english_digits(text):
    if pd.isna(text):
        return text
    persian_digits = "۰۱۲۳۴۵۶۷۸۹"
    english_digits = "0123456789"
    trans_table = str.maketrans("".join(persian_digits), "".join(english_digits))
    return str(text).translate(trans_table)