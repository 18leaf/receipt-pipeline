-- db/init.sql  ─ executed automatically by the MySQL image
CREATE TABLE receipt (
    id          BIGINT PRIMARY KEY AUTO_INCREMENT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    vendor      VARCHAR(64),
    total       DECIMAL(8,2),
    raw_json    JSON
);

CREATE TABLE item (
    id         BIGINT PRIMARY KEY AUTO_INCREMENT,
    receipt_id BIGINT,
    name       VARCHAR(64),
    canonical  VARCHAR(64),
    price      DECIMAL(8,2),
    confidence FLOAT,
    CONSTRAINT fk_receipt FOREIGN KEY (receipt_id) REFERENCES receipt(id)
);
