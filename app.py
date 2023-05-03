from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/submit', methods=['POST'])
def submit():
    expected_answers = {'1': "Полиция пожары не тушит, тушат пожары пожарные",
                        '2': "Спать по ночам",
                        '3': "Спичку",
                        '4': "Она сидит у вас на коленях",
                        '5': "Они были на разных берегах",
                        '6': "Это были дед, отец и сын",
                        '7': "13 рублей",
                        '8': "1 и 2 рубля",
                        '9': "5 минут",
                        '10': "Верёвка была ни к чему не привязана"}

    increment = 100 / len(expected_answers)
    score = 0

    for key in expected_answers.keys():
        if expected_answers[key] == request.form.get(key):
            score += increment

    return redirect(url_for('verdict', score=score))


@app.route('/verdict/<int:score>')
def verdict(score):
    return render_template('verdict.html', score=score)


if __name__ == "__main__":
    app.run(debug=True)
