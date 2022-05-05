SELECT
    pg_terminate_backend(pid)
FROM
    pg_stat_activity
WHERE
        pid <> pg_backend_pid()
  AND datname = 'fa_test'
;

-- postgres
DROP DATABASE IF EXISTS fa_test;
DROP USER IF EXISTS fa_test;
CREATE USER fa_test WITH PASSWORD 'fa_test';
CREATE DATABASE fa_test;
GRANT ALL PRIVILEGES ON DATABASE fa_test to fa_test;
ALTER ROLE fa_test SUPERUSER;


ALTER ROLE fa_test SET client_encoding TO 'utf8';
ALTER ROLE fa_test SET default_transaction_isolation TO 'read committed';
ALTER ROLE fa_test SET timezone TO 'UTC';


