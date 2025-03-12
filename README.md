# Django Recipe API

A Recipe API built using Django, Docker, and integrated with GitHub Actions for continuous integration.

## Features

- **Recipe Management**: CRUD operations to create, read, update, and delete recipes.
- **Docker Integration**: Containerized application using Docker for consistent development and deployment environments.
- **Continuous Integration**: Automated testing and linting with GitHub Actions to ensure code quality.

## Installation

To set up the project locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ain-py/django-recip-api.git
   cd django-recip-api
   ```

2. **Build and start the Docker containers**:

   Ensure you have Docker installed on your system. Then, run:

   ```bash
   docker-compose up --build
   ```

   This command will build the Docker images and start the containers as defined in the `docker-compose.yml` file.

3. **Apply database migrations**:

   Once the containers are running, apply the migrations to set up the database schema:

   ```bash
   docker-compose exec app python manage.py migrate
   ```

4. **Create a superuser**:

   To access the Django admin interface, create a superuser account:

   ```bash
   docker-compose exec app python manage.py createsuperuser
   ```

5. **Access the application**:

   - API Root Endpoint: `http://localhost:8000/api/`
   - Django Admin: `http://localhost:8000/admin/`

## Running Tests

To run tests and check code linting:

```bash
docker-compose exec app sh -c "python manage.py test && flake8"
```


This command executes the test suite and runs flake8 for linting checks.

## Continuous Integration

This project utilizes GitHub Actions for continuous integration. The configuration is defined in the `.github/workflows` directory. On each push or pull request, the workflow runs the test suite and linting checks to ensure code quality.

## Deployment

For deployment:

1. **Set environment variables**: Ensure all necessary environment variables (e.g., `DEBUG`, `ALLOWED_HOSTS`, `DATABASE_URL`, `SECRET_KEY`) are correctly configured.
2. **Static and media files**: Configure a cloud storage service (like AWS S3 or Cloudinary) for handling static and media files in production.
3. **Web server configuration**: Use a production-ready web server setup, such as Nginx paired with Gunicorn or uWSGI, to serve the application.
4. **CI/CD**: Implement Continuous Integration and Continuous Deployment pipelines using tools like GitHub Actions to automate testing and deployment processes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

