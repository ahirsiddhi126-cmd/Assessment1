"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI       (delete two)
Date  :
"""

def status_of(value, limit):
  if value > limit:
     status = "OVER LIMIT"
  else:
    status = "OK"

  return status

def check(value, limit):
  difference = limit - value
  percentage = (value / limit) * 100
  return difference, percentage

def print_report(label, value, limit, difference, percentage, status):
    print("=" * 40)
    print(f"   RECORD CHECK - {label}")
    print("=" * 40)
    print(f"Rows loaded        : {value:>10.2f}")
    print(f"Rows expected      : {limit:>10.2f}")
    print(f"Rows remaining     : {difference:>10.2f}")
    print(f"Percent loaded     : {percentage:10.2f} %")
    print(f"Status             : {status:>10}" )
    print("=" * 40)


count = 0

while True:
  label = input("Enter the record label (or quit): ")
  if label == "quit":
    break

  value = float(input("Enter the number of rows loaded: "))
  limit = float(input("Enter the number of rows expected: "))

  difference, percentage = check(value, limit)
  status = status_of(value, limit)
  
  print_report(label, value, limit, difference, percentage, status)

  if status == "OVER LIMIT":
    count += 1

print()
print("Number of OVER LIMIT records:", count)

#when the value and limit are both 0, the error shown is that there is Zero division error.
