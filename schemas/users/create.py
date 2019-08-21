import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from database import db_session,User as UserModel
from sqlalchemy import and_
from users import Users

class createUser(graphene.Mutation):
    class Input:
        name    = graphene.String()
        email   = graphene.String()

    ok      = graphene.Boolean()
    user    = graphene.Field(Users)

    @classmethod
    def mutate(cls, _, args, context, info):
        user = UserModel(name=args.get('name'), email=args.get('email'))
        db_session.add(user)
        db_session.commit()
        ok = True
        return createUser(user=user, ok=ok)

