from flask import Flask, request
from routes import register_routes
# from database import init_db

app = Flask(__name__)
register_routes(app)

@app.route('/')
def index():
    return {"Hello":"Flask!"}

@app.route('/api/v1/feeds', methods=['GET']) # REST API: [GET] /api/v1/feeds
def show_all_feeds():
    data = {'result':'success', 'data':{'feed1':'data1', 'feed2':'data2'}}

    return data  # 데이터 타입이 파이썬 Dict인데 자동으로 jsonify

@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    data = {'result':'success', 'data':f'feed ID: {feed_id}'}

    return data

@app.route('/api/v1/feeds', methods=['POST'])
def create_feed():
    email = request.form['email']
    content = request.form['content']
    data = {'result':'success', 'data': {'email':email, 'contet':content}}
    
    return data

if __name__ == "__main__":
    app.run(debug=True)
    # init_db()

