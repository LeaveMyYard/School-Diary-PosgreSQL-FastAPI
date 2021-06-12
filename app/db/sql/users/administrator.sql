CREATE ROLE administrator;
GRANT CONNECT ON DATABASE postgres TO administrator;
GRANT SELECT,
    INSERT,
    UPDATE,
    DELETE ON ALL TABLES IN SCHEMA public TO administrator;