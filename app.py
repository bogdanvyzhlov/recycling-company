from flask import Flask, render_template
from views.auth import auth_bp
from views.homepage import homepage
from views.admin.admin import admin_bp
from views.default.account import account_bp
from views.worker.worker import worker_bp
from database import database
from service.materials_service import MaterialsService


app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object('config')
database.init_app(app)

app.register_blueprint(homepage, url_prefix='/')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(account_bp, url_prefix='/account')
app.register_blueprint(worker_bp, url_prefix='/worker' )
@app.route('/prices')
def view_current_prices():
    prices = MaterialsService.get_current_prices()
    return render_template("prices.html", prices=prices)

@app.route('/stats')
def view_all_stats():
    stats = MaterialsService.get_stats()
    return render_template("stats.html", stats=stats)

@app.route('/about')
def view_about_us():
    return render_template("about_us.html")

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)


