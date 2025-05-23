from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # debug=True 表示啟用自動重新載入與錯誤訊息顯示
    app.run(debug=True)
