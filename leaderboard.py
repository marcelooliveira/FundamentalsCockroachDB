from cockroachdb.sqlalchemy import run_transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from transactions import get_scores_txn, add_score_txn


class Leaderboard:
    """
    Wraps the database connection. The class methods wrap database transactions.
    """

    def __init__(self, conn_string):
        """
        Establish a connection to the database, creating Engine and Sessionmaker objects.

        Arguments:
            conn_string {String} -- CockroachDB connection string.
        """

        print('conn_string: ' + conn_string)

        self.engine = create_engine(conn_string, convert_unicode=True)
        self.sessionmaker = sessionmaker(bind=self.engine)


    def get_scores(self):
        """
        Wraps a `run_transaction` call that gets scores as a list of dictionaries.

        Returns:
            List -- A list of dictionaries containing score data.
        """
        return run_transaction(self.sessionmaker,
                               lambda session: self.prepare_scores(session))

    def add_score(self, score):
        return run_transaction(self.sessionmaker,
                               lambda session: add_score_txn(session, score.avatar, score.playername, score.points))

    def prepare_scores(self, session):
        scores = get_scores_txn(session)
        scores.sort(reverse=True, key=lambda e: e.points)

        result = list(map(lambda score, i: {'id': score.id,
                                            'ranking': i + 1,
                                            'avatar': self.get_avatar_dic()[str(score.avatar)],
                                            'playername': score.playername,
                                            'points': score.points
                                            },
                        scores,
                        list(range(len(scores)))))

        return result

    def get_avatar_dic(self):
        return {
        "0":"not set",
        "1":"👨🏻",
        "2":"👨🏼",
        "3":"👨🏽",
        "4":"👨🏾",
        "5":"👨🏿",
        "6":"👩🏻",
        "7":"👩🏼",
        "8":"👩🏽",
        "9":"👩🏾",
        "10":"👩🏿"
        }