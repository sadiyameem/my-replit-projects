#Breach Bot Starter Code
breachYear = 2019

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of Breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since Facebook Data Breach.")


#Introduces Breach
print("Would you like to learn about the Facebook Data 2019 Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains Breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("Personal Information of 533 millions and in 106 countries was taken from Facebook users such as their full names, phone numbers, locations, some email addresses and other details were posted to amateur hacking forums. It was taken by Malicious Actors or threat actors who scraped data by exploiting a vulnerability in a low defunct feature on the platform that allowed users to find each other’s phone numbers.")
  
  elif topic.lower() == "b":
    print("The social media company (Facebook) fixed the problem in August of 2019 and they are confident that it won’t happen again. Facebook also reached out for a 5 billion deal with the U.S. Federal Trade Commission for violating an agreement with the agency to protect users' privacy. Tony Hunt created this site called HaveBeenPwnd to see if any personal data has been leaked, which has been updated by 65% of data added to the tracker from the last leaks. Facebook also did not recommend any actions from users.")
  
  elif topic.lower() == "c":
     break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reation, (c) my advice, (d) none")
  topic = input()

  if topic.lower() == "a":
    print("The data breach connects to confidentiality because private personal information was exposed to unauthorized individuals.")

  elif topic.lower() == "b":
    print("We disagree with the organization's response because Facebook said they fixed the issue in 2019, but by the time everyone found out the damage was already done. They should have taken more action to protect their user's data.")

  elif topic.lower() == "c":
     print("I would convince victims to take action by saying personal information can be used to steal valuable things such as identity and credit cards.")

  elif topic.lower() == "d":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

  input("Press enter to continue\n")

#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")