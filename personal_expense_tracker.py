
#====================================================================================================
# Global Variables
#====================================================================================================
list_of_expenses = [] 
file_name = "MyExpenses.csv" 
monthly_budget = 0.0 

#====================================================================================================
# Function to get expense details from user input
#====================================================================================================
def input_expense():
    expense_input = input ("\n==================================================== \nYou pressed 1 and chose to add expenses.\nPlease enter expense date in YYYY-MM-DD format, expense category, expense amount and expense description (separated by commas) => :")
    list_input_data = expense_input.split(',',3) 

    if len(list_input_data) < 4:
        print("Error: Invalid Input. Please ensure you enter DATE, CATEGORY, AMOUNT, and DESCRIPTION, separated by commas. ")
        return None 

    date_str = list_input_data[0].strip()
    category_str = list_input_data[1].strip()
    amount_str = list_input_data[2].strip()
    description_str = list_input_data[3].strip()

    # Try to convert amount to float
    try:
        amount_float = float(amount_str)
        expense_details = {
            'Expensedate' : date_str,
            'category' : category_str,
            'amount' : amount_float, # Store as float
            'description' : description_str
        }
        print("Expense details captured.")
        return expense_details 
    except ValueError:
        print(f"Error: Invalid amount '{amount_str}'. Please enter a number for the amount.")
        return None 
#====================================================================================================
# Helper function to add expense 
#====================================================================================================
def add_expense():
    new_expense = input_expense() 
    if new_expense: 
        list_of_expenses.append(new_expense) 
        print("Expense added successfully.") 

#====================================================================================================
# Function to display all stored expenses
#====================================================================================================
def view_expense():
     print("\n******Your expenses******")

     if not list_of_expenses:
        print("No expenses recorded yet.")
        print("*************************\n")
        return

     
     for expense in list_of_expenses:
        print("**********Expense Details**********")
        print("Expensedate:", expense['Expensedate'])
        print("category:", expense['category'])
        print("amount:", f"{expense['amount']:.2f}") # Format float for display
        print("description:", expense['description'])
        print("\n")

#====================================================================================================
# Function to allow user to set the monthly budget
#====================================================================================================
def set_budget():
    global monthly_budget 
    print("\n--- Set Monthly Budget ---")
    budget_str = input("Enter your total monthly budget amount: ")

    # Try to convert input to float
    try:
        budget_float = float(budget_str)
        if budget_float >= 0: # Budget must be zero or positive
            monthly_budget = budget_float
            print(f"Monthly budget set to {monthly_budget:.2f}.")
        else:
            print("Budget cannot be negative. Budget is not set yet.")
    except ValueError:
        print("Invalid input. Please enter a number for the budget. Budget is not set yet.")

#====================================================================================================
# Function to calculate total expenses and track against the budget
#====================================================================================================
def track_budget():
    print("\n**** Budget Tracking ****")
    global monthly_budget

    if monthly_budget <= 0: 
        print("Monthly budget is not set or is zero.")
        print("Please set your budget first.") 
        print("-" * 20)
        return

    total_expenses = 0.0 

   
    for expense in list_of_expenses:
        try:
            
            expense_amount = float(expense.get('amount', 0.0))
            total_expenses += expense_amount
        except (ValueError, TypeError):
           
             print(f"Warning: Skipping non-numeric amount during tracking: {expense.get('amount', 'N/A')}")

    print(f"Total recorded expenses: {total_expenses:.2f}")
    print(f"Your monthly budget: {monthly_budget:.2f}")

    remaining_balance = monthly_budget - total_expenses

  
    if remaining_balance < 0:
        print(f"Warning: You have exceeded your budget by {-remaining_balance:.2f}!")
    else:
        print(f"You have {remaining_balance:.2f} left for the month.")

    print("-" * 20)

#====================================================================================================
# Function to format one expense dictionary as a CSV line string
#====================================================================================================
def convert_dict_to_csv(expense_dict):
    
    date_str = str(expense_dict['Expensedate'])
    category_str = str(expense_dict['category'])
    amount_str = str(expense_dict['amount']) # Convert float amount to string
    description_str = str(expense_dict['description'])

    # Join with commas and add newline
    csv_line = f"{date_str},{category_str},{amount_str},{description_str}\n"
    return csv_line


#====================================================================================================
# Function to save all expenses from the list to the file
#====================================================================================================
def save_expense(fname):
    try:
        
        file = open(fname, 'a')
        for expense in list_of_expenses:
            csv_line = convert_dict_to_csv(expense)
            file.write(csv_line)
        file.close()
        print(f"Expenses appended to {fname}.")
    except Exception as e: 
        print(f"Error saving expenses: {e}")


#====================================================================================================
# Function to load expenses from the CSV file
#====================================================================================================

def load_expenses(fname):
    global list_of_expenses
    list_of_expenses = [] 
    # Check if file exists before trying to open
 

    try:
        print(f"Attempting to load expenses from {fname}...")
        with open(fname, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

           
                parts = line.split(',', 3)

          
                if len(parts) == 4:
                    date_str = parts[0]
                    category_str = parts[1]
                    amount_str = parts[2]
                    description_str = parts[3]

                    # Try to convert amount back to float
                    try:
                        amount_float = float(amount_str)
                        # Create dictionary
                        expense = {
                            'Expensedate': date_str,
                            'category': category_str,
                            'amount': amount_float,
                            'description': description_str
                        }
                        list_of_expenses.append(expense) 
                    except ValueError:
                        print(f"Warning: Skipping load of line due to invalid amount format: {line}")
                else:
                    print(f"Warning: Skipping malformed line during load: {line}")

        print(f"Loaded {len(list_of_expenses)} expenses.")

    except Exception as e: 
        print(f"An unexpected error occurred while loading expenses: {e}")


#====================================================================================================
# Display Menu Function (Part of Step 5)
#====================================================================================================
def display_menu():
    print("\n********** Personal Expenses Manager Menu **********")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Track budget")
    print("4. Save expenses")
    print("5. Exit")
    print("****************************************************")


#====================================================================================================
# Main Program Execution (Part of Step 5)
#====================================================================================================


print("*********Welcome to your Personal expenses Manager**********")

# Load data from file when the program starts
load_expenses(file_name)

# Main application loop
while True:
    display_menu() # Show menu options

    choice = input("Enter your choice (1-5): ") # Get user input

    if choice == '1':
        add_expense() 

    elif choice == '2':
        view_expense() 

    elif choice == '3':
        
        set_budget()
        track_budget()

    elif choice == '4':
        save_expense(file_name) 

    elif choice == '5':
       
        print("\nExiting program. Saving current expenses...")
        save_expense(file_name) 
        print("Goodbye!")
        break 

    else:
        
        print("\nInvalid choice. Please enter a number between 1 and 5.")

# --- Program ends here when the loop is broken ---