from sql_alchemy import base


class UserModel(base.Model):

    __tablename__ = 'list_users'
    user_id = base.Column(base.Integer, primary_key = True)
    username = base.Column(base.String(40))
    password = base.Column(base.String(40))


    def __init__(self, username, password):
        self.username = username
        self.password = password


    def json(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
        }


    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id = user_id).first()
        if user:
            return user
        else:
            return None
    
    
    @classmethod
    def find_username(cls, username):
        username = cls.query.filter_by(username = username).first()
        if username:
            return username
        else:
            return None


    def save_user(self):
        base.session.add(self)
        base.session.commit()


    def delete_user(self):
        base.session.delete(self)
        base.session.commit()