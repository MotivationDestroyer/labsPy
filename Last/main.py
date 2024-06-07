import coder
import encoder
def start():
    menuSelect=int(input("Нажмите 1 чтобы начать кодировку, нажмите 2 чтобы начать декодирование "))
    if(menuSelect==1):
        coder.codin()
    elif(menuSelect==2):
        encoder.encoding()
    if(int(input("Если хотите продолжить выполнение программы нажмите 1"))==1):
        start()
start()