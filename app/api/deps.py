from db.connection import get_connection
from repositories.resource import ResourceRepository
from repositories.scan import ScanRepository


def get_resource_repository():
    conn = get_connection()
    try:
        yield ResourceRepository(conn)
    finally:
        conn.close()


def get_scan_repository():
    conn = get_connection()
    try:
        yield ScanRepository(conn)
    finally:
        conn.close()
