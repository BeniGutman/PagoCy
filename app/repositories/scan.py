class ScanRepository:
    def __init__(self, connection):
        self.connection = connection

    def get_scans(self):
        query = "SELECT * FROM scans"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def create_scan(self, start, finish):
        query = """
        INSERT INTO scans (start, finish)
        VALUES (%s, %s) RETURNING id;
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (start, finish))
                scan_id = cursor.fetchone()["id"]
                self.connection.commit()
                return scan_id
        except Exception as e:
            self.connection.rollback()
            raise Exception(f"Failed to create scan: {str(e)}")
