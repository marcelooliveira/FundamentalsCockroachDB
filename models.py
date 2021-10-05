from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import INT

Base = declarative_base()

class Score(Base):
    """
    Represents rows of the scores table.

    Arguments:
        Base {DeclaritiveMeta} -- Base class for declarative SQLAlchemy class definitions that produces appropriate `sqlalchemy.schema.Table` objects.

    Returns:
        Score -- Instance of the Score class.
    """
    __tablename__ = 'scores'
    id = Column(UUID, primary_key=True)
    playername = Column(String)
    score = Column(INT)

    def __repr__(self):
        return "<Score(playerName='{0}', id='{1}', score='{2}')>".format(
            self.playername, self.id, self.score)
