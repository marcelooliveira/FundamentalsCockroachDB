from models import Score

def get_scores_txn(session):
    """
    Select rows of the scores table.

    Arguments:
        session {.Session} -- The active session for the database connection.

    Returns:
        List -- A list of dictionaries containing score information.
    """
    scores = session.query(Score).all()
    return list(map(lambda score: {'id': score.id,
                                  'name': score.playername,
                                  'score': score.score},
                    scores))
