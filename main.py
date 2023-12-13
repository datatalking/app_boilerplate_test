# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from timeline import main as main_timeline
import app
import os

# timeline()
# app()


def main():
	get_username_os(user_name)
	print_hi(user_name)
	project_TODO_scanner()
	run_timeline()


def get_username_os(user_name):
	"""
	obtain the computer users name from the local os
	:param name:
	:return:
	"""
	print(f'{user_name}, get_username_os has run')
	return os.getenv("USERNAME")


def print_hi(user_name):
	"""
	Use a breakpoint in the code line below to debug your script
	:param user_name:
	:return:
	"""
	print(f'Hi, {user_name}')  # Press ⌘F8 to toggle the breakpoint.


def project_TODO_scanner():
	"""
	Here we import the TODO_scanner to add to task_pipeline, github issues, TOML
	:param name:
	:return:
	"""
	print(f'{user_name}, project_TODO_scanner has run')
	return


def connect_app_database():
	"""
	connect to .env for database specified
	:param name:
	:return:
	"""
	print(f'{user_name}, connect_app_database has run')
	# TODO pull from sql_template
	return


def run_timeline():
	"""
	ingest the timeline.py script and run it from main to ensure a full working pipeline
	:return:
	"""
	main_timeline()
	print(f"{run_timeline}, has run")


# TODO write tests for database from a cookie cutter template, add sphinx


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	user_name = os.environ.get("USER")
	print_hi(f'{user_name},you are USER')
	main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
