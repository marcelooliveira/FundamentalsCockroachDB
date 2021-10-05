from cockroachdb.sqlalchemy import run_transaction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from transactions import get_scores_txn

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
                              lambda session: get_scores_txn(session))

