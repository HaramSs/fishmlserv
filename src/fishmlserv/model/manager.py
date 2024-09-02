import os


def get_model_path():

    # 현재 파일의 절대 경로를 가져온다
    my_path = __file__
    #print(my_path)
    #/home/haram/code/fishmlserv/src/fishmlserv/model/manager.py
    
    # 현재 파일의 디렉토리를 얻는다
    dir_name = os.path.dirname(my_path)
    #/home/haram/code/fishmlserv/src/fishmlserv/model
    
    # 'model.pkl'의 경로를 조합한다
    #model_path = dir_name + "/" + "model.pkl"
    model_path = os.path.join(dir_name, "model.pkl")
    
    # 조합된 경로를 리턴한다
    return model_path
    # return "living for today"
    
    #사용 fastapi main.py 에서 아래와 같이 사용
    #from fishmlserv.model.manager import get_model_path
    

