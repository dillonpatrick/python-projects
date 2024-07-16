from database import db


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(80), nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    is_diet = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "description": self.description,
            "date": self.date,
            "is_diet": self.is_diet,
        }
