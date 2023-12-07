from chalice import Chalice
#from chalicelib.claim_files.routes import diamond_files_routes
#from chalicelib.claim_notes.routes import diamond_notes_routes

#from chalicelib.api.fields_types.routes import zatanna_fields_types
from chalicelib.api.brands.routes import atalaya_brands
from chalicelib.api.configurations.routes import atalaya_conf
from chalicelib.api.routings_singles.routes import single_routing
from chalicelib.api.routings_multis.routes import routing_multis
from chalicelib.api.routings_multis_urls.routes import routing_multis_urls
from chalicelib.api.generator.routes import routing_generator
from chalicelib.api.logs.routes import atalaya_logs

app = Chalice(app_name="atalaya_routes")

#app.register_blueprint(diamond_files_routes)
#app.register_blueprint(diamond_notes_routes)
app.register_blueprint(atalaya_brands)
app.register_blueprint(atalaya_conf)
app.register_blueprint(single_routing)
app.register_blueprint(routing_multis)
app.register_blueprint(routing_multis_urls)
app.register_blueprint(routing_generator)
app.register_blueprint(atalaya_logs)

#@app.route("/", methods=["GET"])
#def hello():
#    return {"hello": "world"}


