import os,webbrowser,socket,requests,zipfile
from msvcrt import getch as anykey
from time import sleep
from tqdm import tqdm
from shutil import rmtree

title = "原神直连IP修改器 By:HELPMEEADICE"
command = f"title {title}"
os.system(command)
os.system('cls')

version = "Unknown"
def checkGameVer():
    file_path1 = './GenshinImpact.exe'
    file_path2 = './YuanShen.exe'
    global version
    if os.path.exists(file_path1):
        version = "Global"
    elif os.path.exists(file_path2):
        version = "China"
    else:
        version = "Unknown"

checkGameVer()
print(f"1.修改IP\n2.初始化配置\n3.真端状态检测\n4.Grasscutter状态检测\n5.补丁下载\n6.自动下载+配置游戏\n7.清除Electron缓存\n10.作者信息\n0.退出")
number = input("请输入数字:")
def change_ip():
    os.system('cls')
    newip = input("请输入新的IP:")
    try:
        with open('ip.ini', 'r') as ip:
            oldip = ip.read()
            oldip = str(oldip)
    except:
        print("您尚未进行初始化配置！")
        print("5秒后为您跳转至初始化！")
        sleep(5)
        initialization()

    with open('ip.ini', 'w') as f:
        f.write(newip)

    with open('mhypbase.ini', 'r') as f:
        content = f.read()

    new_content = content.replace(oldip, newip)

    with open('mhypbase.ini', 'w') as f:
        f.write(new_content)

    print("修改完毕，按下任意键退出...")
    anykey()
def initialization():
    os.system('cls')
    ip = input("请输入IP:")
    try:
        with open("mhypbase.ini", "r") as f:
            content = f.read()
    except:
        print("您没有安装mhypbase补丁！")
        print("五秒后打开下载界面！")
        sleep(5)
        webbrowser.open('https://mirror.cccpserver.cf/ADrive%20%231/%E8%BD%AF%E4%BB%B6/%E6%B8%B8%E6%88%8F/%E7%B1%B3%E5%93%88%E6%B8%B8/woc%EF%BC%81%E5%8E%9F%EF%BC%81/%E7%A7%81%E6%9C%8D%E6%96%87%E4%BB%B6/mhypbase')
        exit()

    with open("ip.ini", "w") as f:
        f.write(ip)  # 写入新的内容
    # 将需要替换的字符串替换为新的字符串
    old_str = '; ConfigChannel = {"ChannelName":"OfflineWin","PreDefines":"GAIA_ADDON_TOOLS;GAIA_MULTI_TERRAINS;CTS_GAIA_RELOCATE;HOTFIX_ENABLE;UNITY_RELEASE_BUILD;AMPLIFY_SHADER_EDITOR;ODIN_INSPECTOR;ODIN_INSPECTOR_3;UNITY_POST_PROCESSING_STACK_V2;PROBUILDER_FBX_ENABLED","DispatchConfigs":[{"DispatchUrls":["http://example.com/query_region_list"]}],"BaseTextLang":"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15","BaseAudioLang":"Chinese,English(US),Korean,Japanese"}'
    new_str = 'ConfigChannel = {"ChannelName":"OSRELWin","PreDefines":"GAIA_ADDON_TOOLS;GAIA_MULTI_TERRAINS;CTS_GAIA_RELOCATE;HOTFIX_ENABLE;UNITY_RELEASE_BUILD;AMPLIFY_SHADER_EDITOR;ODIN_INSPECTOR;ODIN_INSPECTOR_3;UNITY_POST_PROCESSING_STACK_V2;PROBUILDER_FBX_ENABLED","DispatchConfigs":[{"DispatchUrls":["http://127.0.0.1:2888/query_region_list"]}],"BaseTextLang":"1,2,3,4,5,6,7,8,9,10,11,12,13,14,15","BaseAudioLang":"Chinese,English(US),Korean,Japanese"}'

    content = content.replace(old_str, new_str)

    # 将替换后的字符串写入到原始文件中或写入到新的文件中
    with open("mhypbase.ini", "w") as f:
        f.write(content)
    #重复步骤
    with open("mhypbase.ini", "r") as f:
        content = f.read()

    old_str = '; ConfigBaseUrl = http://example.com'
    new_str = 'ConfigBaseUrl = http://127.0.0.1:2888'

    content = content.replace(old_str, new_str)

    with open("mhypbase.ini", "w") as f:
        f.write(content)

    #替换IP
    with open("mhypbase.ini", "r") as f:
        content = f.read()

    old_str = '127.0.0.1:2888'
    new_str = ip

    content = content.replace(old_str, new_str)

    with open("mhypbase.ini", "w") as f:
        f.write(content)

    print("初始化完毕，按下任意键退出...")
    anykey()
