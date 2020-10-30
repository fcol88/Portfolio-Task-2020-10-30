from datetime import datetime


# simple class at the moment, but could be
# expanded to include other fields like "user"
class Audit:

    def __init__(self):
        self.timestamp = datetime.now()

    def __str__(self):
        return "Timestamp: {0:%d/%m/%y %H:%M}".format(self.timestamp)

    def __repr__(self):
        return "Audit()"
