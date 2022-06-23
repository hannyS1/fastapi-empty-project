while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    echo "Waiting for PostgreSql to start..."
    sleep 1
done

echo "Migrate..."
alembic upgrade head

echo "Run server..."
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000