# Module 5: Fundamental Data Structures — Stacks and Queues

## Description

This project implements four fundamental data structures using Python: ArrayStack, LinkedStack, ArrayQueue, and LinkedQueue. It includes a menu-driven program that allows users to perform stack and queue operations and view the current state after each operation.

The program also includes a balanced-parentheses checker and a print queue simulation that processes print jobs in FIFO order.

## Files

- `array_stack.py` — Implements a stack using an array (Python list) with a fixed capacity.
- `linked_stack.py` — Implements a stack using a linked list.
- `array_queue.py` — Implements a circular array queue with a fixed capacity.
- `linked_queue.py` — Implements a linked queue using head and tail references.
- `main.py` — Contains the menu-driven program and application exercises.
- `analysis.md` — Contains the written answer to the analysis question.

## Requirements

- Python 3

## How to Run

1. Download or clone this repository.
2. Make sure all Python files are saved in the same folder.
3. Open a terminal in that folder.
4. Run the following command:

   `python main.py`

   If your computer uses the Python launcher, you can run:

   `py main.py`

5. Select an option from the main menu.
6. Follow the instructions displayed by the program.

## Features

### ArrayStack
- Push an item
- Pop the top item
- Peek at the top item
- Check whether the stack is empty or full
- Detect overflow and underflow

### LinkedStack
- Push an item at the head
- Pop the top item
- Peek at the top item
- Check whether the stack is empty or full
- Detect underflow

### Circular ArrayQueue
- Enqueue an item
- Dequeue the front item
- Peek at the front item
- Check whether the queue is empty or full
- Reuse array positions through circular wrap-around
- Detect overflow and underflow

### LinkedQueue
- Enqueue an item at the tail
- Dequeue an item from the head
- Peek at the front item
- Check whether the queue is empty or full
- Detect underflow

### Application Exercises
- Check whether parentheses, brackets, and braces are balanced.
- Simulate a print queue using job IDs and page counts.
- Process print jobs in First In, First Out (FIFO) order.

## Error Handling

The program displays descriptive error messages when a stack or queue is empty or full. Invalid menu choices and invalid capacity or page-count inputs are also handled.

## Author

Name: Keith Ablow B. Mabanag

Course: BSIT

Year & Section: 2nd Year, BSIT – 2A
