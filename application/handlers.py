from . import SessionLocal, Base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import Column, Integer, String
import json 

# Esse aqui é o handlers, This is the handlers
# Responsável por lidar com a lógica da API e interagir com o banco de dados,

class DataFormulation(Base):
    """
    Tabela de usuários no banco de dados, Users table in the database
        representa os dados do usuário coletados no formulário de inscrição, represents user data collected from the signup form

    Atributos, Attributes:
        id (Integer): Id único para cada usuário, Unique Id for each user
        name (String): Nome real do usuário, Real Name of the user
        username (String): Apelido ou nome simplificado, Nickname or simplified name
        birthdate (String): Data de nascimento no formato YYYY-MM-DD, Birthdate in the format YYYY-MM-DD
        job_title (String): Cargo ou título do trabalho, Job title
        favorite_music_genre_1 (String): Gênero musical favorito 1, Favorite music genre 1
        favorite_music_genre_2 (String): Gênero musical favorito 2, Favorite music genre 2
        favorite_music_genre_3 (String): Gênero musical favorito 3, Favorite music genre 3
        password (String): Senha do usuário, User password
        email (String): Email do usuário, User email
        numberphone (String): Número de telefone do usuário, User phone number
        cpf (String): CPF do usuário, User CPF
        address (String): Endereço do usuário, User address
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)# Id Unico para cada usuario, Unique Id for each user
    name = Column(String(50))# Nome do real do usuario, Real Name of the user
    username = Column(String(50), unique=True)# Apelido ou nome simplificado, Nickname or simplified name
    birthdate = Column(String(10))# Data de nascimento no formato YYYY-MM-DD, Birthdate in the format YYYY-MM-DD
    job_title = Column(String(100))# Cargo ou título do trabalho, Job title
    favorite_music_genre_1 = Column(String(100))# Gênero musical favorito 1, Favorite music genre 1
    favorite_music_genre_2 = Column(String(100))# Gênero musical favorito 2, Favorite music genre 2
    favorite_music_genre_3 = Column(String(100))# Gênero musical favorito 3, Favorite music genre 3

    password = Column(String(255))# Senha do usuário, User password
    email = Column(String(100))# Email do usuário, User email
    numberphone = Column(String(15))# Número de telefone do usuário, User phone number
    cpf = Column(String(14), unique=True)# CPF do usuário, User CPF
    address = Column(String(200))# Endereço do usuário, User address


    def __repr__(self):
        return f""


class DatabaseHandler:
    """
    Handler do Banco de dados, Database Handler
        Responsável por interagir com o banco de dados, Responsible for interacting with the database
    
    Atributos, Attributes:
        session: Sessão do banco de dados, Database session
    
    funções, functions:
        create_user: Cria um novo usuário no banco de dados, Creates a new user in the database
        update_user: Atualiza os dados de um usuário existente, Updates an existing user's dat
    """
    def __init__(self):
        self.session = SessionLocal()# Cria uma sessão do banco de dados, Creates a database session

    def create_user(self, **user_data):
        try:
            new_user = DataFormulation(**user_data)# Cria uma nova instância do usuário, Creates a new user instance
            self.session.add(new_user)# Adiciona o novo usuário à sessão, Adds the new user to the session
            self.session.commit()# Confirma a transação, Commits the transaction

        except SQLAlchemyError as e:
            self.session.rollback()# Reverte a transação em caso de erro, Rolls back the transaction in case of error
            print("error occurred:", e) # não ficará aqui por muito tempo, quero usar logging, I won't stay here for long, I want to use logging,
            pass

    def update_user(self, user_id, **updated_data):# Atualiza os dados de um usuário existente, Updates an existing user's data
        try:
            user = self.session.query(DataFormulation).filter(DataFormulation.id == user_id).first()# Busca o usuário pelo ID, Fetches the user by ID
            if user:
                for key, value in updated_data.items():
                    setattr(user, key, value)# Atualiza os atributos do usuário, Updates the user's attributes
                self.session.commit()   # Confirma a transação, Commits the transaction
        except SQLAlchemyError as e:
            self.session.rollback()# esse ja foi explicado acima, this has already been explained above
            print("error occurred:", e)# e este também, and this one too
            pass


class APIHandler:
    """
    Handler da API, API Handler
        Responsável por interagir com a lógica da API, Responsible for interacting with the API logic
    
    funções, functions:
        create_user_api: Cria um novo usuário via API, Creates a new user via API
        update_user_api: Atualiza os dados de um usuário existente via API, Updates an existing user's data via API
        auxiliary_method: Método auxiliar para obter todos os usuários, Auxiliary method to get all users
    """
    def __init__(self):
        self.db_handler = DatabaseHandler() # Instancia o handler do banco de dados, Instantiates the database handler

    def create_user_api(self, **user_data):
        """
        Estrutura do user_data, Structure of user_data:
            name: Nome real do usuário, Real Name of the user
            username: Apelido ou nome simplificado, Nickname or simplified name
            birthdate: Data de nascimento no formato YYYY-MM-DD, Birthdate in the format YYYY-MM-DD
            job_title: Cargo ou título do trabalho, Job title
            favorite_music_genre_1: Gênero musical favorito 1, Favorite music genre 1
            favorite_music_genre_2: Gênero musical favorito 2, Favorite music genre 2
            favorite_music_genre_3: Gênero musical favorito 3, Favorite music genre 3
            password: Senha do usuário, User password
            email: Email do usuário, User email
            numberphone: Número de telefone do usuário, User phone number
            cpf: CPF do usuário, User CPF
            address: Endereço do usuário, User address
        """
        self.db_handler.create_user(**user_data)# Cria um novo usuário via API, Creates a new user via API


    def update_user_api(self, user_id, **updated_data):
        """
        Estrutura do updated_data, Structure of updated_data:
            name: Nome real do usuário, Real Name of the user
            username: Apelido ou nome simplificado, Nickname or simplified name
            birthdate: Data de nascimento no formato YYYY-MM-DD, Birthdate in the format YYYY-MM-DD
            job_title: Cargo ou título do trabalho, Job title
            favorite_music_genre_1: Gênero musical favorito 1, Favorite music genre 1
            favorite_music_genre_2: Gênero musical favorito 2, Favorite music genre 2
            favorite_music_genre_3: Gênero musical favorito 3, Favorite music genre 3
            email: Email do usuário, User email
            numberphone: Número de telefone do usuário, User phone number
            cpf: CPF do usuário, User CPF
            address: Endereço do usuário, User address
        """
        self.db_handler.update_user(user_id, **updated_data)# Atualiza os dados de um usuário existente via API, Updates an existing user's data via API
        
    def auxiliary_method(self):# provavelmente vou mudar o nome disso, I will probably change the name of this
        """
        Não é bem um auxiliar, It is not really auxiliary
            Método para obter todos os usuários do banco de dados, Method to get all users from the database
            Retorna uma lista de dicionários representando os usuários, Returns a list of dictionaries

        OBS(Fiz para evitar o uso direto como banco de dados na rota /admin, Note (I made it to avoid direct use as a database in the /admin route
            o que poderia causar problemas de sessão): which could cause session problems) Não tenho certeza rsrs, I'm not sure lol

        """
        session = SessionLocal() # Você ja pode imaginar o que isso faz (ja foi explicado), You can already imagine what this does (it has already been explained)

        try:
            users = session.query(DataFormulation).all()# Busca todos os usuários no banco de dados, Fetches all users from the database

            users_list = [ #Não precisa de explicação, No explanation needed
                {
                "id": user.id,
                "name": user.name,
                "username": user.username,
                "birthdate": user.birthdate,
                "job_title": user.job_title,
                "favorite_music_genre_1": user.favorite_music_genre_1,
                "favorite_music_genre_2": user.favorite_music_genre_2,
                "favorite_music_genre_3": user.favorite_music_genre_3,
                "email": user.email,
                "numberphone": user.numberphone,
                "cpf": user.cpf,
                "address": user.address,
                "password": user.password,
                } for user in users]
            return users_list
        finally:
            session.close()