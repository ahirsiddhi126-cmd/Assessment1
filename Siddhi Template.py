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

count = 0

while True:
  label = input("Enter label: ")

  if label == "quit":
    break

  used = float(input("Enter used:"))
  total = float(input("Enter total:"))

  free = total - used
  percent = (used/total) * 100

  if percent >= 100:
    status = "OVER LIMIT"
    count += 1
  elif percent >= 90:
    status = "WARNING"
  else:
    status = "OK"

  print("=" * 30)
  print(f"  RECORD CHECK  -  {label}")
  print("=" * 30)
  print(f"Used : {used:6.2f}")
  print(f"Total : {total:6.2f}")
  print(f"Free : {free:6.2f}")
  print(f"Percent : {percent:6.2f} %")
  print(f"Status : {status}")
  print("=" * 30)

print("Over limit :", count)