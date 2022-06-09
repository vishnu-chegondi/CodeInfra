import hashlib

from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users_table'

    username = Column(String, primary_key=True)
    password = Column(String)

    def __repr__(self):
        return "<User(username={})>".format(self.username)

    def set_password(self, raw_password):
        self.password = hashlib.sha512(raw_password.encode()).hexdigest()

    def verify_password(self, raw_password):
        if self.password == hashlib.sha512(raw_password.encode()).hexdigest():
            return True
        else:
            return False


class Templates(Base):
    __tablename__ = "templates_table"

    template = Column(String, primary_key=True)
    cloud = Column(String)
    vpc = Column(String)
    private_subnets = Column(Integer)
    public_subnets = Column(Integer)
    ownername = Column(String, ForeignKey("users_table.username"))
    owner = relationship(User)

    def __repr__(self):
        return "<Template {}>".format(self.template)
