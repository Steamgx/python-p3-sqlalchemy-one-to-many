from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game, Review, Base
from faker import Faker

# Create a SQLite database
engine = create_engine('sqlite:///one_to_many.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

# Create sample games
for _ in range(5):
    game = Game(
        title=fake.catch_phrase(),
        genre=fake.word(),
        platform=fake.word(),
        price=fake.random_int(min=20, max=60)
    )
    session.add(game)

session.commit()

# Create sample reviews
games = session.query(Game).all()
for game in games:
    for _ in range(3):  # Each game gets 3 reviews
        review = Review(
            score=fake.random_int(min=1, max=10),
            comment=fake.sentence(),
            game_id=game.id
        )
        session.add(review)

session.commit()
session.close()
