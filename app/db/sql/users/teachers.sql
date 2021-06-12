CREATE ROLE teacher;
GRANT CONNECT ON DATABASE postgres TO teacher;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO teacher;
GRANT SELECT,
    INSERT,
    UPDATE,
    DELETE ON Mark,
    Homework,
    Presence IN SCHEMA public TO teacher;