-- create a test database and user
CREATE USER IF NOT EXISTS "hbnb_test"@"localhost" IDENTIFIED BY "hbnb_test_pwd";
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
GRANT ALL ON hbnb_test_db.* TO "hbnb_test"@"localhost";
GRANT SELECT ON performance_schema.* TO "hbnb_test"@"localhost";
