# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
    
        addresses = re.split(r'\s*,\s*', self.email_addresses)
        return addresses

