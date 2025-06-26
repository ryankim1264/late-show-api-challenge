from server.app import create_app
app = create_app()

from server.extentions import db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from werkzeug.security import generate_password_hash

def seed():
    with app.app_context():
        
        
        db.drop_all()
        db.create_all()

        
        user1 = User(username="Kim", password_hash=generate_password_hash("kim123"))
        db.session.add(user1)

        
        guest1 = Guest(name="Kimutai ryan", occupation="Artist")
        guest2 = Guest(name="Lamar mwende", occupation="Singer")

        
        episode1 = Episode(date="2023-06-01", number=177)
        episode2 = Episode(date="2023-06-02", number=129)

        db.session.add_all([guest1, guest2, episode1, episode2])
        db.session.commit()

        
        appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
        appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode2.id)

        db.session.add_all([appearance1, appearance2])
        db.session.commit()

print("seeded")
        

if __name__ == "__main__":
    seed()