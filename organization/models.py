from django.db import models


class OrganizationItem:
    def __init__(self, name, url_name, count):
        self.name = name
        self.url_name = url_name
        self.count = count
