--
CREATE TABLE IF NOT EXISTS second_table
(id INT DEFAULT NULL, name VARCHAR(256), score INT);
INSERT INTO `second_table`(`id`, `name`, `score`)
VALUES

    (1, "john", 10),
    (2, "ALEX", 3),
    (3, "Bob", 14),
    (4, "George", 8);