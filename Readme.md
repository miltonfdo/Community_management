Setting up the project:
This project is created on Python 3.10.2

Step 1 : Setup python virtual environment
  Command syntax -> python -m venv <name_of_virtualenv>
  Command -> python -m venv pyEnv

Step 2: Activate the Virtual environment
 Command -> .\pyEnv\Scripts\activate 


Step 3: Install are dependent python packages
 Command -> pip install -r requirements.txt


Note:
 If any new package is being added newly in the project update the requitemnt.txt file, this can automatically be done by running below command
  -> pip freeze > requirements.txt