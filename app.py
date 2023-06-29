from flask import Flask, render_template, jsonify           # import Flask object and jsonify function


app = Flask(__name__)                       # use Flask object to create an app object


@app.route('/')                             # setup route as '/'
def index():
    return render_template('Index.html')


@app.route('/fizzbuzz', methods=['GET'])    # setup route as '/fizzbuzz'
def fizz_buzz():  # put application's code here
    ans = []
    for i in range(1, 101):                 # iterate all integers from 1 to 100
        if (i % 3 == 0) and (i % 5 == 0):
            ans.append('FizzBuzz')
        elif i % 3 == 0:
            ans.append('Fizz')
        elif i % 5 == 0:
            ans.append('Buzz')
        else:
            ans.append(i)
    return jsonify(ans)                     # transfer the list to Json format and return it


if __name__ == '__main__':
    app.run()
