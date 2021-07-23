from django.shortcuts import render
from tensorflow.python.keras.models import load_model
import joblib


def result(gender, p):
    if (gender == 0):
        if(p <= 11):
            re = '이정도의 체지방률은 여성보디빌더 체지방률으로 운동으로만 만들어지는 것이 아닌 눈으로 볼때 보이는 근육질의 몸매 입니다. 그렇기 때문에 그냥 일반사람이 운동으로 만들기에는 어려운 정도의 체지방률입니다.'
        elif(p < 15):
            re = '이정도의 체지방률은 피트니스들이 운동으로 만든 몸매이며 체지방률 11퍼센트와 같이 그냥 운동만으로는 달성하기 어렵습니다. 육안으로는 근육이 많이 잡혀 있는듯 보이지만 실제로 옷을 입었을 시에는 맵시가 나며 건강하게 보이는 몸매입니다.'
        elif(p <= 19):
            re = '주로 이정도는 모델들과 연예인들이 유지하는 체지방률 인데요. 보기에 마른듯한 느낌이 드는 몸매이며 몸라인이 매우 예쁘게 느껴지는 몸매입니다.'
        elif(p <= 24):
            re = '이 체지방률은 실제로 봤을 때 가장 예쁘게 보이는 몸매이며 밥도 적당히 먹으면서 운동을 할수 있는 정도이다. 보이기에 가장 이뻐 보이는 체지방률이므로 이정도를 목표로 가지고 운동을 하면 될 것이다.'
        elif(p <= 30):
            re = '이 체지방률은 건강상으로 가장 적당한 정도 이며, 배가 약간 나오면서 접히는 부분이 생기고 통통하다는 말을 자주 듣는 정도의 체지방률이다 필히 운동이 필요하다.'
        else:
            re = '건강과 보이는 상에 모두 문제가 생기는 몸매 이며 식단조절을 하고 꾸준히 운동을 해야 하는 체지방률이다. 건강을 위해 꼭 운동을 시작하여 중간정도의 체지방률을 만들도록 하자.'
        
    else:
        if(p <= 7):
            re = '일반인들이 도전하기는 정말 어려운 정도의 체지방률이며, 피트니스모델 들이 유지하는 정도의 몸매라고 알고 있으면 될 것이다.'
        elif(p <= 12):
            re = '모델들의 몸매이며 체지방률 때문에 말라보이긴 하지만 근육량이 적당히 있으면서 사진찍을때에 딱 이뻐보이는 체지방률이다. '
        elif(p <= 16):
            re = '평균적으로 운동하는 사람들이 만드는 몸매로 식스팩이 살짝 보이면서 적당한 식사와 적당한 운동으로 만들수 있는 몸매이다.'
        elif(p <= 24):
            re = '건장한 정도의 몸매이며 건강상으로는 가장 이상적인 체지방률에 속한다. \n남자의 평균 체지방률로 생각하면 되며, 단 여기에서 살이 찌면 자칫 통통해 보일수 있으니 주의 해야 한다.'
        elif(p <= 30):
            re = '통통해 보이는 체지방률이다.\n육안으로 보이기에도 배도 나오고 몸은 무거워지고 운동을 꼭 시작하여 더이상 뚠뚠해 지는것을 막아야 할정도이다. '
        else:
            re = '뚱뚱해 보이는 몸매이며 가만히 나둘경우 건강상에도 문제가 생길수 있다. \n꼭 식단조절과 꾸준한 운동으로 몸매를 관리하여야 한다.'
    
    return re

def index(request):
    return render(request, 'fatapp/index.html')

def senior(request):
    return render(request, 'fatapp/senior.html')

def seniorBasic(request):
    return render(request, 'fatapp/seniorBasic.html')

def child(request):
    return render(request, 'fatapp/child.html')

def childBasic(request):
    return render(request, 'fatapp/childBasic.html')


def adult(request):
    return render(request, 'fatapp/adult.html')

def adultBasic(request):
    return render(request, 'fatapp/adultBasic.html')
    
def adultSubmit(request):
    model = load_model(r"C:\DevRoot\Dropbox\App20\PyWork\AI_Project\fatpred\fatapp\templates\fatapp\adult_model.h5")
    age = request.GET.get('test_age')
    gender = int(request.GET.get('gender'))
    height = request.GET.get('height')
    weight = request.GET.get('weight')
    core_cm = request.GET.get('core_cm')
    situp = request.GET.get('situp')
    flex = request.GET.get('flex')
    run = request.GET.get('run20')

    adult_scalar = joblib.load(r"C:\DevRoot\Dropbox\App20\PyWork\AI_Project\fatpred\fatapp\templates\fatapp\adult_scaler.pkl")
    test_data = [[age, gender, height, weight, core_cm, run, situp, flex]]
    test_data_scaled = adult_scalar.transform(test_data)
    predict = model.predict(test_data_scaled)

    p = round(predict[0][0],2)

    re = result(gender, p)

    dic = {
        "predict" : p,
        "info"  : re
    }

    return render(request, 'fatapp/adultSubmit.html', dic)

