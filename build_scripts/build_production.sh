sh build_scripts/clean_last_build.sh
cd frontend
npm run build
cd ..
python manage.py collectstatic
tar -czvf build.tar.gz gaidi/ appointments_manager/ manage.py public templates/ frontend/webpack-stats.json
scp build.tar.gz root@206.189.215.46:~/

