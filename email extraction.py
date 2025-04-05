import re

# I. Extract all email addresses from a given text
def extract_emails(text):
    """Extract all email addresses from a text string."""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)

# II. Validate a date in "YYYY-MM-DD" format
def validate_date(date_str):
    """Validate if a string is in YYYY-MM-DD format."""
    date_pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
    return bool(re.fullmatch(date_pattern, date_str))

# III. Replace all occurrences of a word with another word
def replace_words(text, old_word, new_word):
    """Replace all occurrences of old_word with new_word in text."""
    return re.sub(r'\b' + re.escape(old_word) + r'\b', new_word, text)

# IV. Split string by all non-alphanumeric characters
def split_by_non_alphanumeric(text):
    """Split a string by any non-alphanumeric characters."""
    return re.split(r'[^a-zA-Z0-9]+', text)

# Demonstration
if __name__ == "__main__":
    # Test email extraction
    sample_text = "Contact us at sylvesternduru@gmail.com or pg246552h@cuz.ac.zw for help."
    print("Extracted emails:", extract_emails(sample_text))

    # Test date validation
    test_dates = ["2023-12-25", "1999-02-30", "2022-13-01", "2020-06-15"]
    for date in test_dates:
        print(f"'{date}' is valid:", validate_date(date))

    # Test word replacement
    sentence = "The cat sat on the mat with another cat."
    print("Replaced text:", replace_words(sentence, "cat", "dog"))

    # Test splitting by non-alphanumeric
    test_string = "Hello, world! This is a test-123."
    print("Split result:", split_by_non_alphanumeric(test_string))