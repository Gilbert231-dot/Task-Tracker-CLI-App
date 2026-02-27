import sys
import json
from datetime import datetime
import pprint

print("\nThis is my 'Task Tracker CLI App'\n")

# Load data from .json file but
# create one if it doesn't exist.
filename = "task_container.json"   
try:
    with open(filename, "r", encoding='utf-8') as f:
        container = json.load(f)
except FileNotFoundError:
    container = {}

# Add data to .json file
def Add():
    # load existing data
    with open(filename, "r", encoding='utf-8') as f:
        container = json.load(f)

    # Take user Input
    user = " ".join(sys.argv[2:])
    # Date
    t = datetime.now().strftime("%d/%m/%Y, %H:%M")
    changes = {
        'task': user,
        'status': 'todo',
        'created_At': t,
        'Updated_At': t    
    }    
    container[len(container)+1] = changes

    # Write data to .json file
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(container, f, indent=2)

    # Show Task in CLI
    for key,value in container.items():
        print(f"ID: {key}| Task: {value['task']}| Status: {value['status']}")
        pprint.pprint('='*60) 

    print(f"Task added: {user}")
    return print(f"\n'task': {user},\n'status': 'todo',\n'created_At': {t},\n'Updated_At': {t}")



def Update():
    # Tell user to enter ID and New Task
    if len(sys.argv) < 3:
        print("Please Enter ID and New Task to Update.")

    # Get Task ID
    Use_id = sys.argv[2]
    # Get New Task
    update_task = " ".join(sys.argv[3:])

    # Updated Date
    update_time = datetime.now().strftime("%d/%m/%Y, %H:%M")
    existing_dict = container[Use_id]
    existing_dict['task'] = update_task
    existing_dict['Updated_At'] = update_time

    with open(filename, "w", encoding='utf-8') as f:
        json.dump(container, f, indent=2)

    for key,value in container.items():
        print(f"ID: {key}| Task: {value['task']}| Status: {value['status']}")
        pprint.pprint('='*60) 

    return print(f"Created_At: {existing_dict['created_At']}\nUpdated_At: {existing_dict['Updated_At']}")


def Status():
    with open(filename, "r", encoding='utf-8') as f:
        container = json.load(f)
    
    if len(sys.argv) < 3:
        print("Enter task ID to see status.")
        return
    task_id = sys.argv[2]
    print(f"Status is: '{container[task_id]['status']}'")    
    
    which_status = input("Enter\n '0' for todo,\n '1' for In Progress,\n '2' for Done\n: ")
    if which_status.capitalize() == '0':
        container[task_id]['status'] = 'todo'
        print(f"Status has been set to: '{container[task_id]['status']}'")
    elif which_status.capitalize() == '1':
        container[task_id]['status'] = 'In Progress'
        print(f'Status has been set to: {container[task_id]['status']}')
    elif which_status.capitalize() == '2':
        container[task_id]['status'] = 'Done'
        print(f"Status has been set to: {container[task_id]['status']}")
    else:
        print('Invalid Input.')

    for key,value in container.items():
        print(f"ID: {key}| Task: {value['task']}| Status: {value['status']}")
        pprint.pprint('='*60) 

    with open(filename, "w", encoding='utf-8') as f:
        json.dump(container, f, indent=2)





def Delete():
    global container
    with open(filename, "r", encoding='utf-8') as f:
        container = json.load(f)


    if len(sys.argv) < 3:
        print("Enter task_id to Delete.")
        return
    task_id = sys.argv[2]
    
    if task_id in container:
        print(f"'{container[task_id]['task']}' has been removed.")
        del container[task_id]
        container_copy = container.copy()
        container_copy.clear()

        for key,value in container.items():
            container_copy[len(container_copy)+1] = value
        container.clear()
        container = container_copy
        
    else:
        print(f"Please ID: {task_id} does not exist.")

    for key,value in container.items():
        print(f"ID: {key}| Task: {value['task']}| Status: {value['status']}")
        pprint.pprint('='*60)    

    with open(filename, "w", encoding='utf-8') as f:
        json.dump(container, f, indent=2)
    return





def Listing():
    for key,value in container.items():
        print(f"ID: {key}| Task: {value['task']}| Status: {value['status']}")
        pprint.pprint('='*60)
        
    return

def All_todo():
    for key,value in container.items():
        if value['status'] == 'todo':
            print(f"ID: {key}| Task: {value['task']}| Status: {value['status']}")
        else:
            print("There is no Task with 'status': 'todo'")
    return

def All_Done():
    for key,value in container.items():
        if value['status'] == 'Done':
            print(f"ID: {key}| Task: {value['task']}| Status: {value['status']}")
        else:
            print("There is no Task with 'status': 'Done'")
    return
    


def All_In_Progress():
    for key,value in container.items():
        if value['status'] == 'In progress':
            print(f"ID: {key}| Task: {value['task']}| Status: {value['status']}")
        else:
            print("There is no Task with 'status': 'Inprogress'")
    return

print("""\n
                Available commands:""")
tab = '\t'
table = '='*34
dashes = '-'*34
print(f"{tab}{table}")
print("        | Add    | Delete   | Inprogress |")
print(f"{tab}{dashes}")
print("        | Update | Listing  |            |")
print(f"{tab}{dashes}")
print("        | Status | Done     |            |")
print(f"{tab}{table}\n")


def main():
    try:
        if len(sys.argv) < 2:
            print("""\nPlease specify a command.
                    Available commands:""")
            tab = '\t'
            table = '='*34
            dashes = '-'*34
            print(f"{tab}{table}")
            print("        | Add    | Delete   | Inprogress |")
            print(f"{tab}{dashes}")
            print("        | Update | Listing  |            |")
            print(f"{tab}{dashes}")
            print("        | Status | Done     |            |")
            print(f"{tab}{table}\n")
    
        command = sys.argv[1]

        if command.capitalize() == 'Add':
            Add()

        elif command.capitalize() == 'Delete':
            Delete()

        elif command.capitalize() == 'Inprogress':
            All_In_Progress()

        elif command.capitalize() == 'Update':
            Update()

        elif command.capitalize() == 'Listing':
            Listing()

        elif command.capitalize() == 'Status':
            Status()

        elif command.capitalize() == 'Done':
            All_Done()
        elif command.capitalize() == 'Todo':
            All_todo()

        else:
            print(f"Please the command: {command} does not exist.")

    except UnboundLocalError,IndexError:
        print("Please Try again...")

if __name__ == "__main__":
    main()