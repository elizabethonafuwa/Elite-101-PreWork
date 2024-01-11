def welcome_user():
  print("Welcome to the ChatBot!")

def get_user_info():
  name = input("What's your name? ")
  age = input("How old are you? ")
  return name, age

def help_user():
  print("How can I help you?")
  # You can add more details or options here

def show_menu():
  print("\nMenu:")
  print("1. Option 1")
  print("2. Option 2")
  print("3. Exit")

def chatbot():
  welcome_user()
  name, age = get_user_info()
  print(f"\nHello {name}! Nice to meet you. You are {age} years old.")

  while True:
      show_menu()
      choice = input("Choose an option (1-3): ")

      if choice == "1":
          print("You selected Option 1. Placeholder action.")
      elif choice == "2":
          print("You selected Option 2. Placeholder action.")
      elif choice == "3":
          print("Goodbye! Have a great day!")
          break
      else:
          print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
  chatbot()

