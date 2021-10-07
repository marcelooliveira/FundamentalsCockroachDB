from models import Score

def get_scores_txn(session):
    """
    Select rows of the scores table.

    Arguments:
        session {.Session} -- The active session for the database connection.

    Returns:
        List -- A list of dictionaries containing score information.
    """
    query = session.query(Score)
    scores = query.all()
    scores.sort(reverse=True, key=lambda e: e.score)
    
    result = list(map(lambda score, i: { 'id': score.id,
                                  'ranking': i + 1,
                                  'playername': score.playername,
                                  'score': score.score
                                  },
                                  scores,
                                  list(range(len(scores)))))

    return result



