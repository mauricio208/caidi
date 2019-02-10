cd frontend
npm run build
cd ..
python manage.py collecstatic
cp -r homepage/ build
cp -r manage.py build/
cp -r public build/
cp -r templates/ build/

