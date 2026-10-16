"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI     (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def check_record(value,limit):
  difference =limit - value
  percent = (value/limit) * 100

  if value > limit:
    status = "OVER LIMIT"
  else:
    status = "OK"

  return difference, percent, status

def print_report(label, value, limit, differnce, percent, status):
  print("=" * 45)
  print("label:", label)
  print("=" * 45)
  print("value:", value)
  print("limit:", limit)
  print("difference:", differnce)
  print(f"percent:{percent:2.2f} % ")
  print("status:", status)
  print()

def load_records(path):
    records = []

    with open(path, "r") as file:
      for line in file:
        label, value, limit = line.strip().split(",")
        record = {
          "label": label,
          "value": float(value),
          "limit": float(limit)
        }
        records.append(record)

    return records

try:
  records = load_records("records.txt")
except FileNotFoundError:
  print("File not found: records.txt")
  records = []

over_count = 0


with open("results.txt", "w") as file:
    for record in records:
        difference, percent, status = check_record(
            record["value"], record["limit"]
        )
        print_report(
           record["label"],
           record["value"],
           record["limit"],
           difference,
           percent,
           status
        )

        file.write(record["label"] + "," + status + "\n")
        if status == "OVER LIMIT":
           over_count += 1

print(f"Total over limit:", over_count)