def adultBasicSubmit(request):
    model = load_model(r"C:\DevRoot\Dropbox\App20\PyWork\AI_Project\fatpred\fatapp\templates\fatapp\adult_basic_model.h5")
    age = request.GET.get('test_age')
    gender = int(request.GET.get('gender'))
    height = request.GET.get('height')
    weight = request.GET.get('weight')
    core_cm = request.GET.get('core_cm')
    

    adult_scalar = joblib.load(r"C:\DevRoot\Dropbox\App20\PyWork\AI_Project\fatpred\fatapp\templates\fatapp\adult_basic_scaler.pkl")
    test_data = [[age, gender, height, weight, core_cm]]
    test_data_scaled = adult_scalar.transform(test_data)
    predict = model.predict(test_data_scaled)

    p = round(predict[0][0],2)

    re = result(gender, p)

    dic = {
        "predict" : p,
        "info"  : re
    }

    return render(request, 'fatapp/adultBasicSubmit.html', dic)

def childSubmit(request):
    model = load_model(r"C:\DevRoot\Dropbox\App20\PyWork\AI_Project\fatpred\fatapp\templates\fatapp\youth_model.h5")
    age = request.GET.get('test_age')
    gender = int(request.GET.get('gender'))
    height = request.GET.get('height')
    weight = request.GET.get('weight')
    core_cm = request.GET.get('core_cm')
    run = request.GET.get('run20')
    situp = request.GET.get('situp')
    flex = request.GET.get('flex')

    scalar = joblib.load(r"C:\DevRoot\Dropbox\App20\PyWork\AI_Project\fatpred\fatapp\templates\fatapp\youth_scaler.pkl")
    test_data = [[age, gender, height, weight, core_cm, run, situp, flex]]
    test_data_scaled = scalar.transform(test_data)
    predict = model.predict(test_data_scaled)

    p = round(predict[0][0],2)

    re = result(gender, p)

    dic = {
        "predict" : p,
        "info"  : re
    }

    return render(request, 'fatapp/childSubmit.html', dic)

def childBasicSubmit(request):
    model = load_model(r"C:\DevRoot\Dropbox\App20\PyWork\AI_Project\fatpred\fatapp\templates\fatapp\youth_basic_model.h5")
    age = request.GET.get('test_age')
    gender = int(request.GET.get('gender'))
    height = request.GET.get('height')
    weight = request.GET.get('weight')
    core_cm = request.GET.get('core_cm')

    scalar = joblib.load(r"C:\DevRoot\Dropbox\App20\PyWork\AI_Project\fatpred\fatapp\templates\fatapp\youth_basic_scaler.pkl")
    test_data = [[age, gender, height, weight, core_cm]]
    test_data_scaled = scalar.transform(test_data)
    predict = model.predict(test_data_scaled)

    p = round(predict[0][0],2)

    re = result(gender, p)

    dic = {
        "predict" : p,
        "info"  : re
    }

    return render(request, 'fatapp/childBasicSubmit.html', dic)

def seniorSubmit(request):
    model = load_model(r"C:\DevRoot\Dropbox\App20\PyWork\AI_Project\fatpred\fatapp\templates\fatapp\senior_model.h5")
    age = request.GET.get('test_age')
    gender = int(request.GET.get('gender'))
    height = request.GET.get('height')
    weight = request.GET.get('weight')
    core_cm = request.GET.get('core_cm')
    walk2m = request.GET.get('walk2m')
    chairup = request.GET.get('chairup')
    flex = request.GET.get('flex')

    scalar = joblib.load(r"C:\DevRoot\Dropbox\App20\PyWork\AI_Project\fatpred\fatapp\templates\fatapp\senior_scaler.pkl")
    test_data = [[age, gender, height, weight, core_cm, walk2m, chairup, flex]]
    test_data_scaled = scalar.transform(test_data)
    predict = model.predict(test_data_scaled)

    p = round(predict[0][0],2)

    re = result(gender, p)

    dic = {
        "predict" : p,
        "info"  : re
    }
    
    return render(request, 'fatapp/seniorSubmit.html', dic)

def seniorBasicSubmit(request):
    model = load_model(r"C:\DevRoot\Dropbox\App20\PyWork\AI_Project\fatpred\fatapp\templates\fatapp\senior_basic_model.h5")
    age = request.GET.get('test_age')
    gender = int(request.GET.get('gender'))
    height = request.GET.get('height')
    weight = request.GET.get('weight')
    core_cm = request.GET.get('core_cm')

    scalar = joblib.load(r"C:\DevRoot\Dropbox\App20\PyWork\AI_Project\fatpred\fatapp\templates\fatapp\senior_basic_scaler.pkl")
    test_data = [[age, gender, height, weight, core_cm]]
    test_data_scaled = scalar.transform(test_data)
    predict = model.predict(test_data_scaled)

    p = round(predict[0][0],2)

    re = result(gender, p)

    dic = {
        "predict" : p,
        "info"  : re
    }
    
    return render(request, 'fatapp/seniorBasicSubmit.html', dic)