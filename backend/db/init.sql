CREATE DATABASE convergent;
use convergent;

CREATE TABLE officers (
  oid SMALLINT(4),
  name VARCHAR(50),
  role VARCHAR(50)
);

INSERT INTO officers
  (oid, name, role)
VALUES
  (1, 'Priya Barve', 'Tech Lead and Social Chair'),
  (2, 'Tesna Thomas', 'Design Lead'),
  (3, 'Kevin Jacob', 'VP');
