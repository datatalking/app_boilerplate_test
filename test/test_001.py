# test_load_pyproject_toml.py

import os
import tomli

Optional = bool


# TODO refactor to test if pyproject_toml is included and has which tier of code
# TODO there are eight tiers TEST feature for now
def load_pyproject_toml(use_pep517: Optional[bool], pyproject_toml: str, setup_py: str, req_name: str):
	# TODO define, test, write Optional[BuildSystemDetails]:
	"""Load the pyproject.toml file.
	Parameters:
		use_pep517 - Has the user requested PEP 517 processing? None
					 means the user hasn't explicitly specified.
		pyproject_toml - Location of the project's pyproject.toml file
		setup_py - Location of the project's setup.py file
		req_name - The name of the requirement we're processing (for
				   error reporting)
	Returns:
		None if we should use the legacy code path, otherwise a tuple
		(
			requirements from pyproject.toml,
			name of PEP 517 backend,
			requirements we should check are installed after setting
				up the build environment
			directory paths to import the backend from (backend-path),
				relative to the project root.
		)
	"""

	pyproject_toml = 'pyproject_toml.'

	has_pyproject = os.path.isfile(pyproject_toml)
	has_setup = os.path.isfile(setup_py)

	if not has_pyproject and not has_setup:
		raise InstallationError(
			f"{req_name} does not appear to be a Python project: "
			f"neither 'setup.py' nor 'pyproject.toml' found."
		)

	if has_pyproject:
		with open(pyproject_toml, encoding="utf-8") as f:
			pp_toml = tomli.loads(f.read())
