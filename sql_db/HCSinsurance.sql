CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE car (
    licenseplate VARCHAR(8) PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    current_value FLOAT NOT NULL
);

CREATE TABLE insurance_policy (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    content TEXT NOT NULL,
    embedding VECTOR(384) NOT NULL
);

CREATE TABLE customer_policy (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    date_start DATE NOT NULL,
    price_per_month FLOAT NOT NULL,
    car_licenseplate VARCHAR(8) NOT NULL,
    insurance_policy_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer (id) ON DELETE CASCADE,
    FOREIGN KEY (car_licenseplate) REFERENCES car (licenseplate) ON DELETE CASCADE,
    FOREIGN KEY (insurance_policy_id) REFERENCES insurance_policy (id) ON DELETE CASCADE
);
