import json
import falcon

class ObjRequstClass:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        first_name = req.get_param('first_name', 'Emre')
        last_name = req.get_param('last_name', 'Ozan') 

        upper_firstname = first_name.upper() 
        upper_lastname = last_name.upper() 
        length = len(upper_firstname) + len(upper_lastname)
        
        output = {
            'first_name' : upper_firstname,
            'last_name': upper_lastname,
            'total_length': length
        }
        
        resp.body = json.dumps(output)
        return resp.body

def create_api():
    api = falcon.API(media_type="application/json")
    api.add_route('/hello', ObjRequstClass())
    return api
