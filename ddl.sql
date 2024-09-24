-- Create the Scan table if it does not exist
CREATE TABLE IF NOT EXISTS scans (
    id SERIAL PRIMARY KEY,
    start TIMESTAMP NOT NULL,
    finish TIMESTAMP
);

-- Create the ResourceType enum if it does not exist
DO $$ 
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'resource_type') THEN
        CREATE TYPE resource_type AS ENUM ('User', 'Group', 'Repository', 'Branch');
    END IF;
END $$;

-- Create the Resource table with a composite primary key (scan_id, urn)
CREATE TABLE IF NOT EXISTS resources (
    scan_id INT REFERENCES scans(id) ON DELETE CASCADE NOT NULL,
    urn VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    type resource_type NOT NULL,
    date_fetched TIMESTAMP NOT NULL,
    data JSONB,
    PRIMARY KEY (scan_id, urn)
);

-- Create additional indexes if they do not exist
CREATE INDEX IF NOT EXISTS idx_scans_start ON scans(start);
CREATE INDEX IF NOT EXISTS idx_scans_finish ON scans(finish);
CREATE INDEX IF NOT EXISTS idx_resources_type ON resources(type);
