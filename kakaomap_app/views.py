from django.shortcuts import render
import json

def index(request):

    data = {
        "map_data" : {
            "category": "Fisrt",
            "writer": "수니니",
            "place": "홍카페",
            "coord": {
                "x" : 36.601659208879646,
                "y" : 127.29777601594054
            },
            "tag": "냠냠굿, 치즈케이크와 와플, 봄날에 카페",
            "q1": "홍익대학교를 다니면서 과제할 카페를 찾으면서 알게 됐어요",
            "q2": "봄에 남자친구랑 함께요.",
            "q3": "거기 치즈케이크랑 와플을 먹고싶어용",
            "q4": "치즈케이크랑 와플 먹기요"
        },

        "map_key": "890eb7fd7b55736becc3388f215623f7"
    }

    json_data = json.dumps(data)

    return render(request, 'kakaomap_app/index.html', {"json_data": json_data})

def json_func(request):

    json_data = {
        "map_data" : {
            "category": "Fisrt",
            "writer": "수니니",
            "place": "홍카페",
            "coord": {
                "x" : 36.601659208879646,
                "y" : 127.29777601594054
            },
            "tag": "냠냠굿, 치즈케이크와 와플, 봄날에 카페",
            "q1": "홍익대학교를 다니면서 과제할 카페를 찾으면서 알게 됐어요",
            "q2": "봄에 남자친구랑 함께요.",
            "q3": "거기 치즈케이크랑 와플을 먹고싶어용",
            "q4": "치즈케이크랑 와플 먹기요"
        },

        "map_key": "890eb7fd7b55736becc3388f215623f7"
    }

    return render(request, 'kakaomap_app/json_func.html', {'json_data':json_data})



def kakaomap_1st(request):

    return render(request, 'kakaomap_app/kakaomap_1st.html')