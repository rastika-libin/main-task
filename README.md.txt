1. Extract the project folder.
2. Make sure Docker and Docker Compose are installed on your machine.
3. In the project directory, run the following commands:
   - `docker-compose build`
   - `docker-compose up`
4. Once the containers are up, run:
   - `docker-compose exec web python manage.py migrate`
5. Your Django app should be accessible at http://localhost:8000.
