from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password@localhost/database_name'
# SQLALCHEMY_DATABASE_URL = (
#     "postgresql://postgres:anik%40841823@localhost:5432/TodoApplicationDatabase"
# )


 #mysql setup
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:Anik%40841823@127.0.0.1:3306/TodoApplicationDatabase'


#For sqllite
SQLALCHEMY_DATABASE_URL='sqlite:///./todosapp.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

#For postgresql
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()





