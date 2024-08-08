-- Create index on first letter of 'name' and 'score' column
ALTER TABLE names
ADD INDEX idx_name_first_score (name(1), score);
