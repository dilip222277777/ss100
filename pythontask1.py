data_list = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

def initialize_data():
    return [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"}
    ]

def display_person(person):
    if person:
        print("\nPerson Details:")
        print(f"ID: {person['id']}")
        print(f"Name: {person['name']}")
        print(f"Email: {person['email']}")

def create_person(data_list):
    print("\nCreate New Person")
    new_person = {}
    new_id = max(person['id'] for person in data_list) + 1 if data_list else 1
    new_person['id'] = new_id
    new_person['name'] = input("Enter name: ")
    new_person['email'] = input("Enter email: ")
    data_list.append(new_person)
    print(f"Person created successfully with ID {new_id}!")
    return new_person

def list_all_people(data_list):
    for person in data_list:
        print(f"ID: {person['id']}, Name: {person['name']}, Email: {person['email']}")

def view_person(data_list):
    person_id = int(input("\nEnter person ID to view: "))
    person = next((p for p in data_list if p['id'] == person_id), None)
    if person:
        display_person(person)
    else:
        print(f"No person found with ID {person_id}")

def search_people(data_list):
    search_term = input("Enter name or email to search: ").lower()
    results = [p for p in data_list 
              if search_term in p['name'].lower() 
              or search_term in p['email'].lower()]
    if results:
        list_all_people(results)
    else:
        print("No matching people found.")

def update_person(data_list):
    person_id = int(input("\nEnter person ID to update: "))
    person = next((p for p in data_list if p['id'] == person_id), None)
    
    if not person:
        print("Person not found.")
        return
    
    display_person(person)
    print("\nEnter new details (leave blank to keep current value):")
    
    name = input(f"Name [{person['name']}]: ").strip()
    email = input(f"Email [{person['email']}]: ").strip()
    
    if name:
        person['name'] = name
    if email:
        person['email'] = email
    
    print("Person updated successfully!")
    display_person(person)

def delete_person(data_list):
    person_id = int(input("\nEnter person ID to delete: "))
    person = next((p for p in data_list if p['id'] == person_id), None)
    
    if person:
        data_list.remove(person)
        print(f"Person with ID {person_id} deleted successfully.")
    else:
        print("Person not found.")

def main():
    data = initialize_data()
    
    while True:
        print("\nCRUD Operations Menu")
        print("1. List all people")
        print("2. View person details")
        print("3. Search people")
        print("4. Add new person")
        print("5. Update person")
        print("6. Delete person")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            list_all_people(data)
        elif choice == '2':
            view_person(data)
        elif choice == '3':
            search_people(data)
        elif choice == '4':
            create_person(data)
        elif choice == '5':
            update_person(data)
        elif choice == '6':
            delete_person(data)
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()