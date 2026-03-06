from flask import Flask, render_template, request
from lotto import generate_games

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    game_count = int(request.form["game_count"])
    games = generate_games(game_count)

    # 5게임씩 묶기
    grouped_games = [
        games[i:i+5] for i in range(0, len(games), 5)
    ]

    return render_template(
        "result.html",
        game_count=game_count,
        grouped_games=grouped_games
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
