-- Revert tutorial:users from pg

BEGIN;

DROP TABLE users;

COMMIT;