def tcpcheck():
    try:
        with open('ip.ini', 'r') as ip:
            ip = ip.read()
            ip = str(ip)
    except:
        ip = input("请输入IP:")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((ip, 20071))
        print("服务端已启动！")
        print("按下任意键退出...")
        anykey()
    except:
        print("服务端未完全启动或未启动")
        print("按下任意键退出...")
        anykey()
    finally:
        s.close()
def gccheck():
    try:
        with open('ip.ini', 'r') as ip:
            ip = ip.read()
            ip = str(ip)
    except:
        ip = input("请输入IP:")

    port = input("请输入端口：")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((ip, port))
        print("服务端已启动！")
        print("按下任意键退出...")
        anykey()
    except:
        print("服务端未启动")
        print("按下任意键退出...")
        anykey()
    finally:
        s.close()
def cleanTemp():
    os.system('cls')
    if version == "Global":
        folder_path = './GenshinImpact_Data/webCaches'
    elif version == "China":
        folder_path = './YuanShen_Data/webCaches'
    else:
        print("未知的游戏版本")
        print("按下任意键退出...")
        anykey()
    # 判断文件夹是否存在
    if os.path.exists(folder_path):
        # 删除文件夹及其内容
        rmtree(folder_path)
        print('Electron缓存已清除')
        print("按下任意键退出...")
        anykey()
    else:
        print('Electron缓存不存在')
        print("按下任意键退出...")
        anykey()


#一键安装
url = "https://autopatchhk.yuanshen.com/client_app/download/pc_zip/20221024103618_h2e3o3zijYKEqHnQ/GenshinImpact_3.2.0.zip"
filename = "GenshinImpact_3.2.0.zip"
def download(url, filename):
    # 下载文件并显示进度条和下载速度
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=f'Downloading {filename}')
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            progress_bar.update(len(chunk))
            f.write(chunk)
    progress_bar.close()

    # 解压文件并显示解压进度条
    with zipfile.ZipFile(filename, 'r') as zip_file:
        file_list = zip_file.namelist()
        extract_progress = tqdm(total=len(file_list), desc='Extracting', unit='file')
        for file in file_list:
            zip_file.extract(file)
            extract_progress.update(1)
        extract_progress.close()



if number == "1":
    change_ip()
elif number == "2":
    initialization()
elif number == "3":
    tcpcheck()
elif number == "4":
    gccheck()
elif number == "5":
    os.system('cls')
    webbrowser.open('https://mirror.cccpserver.cf/ADrive%20%231/%E8%BD%AF%E4%BB%B6/%E6%B8%B8%E6%88%8F/%E7%B1%B3%E5%93%88%E6%B8%B8/woc%EF%BC%81%E5%8E%9F%EF%BC%81/%E7%A7%81%E6%9C%8D%E6%96%87%E4%BB%B6/mhypbase')
elif number == "6":
    print("仍在开发中...")
    print("按下任意键退出...")
    anykey()
elif number == "10":
    os.system('cls')
    webbrowser.open('https://www.youtube.com/channel/UC6LmkBLElnPLid8GdHZrnRQ')
elif number == "0":
    exit(0)

#彩蛋
elif number == "114514":
    os.system('cls')
    os.system('title 臭死力！')
    print("       　  　▃▆█▇▄▖\n　 　 　 ▟◤▖　　　◥█▎\n   　 ◢◤　 ▐　　　 　▐▉\n　 ▗◤　　　▂　▗▖　　▕█▎\n　◤　▗▅▖◥▄　▀◣　　█▊\n▐　▕▎◥▖◣◤　　　　◢██\n█◣　◥▅█▀　　　　▐██◤\n▐█▙▂　　     　◢██◤\n◥██◣　　　　◢▄◤\n 　　▀██▅▇▀\n  哼哼哼啊啊啊啊啊啊~")
    anykey()


else:
    print("你输入的不是有效的数字")
    print("按下任意键退出...")
    anykey()
