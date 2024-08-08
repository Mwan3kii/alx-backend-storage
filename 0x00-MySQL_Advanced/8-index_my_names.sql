-- Create index on first letter of name column
ALTER TABLE names
ADD INDEX idx_name_first (name(1));
