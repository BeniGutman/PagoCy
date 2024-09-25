-- Drop the indexes
DROP INDEX IF EXISTS idx_scans_start;
DROP INDEX IF EXISTS idx_scans_finish;
DROP INDEX IF EXISTS idx_resources_type;

-- Drop the Resource table
DROP TABLE IF EXISTS resources CASCADE;

-- Drop the ResourceType enum
DO $$ 
BEGIN
    IF EXISTS (SELECT 1 FROM pg_type WHERE typname = 'resource_type') THEN
        DROP TYPE resource_type;
    END IF;
END $$;

-- Drop the Scan table
DROP TABLE IF EXISTS scans CASCADE;
