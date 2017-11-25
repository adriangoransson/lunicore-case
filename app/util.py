# Helper for grabbing one item in a list where id matches
def get(id, list):
    return next(filter(lambda item: item['id'] == id, list), None)
