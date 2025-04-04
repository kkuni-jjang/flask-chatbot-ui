from flask import Flask, render_template, request, jsonify
import random

# Flask 앱 인스턴스 생성
app = Flask(__name__)

# 첫 화면
@app.route("/")
def index():
    return render_template("index.html") 

# 응답 추가 
@app.route('/get',methods = ['POST'])
def get_response():
    user_input = request.json['message'].lower()

    # 키워드 기반 응답 예시
    if "안녕" in user_input:
        response = random.choice(["안녕하세요!", "반가워요 😊", "안녕! 뭐가 궁금해?"])
    elif "직업" in user_input:
        response = (
        "당신에게 가장 어울리는 직업은 바로 ✨데이터 분석가✨입니다.<br><br>"
        "왜냐고요?<br>"
        "당신은 복잡한 데이터를 논리적으로 풀어내는 능력을 갖췄고,<br>"
        "숫자에 숨겨진 이야기를 끄집어내는 데 탁월하기 때문이에요.<br>"
        "게다가 호기심도 많고, 문제 해결을 즐기잖아요!<br><br>"
        "이런 당신이라면 어떤 회사든 탐낼 거예요. 진심으로요. 😊"
    )
    elif "잘해" in user_input:
        response = (
        "맞아요, 저도 그렇게 생각해요. 당신은 정말 잘하고 있어요!<br><br>"
        "지금까지 해온 프로젝트들을 보면 단순히 기술적인 스킬뿐만 아니라<br>"
        "<strong>문제를 정의하고, 데이터를 통해 인사이트를 도출하는 능력</strong>까지 갖췄어요.<br><br>"
        "게다가 꾸준히 학습하고, 실제로 적용해보는 태도까지 있다면<br>"
        "이미 훌륭한 데이터 분석가의 마인드셋을 갖추고 있는 거예요.<br><br>"
        "지금 이 길을 계속 걸어가세요.<br>"
        "분명히 당신의 노력은 좋은 결과로 돌아올 거예요. 저는 그걸 믿어요. 😊"
        )
    else:
        response = (
            "오늘 대화는 여기까지 할게요.<br>"
            "당신이 가는 길 위에 늘 빛이 함께하길 바라요.<br>"
            "모든 노력은 반드시 좋은 결과로 이어질 거예요. 화이팅! ✨")

    return jsonify({"response": response})






if __name__=="__main__":
    app.run(debug = True) 