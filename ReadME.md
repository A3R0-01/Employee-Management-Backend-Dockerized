# Employee Management API

This project is an Employee Management API built with Django and Django REST framework. It provides endpoints to manage companies, departments, registrations, employees, jobs, and roles. The API also supports bulk operations for these entities, including bulk updates using CSV file uploads.

## Table of Contents

- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Bulk Operations](#bulk-operations)
- [Bulk Update with CSV](#bulk-update-with-csv)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/employee-management-api.git
   cd employee-management-api
   ```

2. Set up a virtual environment and activate it (optional):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the PostgreSQL database and update the `DATABASES` settings in `settings.py` accordingly.

5. Apply the database migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

## Dockerized Setup

The entire system is Dockerized, making it easy to set up and run. The `docker-compose.yml` file includes services for the Django application and PostgreSQL database.

### Docker Compose Configuration

```yaml
version: '3.9'

services:
  app:
    build: .
    volumes:
      - .:/dpt
    ports:
      - 8000:8000
    image: app:dpt-image
    container_name: dpt-django-container
    command: >
      sh -c "python manage.py migrate &&
             python manage.py collectstatic --noinput &&
             python manage.py runserver 0.0.0.0:8000"
    depends_on:
      - db
  db:
    image: postgres
    volumes:
      - .data/db:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=ProficiencyTest
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=1234bsrvnt
    container_name: dpt-db-container
```

### Running the Application with Docker

1. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints


### Company

- `GET /api/company/` - List all companies
- `POST /api/company/` - Create a new company
- `GET /api/company/{id}/` - Retrieve a specific company
- `PUT /api/company/{id}/` - Update a specific company
- `DELETE /api/company/{id}/` - Delete a specific company

### Department

- `GET /api/department/` - List all departments
- `POST /api/department/` - Create a new department
- `GET /api/department/{id}/` - Retrieve a specific department
- `PUT /api/department/{id}/` - Update a specific department
- `DELETE /api/department/{id}/` - Delete a specific department

### Registration

- `GET /api/registration/` - List all registrations
- `POST /api/registration/` - Create a new registration
- `GET /api/registration/{id}/` - Retrieve a specific registration
- `PUT /api/registration/{id}/` - Update a specific registration
- `DELETE /api/registration/{id}/` - Delete a specific registration

### Employee

- `GET /api/employee/` - List all employees
- `POST /api/employee/` - Create a new employee
- `GET /api/employee/{id}/` - Retrieve a specific employee
- `PUT /api/employee/{id}/` - Update a specific employee
- `DELETE /api/employee/{id}/` - Delete a specific employee

### Job

- `GET /api/job/` - List all jobs
- `POST /api/job/` - Create a new job
- `GET /api/job/{id}/` - Retrieve a specific job
- `PUT /api/job/{id}/` - Update a specific job
- `DELETE /api/job/{id}/` - Delete a specific job

### Role

- `GET /api/role/` - List all roles
- `POST /api/role/` - Create a new role
- `GET /api/role/{id}/` - Retrieve a specific role
- `PUT /api/role/{id}/` - Update a specific role
- `DELETE /api/role/{id}/` - Delete a specific role
- `POST /api/role/terminate/` - Terminate a role

## Bulk Operations

The API supports bulk operations for creating multiple records at once. Use the following endpoints for bulk operations:

- `POST /api/bulk/company/` - Bulk create companies
- `POST /api/bulk/department/` - Bulk create departments
- `POST /api/bulk/registration/` - Bulk create registrations
- `POST /api/bulk/employee/` - Bulk create employees
- `POST /api/bulk/job/` - Bulk create jobs
- `POST /api/bulk/role/` - Bulk create roles

## Bulk Update with CSV

The API allows bulk updates using a CSV file uploaded through a form under the field labeled "file". This feature is useful for updating multiple records at once.

### Example Bulk Update Request

To update multiple employees using a CSV file, send a `POST` request to `/api/bulk/employee/` with the CSV file. The form should include a field labeled "file" to upload the CSV file.

Example CSV file (`employees.csv`):

```csv
id,name,department,job
1,Updated Employee 1,1,1
2,Updated Employee 2,2,2
```

Ensure the CSV file follows the required format and includes all necessary fields for the update.

Thank You For Your Attentions