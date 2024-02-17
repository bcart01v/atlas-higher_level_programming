-- This script will, You guessed it! Create a user.

CREATE USER IF NOT EXISTS 
'user_0d_1'@'localhost' 
IDENTIFIED BY 'user_0d_1';

GRANT ALL PRIVILEGES ON *.* 
TO 'user_0d_1'@'localhost';

-- Need to flush privileges, otherwise the server needs to be restarted.
FLUSH PRIVILEGES;