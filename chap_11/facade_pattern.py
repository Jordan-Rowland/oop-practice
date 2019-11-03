"""
A facade can be thought of as an API or wrapper.

The facade pattern is designed to provide a simple interface to a complex system of
components. For comples tasks, we may need to interact with these objects directly, but
there is often a typical usage for the system for which these complicated interactions
aren't necessary. The facade pattern allows us to define a new object that encapsulates
this typical usage of the system. Any time we want access to common functionality, we can
use this single object's simplified interace. If another part of the project needs access
to more complicated functionality, it is still able to interact with the system directly.

A facade is, in many ways, like an adapter. The primary difference is that a facade tries
to abstract a simpler interface out of a complex one, while an adpapter only tries to map
one existing interface to another.

Below is an example facade for SMTP and IMAP functionality for sending emails and
receiving a list of emails from an inbox:
"""

import smtplib
import imaplib

class EmailFacade:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, message):
        if not "@" in self.username:
            from_email = f"{self.username}@{self.host}"
        else:
            from_email = self.username
        message = (
            f"From: {from_email}\r\n" f"To: {to_email}\r\n" f"Subject: {subject}\r\n\r\n"
            f"{message}"
        )

        smtp = smtplib.SMTP_SSL(self.host, 465)
        smtp.login(self.username, self.password)
        smtp.sendmail(from_email, [to_email], message)

    def get_inbox(self):
        mailbox = imaplib.IMAP4_SSL(self.host)
        mailbox.login(
            # bytes(self.username, "utf8"), bytes(self.password, "utf8")
            self.username, self.password
        )
        mailbox.select()
        x, data = mailbox.search(None, "ALL")
        messages = []
        for num in data[0].split():
            x, message = mailbox.fetch(num, "(RFC822)")
            messages.append(message[0][1])
        return messages


"""
Althought it's rarely mentioned by name in the Python community, the facade pattern is an
integral part of the Python ecosystem. Because Python emphasizes language readability,
both the language and it's libraries tend to provide easy-to-comprehend interfaces to
complicated tasks. For example, fore loops, listcomprehensions, and generators are all
facades into a more complicated iterator protocol. The defaultdict implementation is a
facade that abstracts away annoying corner cases when a key doesn't exist in a dictionary.
the third-party Requests library is a powerful facade over less readable libraries for
HTTP requests, which are themselves a facade overmanagin the text-based HTTP protocol
yourself.
"""
