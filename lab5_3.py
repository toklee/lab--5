import re

PATH = 'task3.txt'
PATH_OUT = 'modified_task3.txt'

def find_id(text):
    ids = re.findall(r'\b(?!\d{4}-\d{2}-\d{2}\b)([1-9]\d{0,3}|10000)\b', text)
    return ids

def find_surname(text):
    surnames = re.findall(r'\b[A-Z][a-zA-Z\']+\b', text)
    return surnames

def find_emails(text):
    emails = re.findall(r'\S+@\S+', text)
    return emails

def find_date(text):
    dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)
    return dates

def find_site(text):
    sites = re.findall(r'\bhttps?://[^\s]+', text)
    return sites

with open(PATH, encoding='utf-8') as text, open(PATH_OUT, 'w', encoding='utf-8') as out:
    for line in text:
        ids = find_id(line)
        surnames = find_surname(line)
        emails = find_emails(line)
        dates = find_date(line)
        sites = find_site(line)

        max_length = max(len(ids), len(surnames), len(emails), len(dates), len(sites))

        for i in range(max_length):
            id_value = ids[i] if i < len(ids) else None
            surname_value = surnames[i] if i < len(surnames) else None
            email_value = emails[i] if i < len(emails) else None
            date_value = dates[i] if i < len(dates) else None
            site_value = sites[i] if i < len(sites) else None


            line_output = f"{id_value:<10} {surname_value:<20} {email_value:<30} {date_value:<15} {site_value}"
            out.write(line_output + '\n')
            print(line_output)

        if max_length > 0:
            print()
