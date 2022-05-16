#import os
#os.system('pip install ScraGet')
# Built with ScraGet.
# Creds: https://github.com/Quantum-Codes/ScraGet
#os.system('clear')
#print("'info' for help.")

# NOTICE: "s!" stands for Search, it is the
# basic prefix for browser commands.

#while True:
  #option = input(">>> ")
  #if option == "s!profile":
  #  profile = input("username>>> ")
    # Add code to retrieve data

# NEW AND IMPROVED SCRIPT
import time
import os

os.system("clear")

while True:
  historyShown = "N"
  searchingFor = input("S for Studio or P for project or U for user: ")
  if searchingFor == "U":
    searchUser = input("What user would you like to search? ")
    print()
    print("User data:")
    from ScraGet import ScraGet
    user = ScraGet.get_user()
    user.updateScratch(searchUser)
    print("Name: " + user.username)
    print("ID: " + str(user.id))
    print("Joined: " + str(user.join_date))
    print("Country: " + str(user.country))
    print()
  elif searchingFor == "S":
    searchStudio = input("What's the studio ID? ")
    print()
    print("Studio Data: ")
    from ScraGet import ScraGet
    studios = ScraGet.get_studio()
    studios.updateScratch(searchStudio)
    print("Title: " + studios.title)
    print("Host ID: " + str(studios.host_id))
    print("Stats: " + str(studios.stats))
    print("Changed: " + str(studios.modified))
    print()
    historyShown = input("Y to see history and N for no: ")
    if historyShown == "Y":
      print()
      from ScraGet import ScraGet
      studios = ScraGet.get_studio()
      studios.updateScratch(searchStudio)
      print(studios.history)
      print()
    else:
      print("Ok")
  elif searchingFor == "P":
    searchProject = input("What is the project ID? ")
    print()
    print("Project Data: ")
    from ScraGet import ScraGet
    project = ScraGet.get_project()
    project.updateScratch(searchProject)
    print("Title: " + str(project.title))
    print("Shared on: " + str(project.shared))
    print("Stats: " + str(project.stats))
    print()

  else:
    print()
    print("Invalid. Please type S, P or U.")
    print()
