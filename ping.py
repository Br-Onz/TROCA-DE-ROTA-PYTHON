import subprocess
import time
import os
import platform


operating_sys = platform.system()
def clearConsole(): return os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    
while True: 
    try:
        on = 0
        off = 0
        clearConsole()
        for ips in range(10):  # ENVIANDO 10 PINGS
            ips = '172.19.2.2'  # 
            ping_command = ['ping', ips, '-n', '1'] if operating_sys == 'Windows' else ['ping', ips, '-c 1']  
            shell_needed = True if operating_sys == 'Windows' else False
            ping_output = subprocess.run(ping_command, shell=shell_needed, stdout=subprocess.PIPE)
            success = ping_output.returncode
            if success == 0: 
                # print(subprocess.run(ping_command))
                on = on+1
                print('>>> '+ips+' ONLINE <<<')
            else:
                off = off+1
                print('>>> '+ips+' OFFLINE')

        if off >= 6:  # CASO A ANTENA PERDA OS 8 PING ENVIADO IRA TROCAR A ROTA PARA VM
            clearConsole()
            print('ANTENA CAIU ')
            print('TROCANDO DE ROTA PARA [ VM ]')
            time.sleep(3)
            for ip in range(19):
                # print('psexec64.exe \\\\172.22.5.', ip+1,' -u administrador -p @dmb4r4t40* -n 1 -i cmd /c route add 172.19.0.0 mask 255.255.0.0 172.22.9.50 metric 80 -p')
                print(ip+1)
                print('ROTAS TROCADAS')
            time.sleep(5)
            teste = 0
            while teste < 1:  # IRA ENTRAR EM LOOP, FICARA VERIFICANDO SE O PING DA ANTENA IRÁ NORMALIZAR
                clearConsole()
                print('VERIFICANDO SE A ANTENA VOLTOU [ ENVIANDO PING ]')
                on = 0
                off = 0
                for ips in range(10):  # ENVIANDO 10 PINGS
                    ips = '172.19.2.2'  # IP ANTENA
                    ping_command = ['ping', ips, '-w', '3'] if operating_sys == 'Windows' else [
                        'ping', ips, '-n 1']  # VAI FICAR MANDANDO PING COM 3 DISPARO
                    shell_needed = True if operating_sys == 'Windows' else False
                    ping_output = subprocess.run(
                        ping_command, shell=shell_needed, stdout=subprocess.PIPE)
                    success = ping_output.returncode
                    if success == 0:
                        on = on+1
                        print('>>> '+ips+' ONLINE <<<')
                    else:
                        off = off+1
                        print('>>> '+ips+' OFFLINE')
                if on == 10:  # SE O PING DA ANTENA NORMALIZAR ELE VAI SAIR DA VM
                    clearConsole()
                    print('ANTENA NORMALIZADA')
                    print('TROCANDO A ROTA PARA ANTENA')
                    for ip in range(19):
                        # print('psexec64.exe \\\\172.22.5.', ip+1,' -u administrador -p @dmb4r4t40* -n 1 -i cmd /c route add 172.19.0.0 mask 255.255.0.0 172.22.9.50 metric 80 -p')
                        print('ROTRAS TROCADAS PARA ANTENA')
                        teste = 1
                    time.sleep(5)
    except:
        print(' ERRO')
        print('REINICIANDO PROCESSO!')
        time.sleep(5)
