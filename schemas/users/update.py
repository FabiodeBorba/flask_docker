import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from database import db_session,User as UserModel
from sqlalchemy import and_
from users import Users


class changeUser(graphene.Mutation):
    class Input:
        email = graphene.String()

    ok      = graphene.Boolean()
    user    = graphene.Field(Users)

    @classmethod
    def mutate(cls, _, args, context, info):
        query = Users.get_query(context)
        email = args.get('email')
        user = query.filter(UserModel.email == email).first()
        db_session.commit()
        ok = True

        return changeUser(user=user, ok=ok)
