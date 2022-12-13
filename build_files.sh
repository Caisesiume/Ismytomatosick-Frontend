# build_files.sh
echo "BUILD START"
python -m pip install -r requirements.txt
python TomatoDiagnostics/manage.py collectstatic --noinput --clear
echo "BUILD END"