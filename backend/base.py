import json
from flask import Flask, request, jsonify
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required, JWTManager
from flask import request
from werkzeug.security import check_password_hash,generate_password_hash
from User import User
from db import initialize_db
api = Flask(__name__)
initialize_db()
api.config["JWT_SECRET_KEY"] = "please-remember-to-change-me"
api.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(api)

@api.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_token"] = access_token 
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response


@api.route('/signup', methods=["POST"])
def signup():
    email = request.json.get("email", None)
    password = request.json.get("password", None)    
    user = User.objects(email=email).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=email)
        response = {"access_token": access_token}
        return response
    else:
        return {"msg": "Wrong email or password"}, 401
    


@api.route('/register', methods=['POST'])
def register():
    # Obtenir les données du formulaire d'inscription
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    # Vérifier si l'utilisateur existe déjà
    existing_user = User.objects(email=email).first()
    if existing_user:
        return jsonify({'message': 'L\'utilisateur existe déjà'}), 400

    # Hasher le mot de passe avant de le stocker dans la base de données
    hashed_password = generate_password_hash(password)

    # Créer un nouvel utilisateur et l'enregistrer dans la base de données
    new_user = User(email=email, password=hashed_password)
    if new_user:
        new_user.save()
        return jsonify({'message':'utulisateur crée'}),201

    return jsonify({'message': 'Utilisateur enregistré avec succès'}), 201




@api.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

@api.route('/profile')
@jwt_required()
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }
    return response_body