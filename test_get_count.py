#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

# Count all objects and State objects
print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

# Get the list of State objects
state_objects = list(storage.all(State).values())

if state_objects:
    # Check if the list is not empty before accessing the first element
    first_state_id = state_objects[0].id
    print("First state: {}".format(storage.get(State, first_state_id)))
else:
    print("No State objects found.")
