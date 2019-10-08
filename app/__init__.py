
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask  import request, jsonify, abort

# local import
from instance.config import app_config


# initialize sql-alchemy
db = SQLAlchemy()


def create_app(config_name):
	from app.models import Bucketlist
	app = FlaskAPI(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db.init_app(app)

	@app.route('/bucketlists/', methods=['POST', 'GET'])
	def beucketlists():
		if request.method == "POST":
			name = str(request.data.get('name',''))
			if name:
				bucketlist = bucketlist(name=name)
				bucketlist.save()
				response = jsonify({
					'id': bucketlist.id,
					'name': bucketlist.name,
					'date_created': bucketlist.date_created,
					'date_modifed': bucketlist.date_modified 
				})
				response.status_code = 201
				return response
		else:
			#GET
			bucketlists = Bucketlist.get_all()
			results = []

			for bucketlist in bucketlists:
					obj = {
						'id': bucketlist.id,
						'name': bucketlist.name,
						'date_created': bucketlist.date_created,
						'date_modified': bucketlist.date_modified
					}
					results.append(obj)
			response = jsonify(results)
			response.status_code = 200
			return response

	@app.route('/bucketlist/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
	def bucketlist_manipulation(id, **kwargs):
    #Retirieve bucket list using its ID
		bucketlist = Bucketlist.query.filter_by(id=id).first()
		
		if not bucketlist:
			abort(404)

		if request.method == 'DELETE':
			bucketlist.delete()
			return {
				f"message": "bucketlist {bucketlist.id} succesfuly deleted"
			}, 200

		elif request.method == 'PUT':
			name = str(request.data.get('name', ''))
			bucketlist.name = name
			bucketlist.save()
			response = jsonify({
				'id': bucketlist.id,
				'name': bucketlist.name,
				'date_created': bucketlist.date_created,
				'date_modified': bucketlist.date_modifie
			})
			response.status_code = 200
			return response

		else:
			#GET
			response = jsonify({
				'id': bucketlist.id,
				'name': bucketlist.name,
				'date_created': bucketlist.date_created,
				'date_modified': bucketlist.date_modified
			})
			response.status_code = 200
			return response			 

	return app		