CREATE USER teacher WITH PASSWORD 'qweR1tyFUn123';
GRANT CONNECT ON DATABASE postgres TO teacher;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO teacher;
GRANT SELECT,
    INSERT,
    UPDATE,
    DELETE ON Mark,
    Homework,
    Presence TO teacher;