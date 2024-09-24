import json


class ResourceRepository:
    def __init__(self, connection):
        self.connection = connection

    def get_resources(self, scan_id=None, type=None):
        query = "SELECT * FROM resources WHERE TRUE"
        params = []

        if scan_id:
            query += " AND scan_id = %s"
            params.append(scan_id)
        if type:
            query += " AND type = %s"
            params.append(type)

        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

    def create_resource(self, scan_id, urn, name, type, date_fetched, data):
        query = """
        INSERT INTO resources (scan_id, urn, name, type, date_fetched, data)
        VALUES (%s, %s, %s, %s, %s, %s);
        """
        data_json = json.dumps(data) if data else None
        with self.connection.cursor() as cursor:
            cursor.execute(query, (scan_id, urn, name, type, date_fetched, data_json))
            self.connection.commit()
