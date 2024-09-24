# PostgreSQL with pgAdmin using Docker

This setup allows you to run PostgreSQL and pgAdmin in Docker containers using `docker-compose`. 

## Prerequisites

Make sure you have Docker and Docker Compose installed on your machine. 

- [Docker Installation Guide](https://docs.docker.com/get-docker/)
- [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

## Setup

### 1. Clone the repository or download the `docker-compose.yml` file.

```bash
git clone <repository-url>
cd <repository-directory>
```

---

### 2. Modify Environment Variables (Optional)

In the `docker-compose.yml` file, you can change the following environment variables according to your preferences:

- `POSTGRES_USER`: The username for your PostgreSQL instance (default is `user`).
- `POSTGRES_PASSWORD`: The password for your PostgreSQL instance (default is `password`).
- `POSTGRES_DB`: The name of the default database (default is `mydb`).
- `PGADMIN_DEFAULT_EMAIL`: The email to log in to pgAdmin (default is `admin@admin.com`).
- `PGADMIN_DEFAULT_PASSWORD`: The password for pgAdmin (default is `admin`).

---

### 3. Start the Containers

To start the PostgreSQL and pgAdmin containers, run the following command in the directory where your `docker-compose.yml` file is located:

```bash
docker-compose up -d
```

This will start both the PostgreSQL and pgAdmin containers in detached mode. 


---

### 4. Access pgAdmin

Once the containers are running, you can access pgAdmin by going to: http://localhost:8080


Use the default credentials to log in:

- **Email**: `admin@admin.com`
- **Password**: `admin`

---

### 5. Connect pgAdmin to PostgreSQL

After logging in to pgAdmin, follow these steps to connect to the PostgreSQL database:

1. Click on "Add New Server".
2. In the `General` tab, provide a name for your server (e.g., `PostgresDB`).
3. Go to the `Connection` tab and enter the following details:
   - **Host**: `postgres`
   - **Port**: `5432`
   - **Username**: The value of `POSTGRES_USER` (default is `user`).
   - **Password**: The value of `POSTGRES_PASSWORD` (default is `password`).
4. Click "Save".

You should now be able to access and manage your PostgreSQL database through pgAdmin.

## Persistent Data

The `docker-compose.yml` file is set up to persist PostgreSQL data using a Docker volume, so your data will not be lost even if you stop or remove the container.

### Data Volume
- The PostgreSQL data is stored in the `./data` directory on your host machine, which is mapped to the container's `/var/lib/postgresql/data` directory.

## Stopping the Containers

To stop the containers, run:

```bash
docker-compose down
```

If you want to remove all data along with the containers, run:

```bash
docker-compose down
```

This will also remove the volumes and persistent data.


## Notes

- Make sure to change the default credentials if you're using this setup in a production environment.
- If you want to change the ports, you can modify the `ports` section in the `docker-compose.yml` file.
