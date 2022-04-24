CREATE TABLE applicant
(
    id SERIAL PRIMARY KEY,
    first_name CHARACTER VARYING(30),
    last_name CHARACTER VARYING(30),
    tg_id CHARACTER VARYING(30) UNIQUE,
    email CHARACTER VARYING(30),
    direction CHARACTER VARYING(90),
    experience CHARACTER VARYING(400),
    university CHARACTER VARYING(120),
    graduation_year int,
    city_for_employment CHARACTER VARYING(20),
    hobby CHARACTER VARYING(90),
    topics_for_discussion CHARACTER VARYING(150),
    Age INTEGER
);