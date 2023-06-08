from django.shortcuts import render
import json

def index(request):

    data = {
        "map_data" : {
            "0":{
                "place": "조치원역",
                "coord": {
                    "x" : 36.601659208879646,
                    "y" : 127.29777601594054
                }
            },
            "1":{
                "place": "그대랑 닭갈비",
                "coord": {
                    "x" : 36.602816,
                    "y" : 127.298170
                }
            },
            "2":{
                "place": "수구레국밥",
                "coord": {
                    "x" : 36.600082,
                    "y" : 127.297920
                }
            }
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
            }
        },

        "map_key": "890eb7fd7b55736becc3388f215623f7"
    }

    return render(request, 'kakaomap_app/json_func.html', {'json_data':json_data})



def kakaomap_1st(request):
    data = {
        "map_data" : {
            "0":{
                "place": "조치원역",
                "coord": {
                    "x" : 36.601659208879646,
                    "y" : 127.29777601594054
                }
            },
            "1":{
                "place": "그대랑 닭갈비",
                "coord": {
                    "x" : 36.602816,
                    "y" : 127.298170
                }
            },
            "2":{
                "place": "수구레국밥",
                "coord": {
                    "x" : 36.600082,
                    "y" : 127.297920
                }
            }
        },

        "map_key": "890eb7fd7b55736becc3388f215623f7"
    }

    json_data = json.dumps(data)

    return render(request, 'kakaomap_app/kakaomap_1st.html',{"json_data": json_data})