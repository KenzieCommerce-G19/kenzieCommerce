set -0 errexit

pip install -r requirements.txt
python manage.py collectsstatic --no-input
python manage.py migrate