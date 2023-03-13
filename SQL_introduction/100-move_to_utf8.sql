Convert first_table table to utf8mb4 character set
and utf8mb4_unicode_ci collation
ALTER TABLE
    first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;