from flask import (
	make_response,
	redirect,
	render_template,
	send_file,
	url_for,
	Response,
	request,
	abort,
)
from apo import app, login_manager, oauth, oauth_client, db
from . import views_blueprint

@views_blueprint.route("/")
def index():
	return render_template("home.html")

@views_blueprint.route("/login/")
def google():
	oauth.register(
		name="google",
		client_id=app.config["GOOGLE_CLIENT_ID"],
		client_secret=app.config["GOOGLE_CLIENT_SECRET"],
		server_metadata_url=app.config["GOOGLE_DISCOVERY_URL"],
		client_kwargs={"scope": "openid email profile"},
	)

	# Redirect to google_auth function
	redirect_uri = url_for("google_auth", _external=True)
	print(redirect_uri)
	return oauth.google.authorize_redirect(redirect_uri)

@views_blueprint.route("/login/callback")
def google_auth():
	token = oauth.google.authorize_access_token()
	user = oauth.google.parse_id_token(token)
	print(" Google User ", user)
	return redirect("/")
