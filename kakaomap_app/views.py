from django.shortcuts import render

def json(request):

    json_data = {
        "Category": "Fisrt",
        "Writer": "수니니",
        "Place": "홍카페",
        "Coord": "36.6138938, 127.2896801",
        "Tag": "냠냠굿, 치즈케이크와 와플, 봄날에 카페",
        "Q1": "홍익대학교를 다니면서 과제할 카페를 찾으면서 알게 됐어요",
        "Q2": "봄에 남자친구랑 함께요.",
        "Q3": "거기 치즈케이크랑 와플을 먹고싶어용",
        "Q4": "치즈케이크랑 와플 먹기요"
    }

    return render(request, 'kakaomap_app/json.html', {'json_data':json_data})

def index(request):

    return render(request, 'kakaomap_app/index.html')