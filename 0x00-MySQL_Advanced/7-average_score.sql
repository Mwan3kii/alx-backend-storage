-- creates stored procedure that computes and store avg score for student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- Update user's average_score
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END //

DELIMITER ;