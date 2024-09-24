import json
import logging
from enum import Enum
from datetime import datetime

import psycopg2
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from psycopg2.extras import RealDictCursor


# Set up logging
logging.basicConfig(
    level=logging.INFO,  # Set the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # You can add more handlers, like FileHandler, if you want to log to a file
    ]
)
logger = logging.getLogger(__name__)

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="user",
    password="password"
)

app = FastAPI()

# Models
class Scan(BaseModel):
    start: datetime
    finish: datetime = None

class Resource(BaseModel):
    scan_id: int
    urn: str
    name: str
    type: str
    date_fetched: datetime
    data: str | dict = None

# Define Enum for Resource Type Validation
class ResourceType(str, Enum):
    User = "User"
    Group = "Group"
    Repository = "Repository"
    Branch = "Branch"

# Helper function to execute queries
def execute_query(query, params=None):
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params)
            if cursor.description:
                return cursor.fetchall()
            conn.commit()
    except Exception as e:
        # If there's an error, rollback the transaction and raise the exception
        conn.rollback()
        raise e

# Endpoints

## 1. Create a new scan
@app.post("/scans/")
def create_scan(scan: Scan):
    query = """
    INSERT INTO scans (start, finish) 
    VALUES (%s, %s) RETURNING id;
    """
    result = execute_query(query, (scan.start, scan.finish))
    if not result:
        raise HTTPException(status_code=500, detail="Failed to create scan")
    return {"scan_id": result[0]['id']}

## 2. Create a new resource
@app.post("/resources/")
def create_resource(resource: Resource):
    query = """
    INSERT INTO resources (scan_id, urn, name, type, date_fetched, data)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    try:
        logger.info(resource.date_fetched)
        data_json = json.dumps(resource.data) if resource.data else None
        execute_query(query, (resource.scan_id, resource.urn, resource.name, resource.type, resource.date_fetched, data_json))
        return {"message": "Resource created successfully"}
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=400, detail=str(e))

## 3. List all scans
@app.get("/scans/")
def list_scans():
    query = "SELECT * FROM scans;"
    result = execute_query(query)
    return {"scans": result}

## 4. List all resources (filter by type and/or scan)
@app.get("/resources/")
def list_resources(
    scan_id: int = Query(None, description="ID of the scan"),
    type: ResourceType = Query(None, description="Type of the resource")
):
    # Build the dynamic SQL query
    base_query = "SELECT * FROM resources"
    filters = []
    params = []

    if scan_id:
        filters.append("scan_id = %s")
        params.append(scan_id)

    if type:
        filters.append("type = %s")
        params.append(type)

    # Add filters to the query
    if filters:
        base_query += " WHERE " + " AND ".join(filters)

    try:
        result = execute_query(base_query, params)
        return {"resources": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 5. Error handling and validation
@app.exception_handler(Exception)
def validation_exception_handler(request, exc):
    return HTTPException(status_code=400, detail=str(exc))
