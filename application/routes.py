from flask import json, jsonify, render_template, redirect , request
from werkzeug.security import generate_password_hash, check_password_hash
from .handlers import APIHandler, DatabaseHandler
import json


#Essa vai dar trabalho de explicar, mas vamos la, This will take some explaining, but let's go.

# Inicializa as rotas do aplicativo Flask (lá do __init__, lembra?), Initializes the routes of the Flask application(from __init__, remember?)

def init_routes(app):
    @app.route('/')# Rota principal, simples e direta, Main route, simple and straightforward
    def index():
    
        return render_template("index.html")
    
    @app.route("/singnin", methods=["POST","GET"])# provavelmente vou mudar o nome disso, I will probably change the name of this
    def singnin():
        if request.method == 'POST': # Se for um POST, processa o formulário, If it's a POST, process the form
            data = { # não preciso explicar isso, I don't need to explain this
                "name": request.form.get("name"),
                "username": request.form.get("username"),
                "password": generate_password_hash(request.form.get("password")),
                "email": request.form.get("email"),
                "birthdate": request.form.get("birthdate"),
                "job_title": request.form.get("job_title"),
                "favorite_music_genre_1": request.form.get("favorite_music_genre_1"),
                "favorite_music_genre_2": request.form.get("favorite_music_genre_2"),
                "favorite_music_genre_3": request.form.get("favorite_music_genre_3"),
                "numberphone": request.form.get("numberphone"),
                "cpf": request.form.get("cpf"),
                "address": request.form.get("address"),
            }
            api = APIHandler() # Instancia o handler da API, classe lá do Handlers, lembra? , Instantiates the API handler, the class from Handlers, remember?
            api.create_user_api(**data)# la no handlers você verá como deve ser a estrutura do data, there in handlers you will see how the structure of data should be
        return render_template("singnin.html")

    @app.route("/admin", methods=["GET"])
    def adminpage():# Rota administrativa para visualizar usuários, Administrative route to view users
        api = APIHandler() #Voce ja sabe o que isso faz, You already know what this does
        users_list = api.auxiliary_method() # Pega a lista de usuários (vou mudar o nome disso), Gets the list of users(I will change the name of this)
        users_list = jsonify(users_list)# transforma em json (vou tentar otimizar isso ou retirar), converts to json(I will try to optimize this or remove it)
        in_dict = json.loads(users_list.get_data())# transforma de json para dicionario (vou tentar otimizar isso ou retirar), converts from json to dictionary(I will try to optimize this or remove it)
        
        return render_template("admin.html", users = in_dict)# Renderiza a página admin com a lista de usuários, Renders the admin page with the list of users
    
    @app.route("/update_user/<int:user_id>", methods=["GET", "POST"])
    def update_user(user_id):# o nome já diz tudo, The name says it all
        api = APIHandler()# voce ja esta cansado de saber o que isso faz, You are already tired of knowing what this does

        if request.method == "POST":
            updated_data = { # nem vou explicar isso, I won't even explain this
                "name": request.form.get("name"),
                "username": request.form.get("username"),
                "email": request.form.get("email"),
                "birthdate": request.form.get("birthdate"),
                "job_title": request.form.get("job_title"),
                "favorite_music_genre_1": request.form.get("favorite_music_genre_1"),
                "favorite_music_genre_2": request.form.get("favorite_music_genre_2"),
                "favorite_music_genre_3": request.form.get("favorite_music_genre_3"),
                "numberphone": request.form.get("numberphone"),
                "cpf": request.form.get("cpf"),
                "address": request.form.get("address"),
            }
            api.update_user_api(user_id, **updated_data)
            return redirect("/admin")  # redireciona após atualizar

        # Se for GET, mostra a página de edição
        user_list = api.auxiliary_method()
        selected_user = next((user for user in user_list if user["id"] == user_id), None)

        if not selected_user:
            return jsonify({"error": "User not found"}), 404

        return render_template("update_user.html", user=selected_user)# vai lá pro system agora, go to system now,
