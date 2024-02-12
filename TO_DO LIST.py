# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:27:09 2024

@author: aryap
"""

import os


class TodoItem:
    def __init__(self, description, done=False):
        self.description = description
        self.done = done


def add_item(todo_list):
    description = input("Add New Task: ")
    todo_list.append(TodoItem(description))
    save_list(todo_list)


def edit_item(todo_list, index):
    new_description = input(f"Edit Task {index + 1}: ")
    todo_list[index].description = new_description
    save_list(todo_list)


def remove_item(todo_list, index):
    confirmation = input(f"Remove Task {index + 1}? (y/N): ")
    if confirmation.lower() == "y":
        del todo_list[index]
    save_list(todo_list)

def mark_done(todo_list, index):
    todo_list[index].done = True
    save_list(todo_list)


def mark_undone(todo_list, index):
    todo_list[index].done = False
    save_list(todo_list)


def print_list(todo_list):
    os.system("cls") if os.name == "nt" else os.system("clear")
    print("MY To-Do LIST:")
    print("-" * 20)
    for i, item in enumerate(todo_list):
     print(f"{i+1}. {item.description}")

def load_list():
   if os.path.exists("todo_list.txt"):
     with open("todo_list.txt", "r") as f:
         todo_list = []
         for line in f.readlines():
             description, done = line.strip().split(",")
             todo_list.append(TodoItem(description, done=="True"))
     return todo_list
   else:
     return[]




def save_list(todo_list):
     with open("todo List.txt", "w") as f: 
         for item in todo_list:
             f.write("{item.description}, {item.done}\n")
             
todo_list = load_list()
1
while True:
      print_list(todo_list)
      print("\nWhat would you like to do?")
      print("1. Add a new task")
      print("2. Edit a task")
      print("3. Remove a task")
      print("4. Mark a task as done")
      print("5. Mark a task as undone")
      print("6. Quit")
      choice = input("> ")
      
      if choice == "1":
          add_item(todo_list)
      elif choice == "2":
          index= int(input("Enter task number to edit: ")) - 1
          edit_item(todo_list, index)
      elif choice == "3":
          index= int(input("Enter task number to remove: ")) - 1 
          remove_item(todo_list, index)
      elif choice == "4":
          index= int(input("Enter task number to mark done: ")) - 1 
          mark_done(todo_list, index)
      elif choice == "5":
          index= int(input("Enter task number to mark undone: ")) - 1
          mark_undone (todo_list, index)
      elif choice == "6":
          break
      else:
          print("Invalid choice. Please try again.")
          
print("Goodbye!")
