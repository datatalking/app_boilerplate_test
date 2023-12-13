# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import timeline
import app
import os

# timeline()
# app()


def main():
	print_hi(user_name)
	project_TODO_scanner()


def get_username_os():
	"""
	obtain the computer users name from the local os
	:param name:
	:return:
	"""

	return user_name


def print_hi(name):
	"""
	Use a breakpoint in the code line below to debug your script
	:param name:
	:return:
	"""
	print(f'Hi, {user_name}')  # Press ⌘F8 to toggle the breakpoint.


def project_TODO_scanner():
	"""
	Here we import the TODO_scanner to add to task_pipeline, github issues, TOML
	:param name:
	:return:
	"""
	pass


def connect_app_database():
	"""
	connect to .env for database specified
	:param name:
	:return:
	"""
	# TODO pull from sql_template
	pass


# TODO write tests for database from a cookie cutter template, add sphinx


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	user_name = get_username_os()
	print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
