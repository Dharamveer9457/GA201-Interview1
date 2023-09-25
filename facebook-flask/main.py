from flask import Flask, jsonify, request

app = Flask(__name__)

posts = []
post_id_count = 1

app.route("/createpost", methods = ['POST'])
def create_post():
    global post_id_count

    data = request.get_json()
    username = data.get('username')
    caption = data.get('caption')

    if username and caption:
        new_post = {
            'id': post_id_count,
            'username':username,
            'caption':caption
        }
        posts.append(new_post)
        post_id_count+=1
        return jsonify({'msg':"Post created"})
    else:
        return jsonify({'error'})
    
app.route('/getpost', methods = ['GET', 'POST'])
def get_post():
    return jsonify({"posts":posts})

app.route('/deletepost/<int:post_id>', methods = ['DELETE'])
def delete_post(post_id):
    global posts
    post_to_delete = None

    for post in posts:
        if post['id']==post_id:
            post_to_delete = post
            break

        if post_to_delete:
            posts.remove(post_to_delete)
            return jsonify({'msg':"Post deleted"})
        else:
            return jsonify({'error'})
        
if __name__ == '__main__':
    app.run(debug=True)