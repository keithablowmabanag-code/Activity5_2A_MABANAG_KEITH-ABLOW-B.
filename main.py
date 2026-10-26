from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def show_state(structure, structure_type):
    print("\nCurrent structure:", structure.display())

    if structure_type == "stack":
        if not structure.is_empty():
            print("Top element:", structure.peek())
        else:
            print("The stack is empty.")

    elif structure_type == "queue":
        if not structure.is_empty():
            print("Front element:", structure.peek_front())
        else:
            print("The queue is empty.")

    print("Is empty:", structure.is_empty())
    print("Is full:", structure.is_full())


def stack_menu(stack):
    while True:
        print("\n--- STACK OPERATIONS ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Check if full")
        print("6. Back to main menu")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                item = input("Enter an item to push: ")
                stack.push(item)
                print("Item pushed successfully.")
                show_state(stack, "stack")

            elif choice == "2":
                item = stack.pop()
                print("Popped item:", item)
                show_state(stack, "stack")

            elif choice == "3":
                print("Top element:", stack.peek())
                show_state(stack, "stack")

            elif choice == "4":
                print("Is empty:", stack.is_empty())
                show_state(stack, "stack")

            elif choice == "5":
                print("Is full:", stack.is_full())
                show_state(stack, "stack")

            elif choice == "6":
                break

            else:
                print("Invalid choice. Please select 1 to 6.")

        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)
            show_state(stack, "stack")


def queue_menu(queue):
    while True:
        print("\n--- QUEUE OPERATIONS ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek front")
        print("4. Check if empty")
        print("5. Check if full")
        print("6. Back to main menu")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                item = input("Enter an item to enqueue: ")
                queue.enqueue(item)
                print("Item added successfully.")
                show_state(queue, "queue")

            elif choice == "2":
                item = queue.dequeue()
                print("Dequeued item:", item)
                show_state(queue, "queue")

            elif choice == "3":
                print("Front element:", queue.peek_front())
                show_state(queue, "queue")

            elif choice == "4":
                print("Is empty:", queue.is_empty())
                show_state(queue, "queue")

            elif choice == "5":
                print("Is full:", queue.is_full())
                show_state(queue, "queue")

            elif choice == "6":
                break

            else:
                print("Invalid choice. Please select 1 to 6.")

        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)
            show_state(queue, "queue")


def balanced_parentheses():
    expression = input(
        "\nEnter an expression containing parentheses, brackets, and braces: "
    )

    stack = []
    matching = {")": "(", "]": "[", "}": "{"}
    opening = "([{"
    valid = True

    for character in expression:
        if character in opening:
            stack.append(character)

        elif character in matching:
            if not stack or stack[-1] != matching[character]:
                valid = False
                break
            stack.pop()

    if valid and not stack:
        print("Result: The parentheses are balanced.")
    else:
        print("Result: The parentheses are NOT balanced.")


def print_queue_simulation():
    jobs = []

    while True:
        print("\n--- PRINT QUEUE SIMULATION ---")
        print("1. Enqueue print job")
        print("2. Print next job")
        print("3. View waiting jobs")
        print("4. Back to main menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            job_id = input("Enter job ID: ").strip()

            if not job_id:
                print("Job ID cannot be empty.")
                continue

            if any(job["id"] == job_id for job in jobs):
                print("That job ID is already waiting.")
                continue

            try:
                pages = int(input("Enter number of pages: "))

                if pages <= 0:
                    print("Page count must be greater than zero.")
                    continue

            except ValueError:
                print("Invalid page count. Enter a whole number.")
                continue

            jobs.append({"id": job_id, "pages": pages})
            print("Print job added successfully.")
            print("Current waiting order:", jobs)

        elif choice == "2":
            if not jobs:
                print("Print queue underflow: there are no jobs to print.")
            else:
                job = jobs.pop(0)
                print("Printing job:", job["id"])
                print("Number of pages:", job["pages"])
                print("Job completed.")

                if jobs:
                    print("Next job in line:", jobs[0]["id"])
                else:
                    print("No more jobs waiting.")

                print("Remaining jobs:", jobs)

        elif choice == "3":
            if not jobs:
                print("The print queue is empty.")
            else:
                print("\nWaiting order (FIFO):")

                for position, job in enumerate(jobs, start=1):
                    print(
                        f"{position}. Job ID: {job['id']}, "
                        f"Pages: {job['pages']}"
                    )

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please select 1 to 4.")


def choose_stack():
    print("\n--- SELECT STACK IMPLEMENTATION ---")
    print("1. ArrayStack")
    print("2. LinkedStack")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        try:
            capacity = int(input("Enter stack capacity: "))

            if capacity <= 0:
                print("Capacity must be greater than zero.")
                return

            stack = ArrayStack(capacity)
            stack_menu(stack)

        except ValueError:
            print("Invalid capacity. Enter a whole number.")

    elif choice == "2":
        stack = LinkedStack()
        stack_menu(stack)

    else:
        print("Invalid choice.")


def choose_queue():
    print("\n--- SELECT QUEUE IMPLEMENTATION ---")
    print("1. Circular ArrayQueue")
    print("2. LinkedQueue")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        try:
            capacity = int(input("Enter queue capacity: "))

            if capacity <= 0:
                print("Capacity must be greater than zero.")
                return

            queue = ArrayQueue(capacity)
            queue_menu(queue)

        except ValueError:
            print("Invalid capacity. Enter a whole number.")

    elif choice == "2":
        queue = LinkedQueue()
        queue_menu(queue)

    else:
        print("Invalid choice.")


def main():
    while True:
        print("\n===================================")
        print(" FUNDAMENTAL DATA STRUCTURES")
        print("       STACKS AND QUEUES")
        print("===================================")
        print("1. ArrayStack")
        print("2. LinkedStack")
        print("3. Circular ArrayQueue")
        print("4. LinkedQueue")
        print("5. Balanced Parentheses Checker")
        print("6. Print Queue Simulation")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1" or choice == "2":
            choose_stack()

        elif choice == "3" or choice == "4":
            choose_queue()

        elif choice == "5":
            balanced_parentheses()

        elif choice == "6":
            print_queue_simulation()

        elif choice == "7":
            print("Program terminated. Thank you!")
            break

        else:
            print("Invalid choice. Please select 1 to 7.")


if __name__ == "__main__":
    main()