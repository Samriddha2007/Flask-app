from flask import Flask,jsonify,request

app = Flask(__name__)
tasks = [
    {
        'id':1,
        'title':u'Buy Groceries',
        'description': u'Chocolate, Chips, Vegetables, Fruits, bread, biscuit',
        'done':False
    },
    {
        'id':2,
        'title':u'Learn Python',
        'description': u'Use cv2, matplotlib, pandas, time, pyplot',
        'done':False
    },
]
@app.route('/')

def hello_world():
    return 'Hello World!'

@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify(
            {'status':'error',
            'msg':'Please provide data'},400)
    task = {
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',''),
        'done':False
    }
    tasks.append(task)
    return jsonify({'status':'success','msg':'Task added'})
@app.route('/get-data')
def get_task():
    return jsonify({
        'data':tasks
    })
    

if __name__ == '__main__':
    app.run(debug=True)


