# ticket_management.py

import os

FILENAME = "tickets.txt"

def load_tickets():
    """Load tickets from file as a list of dictionaries"""
    tickets = []
    if not os.path.exists(FILENAME):
        return tickets
    with open(FILENAME, "r") as file:
        for line in file:
            line = line.strip()
            if line:  # skip empty lines
                tid, name, issue = line.split("|")
                tickets.append({"id": tid, "name": name, "issue": issue})
    return tickets

def save_tickets(tickets):
    """Save tickets to file"""
    with open(FILENAME, "w") as file:
        for ticket in tickets:
            file.write(f"{ticket['id']}|{ticket['name']}|{ticket['issue']}\n")

def create_ticket(tickets):
    """Add a new ticket"""
    tid = str(len(tickets) + 1)  # simple incremental ID
    name = input("Enter customer name: ")
    issue = input("Enter issue description: ")
    tickets.append({"id": tid, "name": name, "issue": issue})
    print(f"Ticket {tid} created!")

def view_tickets(tickets):
    """Display all tickets"""
    if not tickets:
        print("No tickets found!")
