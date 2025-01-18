CREATE TABLE IF NOT EXISTS reviews (
    ID SERIAL PRIMARY KEY,
    student VARCHAR(255) NOT NULL,
    student_type VARCHAR(255) NOT NULL,
    gym_location VARCHAR(255) NOT NULL,
    rating INT,
    comment VARCHAR(255) NOT NULL
);