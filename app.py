from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('test.html', questions=get_questions())


def get_questions():
    questions = ("Стоит богатый дом и бедный. Они горят. Какой дом будет тушить полиция?",
                 "Как человеку не спать 8 дней?",
                 "Вы заходите в тёмную кухню. В ней есть свеча, керосиновая лампа и газовая плита. Что вы зажжёте в "
                 "первую очередь?",
                 "Сидит девушка, а вы не можете сесть на её место, даже если она встанет и уйдёт. Где она сидит?",
                 "К реке подходят два человека. У берега лодка, которая может выдержать только одного. Оба человека "
                 "переправились на противоположный берег. Как?",
                 "Два отца, два сына нашли три апельсина и разделили их. Каждому досталось по целому апельсину. Как "
                 "такое может быть?",
                 "Полтора судака стоят полтора рубля. Сколько стоят 13 судаков?",
                 "На столе лежат две монеты, в сумме они дают 3 рубля. Одна из них — не 1 рубль. Какие это монеты?",
                 "Если 5 кошек ловят 5 мышей за 5 минут, то сколько времени нужно 1 кошке, чтобы поймать 1 мышку?",
                 "Собака была привязана к десятиметровой верёвке, а прошла 300 метров. Как ей это удалось?")
    return questions


def get_expected_answers():
    expected_answers = ("Полиция пожары не тушит, тушат пожары пожарные",
                        "Спать по ночам",
                        "Спичку",
                        "Она сидит у вас на коленях",
                        "Они были на разных берегах",
                        "Это были дед, отец и сын",
                        "13 рублей",
                        "1 и 2 рубля",
                        "5 минут",
                        "Верёвка была ни к чему не привязана")
    return expected_answers


@app.route('/submit', methods=['POST'])
def submit():
    expected_answers = get_expected_answers()
    increment = 100 / len(expected_answers)
    score = 0
    answers = []
    correctness_answers = []

    for i in range(len(expected_answers)):
        answer = request.form.get('%d' % (i + 1))
        is_right_answer = expected_answers[i] == answer

        if is_right_answer:
            score += increment

        correctness_answers.append(is_right_answer)
        answers.append(answer)

    return redirect(url_for('verdict', score=score, answers=answers, correctness_answers=correctness_answers))


@app.route('/verdict')
def verdict():
    score = request.args.get('score')
    answers = request.args.getlist('answers')
    correctness_answers = request.args.getlist('correctness_answers')
    correctness_answers = [None if x == 'False' else x for x in correctness_answers]
    return render_template('verdict.html', score=score, answers=answers, correctness_answers=correctness_answers,
                           questions=get_questions(), expected_answers=get_expected_answers())


if __name__ == "__main__":
    app.run(debug=True)
