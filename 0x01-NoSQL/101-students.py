def top_students(mongo_collection):
    # Aggregate pipeline to calculate the average score for each student
    pipeline = [
        {
            '$project': {
                'name': 1,
                'averageScore': {
                    '$avg': '$topics.score'
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]

    # Perform the aggregation
    results = mongo_collection.aggregate(pipeline)
    
    # Convert the results to a list and return
    return list(results)