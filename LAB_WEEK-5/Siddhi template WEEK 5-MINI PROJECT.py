"""
RECORD CHECK  -  my version
===========================

Name  : Ahir Siddhi
Lane  : AI      
Date  : 23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

class Record:
    """Stores information about one dataset record."""

    def __init__(self, label, value, limit):
        """Initialises a record with its label, value and limit."""
        self.label = label
        self.value = float(value)
        self.limit = float(limit)

    def percent(self):
        """Calculates the percentage of rows loaded."""
        return (self.value / self.limit) * 100

    def status(self):
        """Returns the status based on the percentage loaded."""
        if self.percent() >= 100:
            return "OVER LIMIT"
        elif self.percent() >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Loads records from a file and returns a list of Record objects."""
    records = []

    with open(path, "r") as file:
        for line in file:
            label, value, limit = line.strip().split(",")
            record = Record(label, value, limit)
            records.append(record)

    return records


records = load_records("survey_records.txt")

over_count = 0

for record in records:
    status = record.status()

    print("=" * 40)
    print("Dataset:", record.label)
    print("=" * 40)
    print(f"Rows loaded     : {record.value:10.2f}")
    print(f"Rows expected   : {record.limit:10.2f}")
    print(f"Rows remaining  : {record.limit - record.value:10.2f}")
    print(f"Percent loaded  : {record.percent():10.2f} %")
    print(f"Status          : {status:>10}")
    print("=" * 40)
    print()

    if status == "OVER LIMIT":
        over_count += 1

print("Total OVER LIMIT:", over_count)






