def codin():
    morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ё': '.', 
             'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 
             'п': '.--.', 'р': '.-.', 'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 
             'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '\n',
             '0': '-----', '1': '·----', '2': '··---', '3': '···--', '4': '····-', '5': '·····', '6': '-····', '7': '--···', '8': '---··',
             '9': '----·', ',': '.-.-.-', '.':'.. .. ..', ';':'-.-.-.',':':'---...','?':'..--..','!':'--..--','-':'-...-'}
    print("Нажмите 1 если нужно ввести текст вручную, 2 если нужно счтитать с файла")
    a = int(input())
    result = []
    if(a == 1):
        print("Введите текст\n")
        code = input().lower()                                
        for value in code:               
            result.append(morze[value])  
        print(*result)
    elif(a == 2):
        print("Введите имя файла которое нужно декодировать, файл должен находиться в одной директории с программой")
        FILENAME=input()
        file = open(FILENAME, "r", encoding='utf-8')
        for value in file.read():               
            result.append(morze[value])  
        print(*result)
        print()