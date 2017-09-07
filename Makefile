run:
	FLASK_APP=main.py flask run

commit:
	pip freeze > requirements.txt

activate:
	source venv/bin/activate

