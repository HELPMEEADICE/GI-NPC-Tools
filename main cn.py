import os,webbrowser,socket
from msvcrt import getch as anykey
from time import sleep

title = "原神直连IP修改器 By:HELPMEEADICE"
command = f"title {title}"
os.system(command)
os.system('cls')

print(f"1.修改IP\n2.初始化配置\n3.真端状态检测\n4.Grasscutter状态检测\n5.补丁下载\n6.作者信息")
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
    with open('ip.ini', 'r') as ip:
        ip = ip.read()
        ip = str(ip)
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
    with open('ip.ini', 'r') as ip:
        ip = ip.read()
        ip = str(ip)
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
    os.system('cls')
    webbrowser.open('https://www.youtube.com/channel/UC6LmkBLElnPLid8GdHZrnRQ')
else:
    print("你输入的不是有效的数字")
    exit()