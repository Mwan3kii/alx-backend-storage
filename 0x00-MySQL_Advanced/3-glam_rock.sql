-- Create table if not exists

CREATE TABLE IF NOT EXISTS metal_bands (
    band_name VARCHAR(255),
    main_style VARCHAR(255),
    formed YEAR,
    split YEAR
)
SELECT band_name, (IFNULL(split, '2020') - formed) AS lifespan
    FROM metal_bands
    WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
    ORDER BY lifespan DESC;