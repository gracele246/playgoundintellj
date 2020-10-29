# 1 is addition
# 2 is subtraction
# 3 is multiplication
# 4 is division
# 5 is power

def calc():
##############################################
  AnswerContinue=True
  while AnswerContinue:
##############################################
    print("==================")
    print("1 - addition")
    print("2 - subtraction")
    print("3 - multiplication")
    print("4 - division")
    print("5 - power")
    print("==================")
    selection = int(input("What function do you want to use? ")) 
    number_1 = input("Enter A Number ")
    number_2 = input("Enter A Number ")
    result_1 = float(number_1) + float(number_2)
    result_2 = float(number_1) - float(number_2)
    result_3 = float(number_1) * float(number_2)
    result_4 = float(number_1) / float(number_2)
    result_5 = float(number_1) ** float(number_2)

    if selection == 1:
      print(result_1)

    if selection == 2:
      print(result_2)

    if selection == 3:
      print(result_3)

    if selection == 4:
      print(result_4)

    if selection == 5:
      print(result_5)
  #############################################################
    print("Would you like to continue using the calculator?")
    print('Enter Yes or No: ')
    YourAnswer = input()
    if YourAnswer == 'Yes':
      print("Continuing....")
      AnswerContinue = True
    if YourAnswer == 'No':
      print("So long!")
      AnswerContinue = False
  ###############################################################
