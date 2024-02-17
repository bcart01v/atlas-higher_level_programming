-- This script will update Bob's score.
--Trim leading and trailing spaces, and covert to uppercase so we don't miss any records.
UPDATE second_table SET score = 10 WHERE TRIM(UPPER(NAME)) = 'BOB';