from collections import defaultdict
from contextlib import suppress
import smtplib
from time import sleep
from email.mime.text import MIMEText


def send_email(subject, message, from_addr, *to_addrs, host="localhost", port=1025, headers=None):
    headers = headers if headers else {}
    email = MIMEText(message)
    email["Subject"] = subject
    email["From"] = from_addr
    for header, value in headers.items():
        email[header] = value
    sender = smtplib.SMTP(host, port)
    for i, addr in enumerate(to_addrs):
        if not i % 4:
            sleep(3)
        del email["To"]
        email["To"] = addr
        sender.sendmail(from_addr, addr, email.as_string())
    sender.quit()


class MailingList:
    """Manage groups of email addresses for sending emails"""

    def __init__(self, data_file):
        self.data_file = data_file
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def emails_in_groups(self, *groups):
        groups = set(groups)
        emails = set()
        for e, g in self.email_map.items():
            if g & groups:
                emails.add(e)
        return emails

    def send_mailing(self, subject, message, from_addr, *groups, headers=None):
        emails = self.emails_in_groups(*groups)
        send_email(subject, message, from_addr, *emails, headers=headers)

    def save(self):
        with open(self.data_file, "w") as file:
            for email, groups in self.email_map.items():
                file.write(f"{email} {','.join(groups)}\n")

    def load(self):
        self.email_map = defaultdict(set)
        with suppress(IOError):
            with open(self.data_file) as file:
                for line in file:
                    email, groups = line.strip().split(" ")
                    groups = set(groups.split(","))
                    self.email_map[email] = groups

    def __enter__(self):
        self.load()
        return self

    def __exit__(self, type, value, tb):
        self.save()


m = MailingList("addresses.db")
# m.add_to_group('friend1@gmail.com', 'friends')
# m.add_to_group('friend2@gmail.com', 'friends')
# m.add_to_group('friend3@gmail.com', 'friends')
# m.add_to_group('friend3@gmail.com', 'fam')
# m.add_to_group('fam1@gmail.com', 'fam')
# m.save()

m.email_map
m.load()
m.email_map

with MailingList("addresses.db") as ml:
    ml.add_to_group("Friend2example@gmail.com", "friends")
    ml.send_mailing("What's up", "hello bitches", "me@example.com", "friends")
