# Press the green button in the gutter to run the script.
import pandas as pd
import chardet as chardet
import urllib.request
import urllib.error



choice = 0

def reset_choice():
    choice = 0

#This is ENTIRELY LIMINAL and ENTIRELY A PLACEHOLDER! Once we get the JSON file up, DELETE THIS!
#Don't forget this
KEYWORDS = ["mean", "invited", "obviously"]


def manage_keywords(keywords):
  while True:
    print("--- Keyword Manager ---")
    print("Current keywords:", keywords)
    print("a) Add")
    print("r) Remove")
    print("b) Back")
    choice = input("Choice: ")
    match choice:
      case 'a':
        new_kw = input("Enter new keyword: ")
        keywords.append(new_kw)
      case 'r':
        bad_kw = input("Choose keyword to remove")
        keywords.remove(bad_kw)
      case 'b':
        break

#A simple system for counting individual words.
#Should be easy to integrate with word weights
#Unsure exactly how to integrate with the 'contextual rules'
#mostly cause I'm still not entirely sure what that entails
def count_matches(line, keywords):
  line_lower = line.lower()
  count = 0
  for kw in keywords:
    if kw in line_lower:
      count += 1
  return count

#just plops out flagged messages
def scan_logs(logs, keywords):
  flagged = 0
  for log in logs:
    if (count_matches(log, keywords)) > 0:
      print(log + " " + str(count_matches(log, keywords)))
      flagged += 1
  print("Total flagged messages:", flagged)

#Should(read: should) censor all the messages.
#As I recall, this either was or was not working.
#Has no utility right now, moreso just here in case we need to build on it
#since the censoring is something we need to do
def censor_logs(logs, keywords):
  for log in logs:
      for s in keywords:
        log = log.replace(s, "[REDACTED]")
      print(log)

#prints the logs. Includes the date, publisher, and other parts of the messages
def view_logs(list):
    f = 1
    for i in list:
      print("Message number " + str(f) + ": " + i)
      f += 1
    return []

def load_logs(filename):
  try:
    with open(filename, "r", encoding="utf-8") as file:
      lines = [line.strip() for line in file]
    return lines

  except FileNotFoundError:
    print(f"File '{filename}' not found.")
    return []
if __name__ == '__main__':

    print("Welcome to Chat Sentinel.")

    while True:
        print("Please select an option.")
        print("1 - Load Chat Log")
        print("2 - Configure Keywords")
        print("3 - Generate Report")
        print("4 - Fetch Data From URL")
        print("5 - Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                file_epic: str = input("Enter name of file you'd like to use: ")
                logs_list = load_logs(file_epic)
                #you can remove the call to print the entire massive file
                #I just had it to ensure it was properly reading everything
                print(logs_list)
            case 2:
                manage_keywords(KEYWORDS)
            case 3:
                scan_logs(logs_list, KEYWORDS)
            case 4:
                # This DOES NOT WORK YET, this is how we're gonna read from URLs.
                # If someone smarter than me knows a way to do it faster then go for it.
                url = str(input("What's the URL you'd like to input?"))
                myfile = pd.read_csv(url)
                logs_list = view_logs(myfile)
            case 5:
                print("5")
                print("You have exited the program.")
                print("To use the program again, press 'Run'.")
                break
