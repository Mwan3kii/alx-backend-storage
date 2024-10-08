-- Create table if not exists
SELECT band_name, (IFNULL(split, '2020') - formed) AS lifespan
    FROM metal_bands
    WHERE FIND_IN_SET('Glam rock', IFNULL(main_style, "")) > 0
    ORDER BY lifespan DESC;