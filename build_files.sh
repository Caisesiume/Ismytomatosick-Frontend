# build_files.sh
pip install -r requirements.txt
pip install --root-user-action=ignore requests
python3.9 TomatoDiagnostics/manage.py runserver
