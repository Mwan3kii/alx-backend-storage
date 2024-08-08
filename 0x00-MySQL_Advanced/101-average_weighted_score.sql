-- Create the stored procedure ComputeAverageWeightedScoreForUsers
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN

    -- Declare all variables
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE weighted_sum FLOAT;
    DECLARE total_weight INT;
    DECLARE avg_score FLOAT;
    
    DECLARE user_cursor CURSOR FOR 
        SELECT id FROM users;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN user_cursor;
    
    read_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SELECT SUM(c.score * p.weight) INTO weighted_sum
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;
        SELECT SUM(p.weight) INTO total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        IF total_weight = 0 THEN
            SET avg_score = 0;
        ELSE
            SET avg_score = weighted_sum / total_weight;
        END IF;

        UPDATE users
        SET average_score = avg_score
        WHERE id = user_id;
        
    END LOOP;
    CLOSE user_cursor;
END //

DELIMITER ;
