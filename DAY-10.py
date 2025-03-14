# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gyCRAEfNYgCqK8VHaub-HJrgfFieSxG6
"""

import re

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    emails = re.findall(email_pattern, text)

    return emails

input_text = 'Contact us at support@example.com and sales@example.org.'
extracted_emails = extract_emails(input_text)

print("Original Text:", input_text)
print("Extracted Emails:", extracted_emails)