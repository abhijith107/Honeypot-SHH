# ssh_honeypot.py

import socket

def main():
    
    ssh_port = 2222  

    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        s.bind(('0.0.0.0', ssh_port))
        
       
        s.listen()

        print(f"SSH honeypot listening on port {ssh_port}")

        while True:
            
            conn, addr = s.accept()
            print(f"Connection from {addr}")

           
            with open("ssh_log.txt", "a") as logfile:
                logfile.write(f"Connection from {addr}\n")

           
            conn.close()

if __name__ == "__main__":
    main()
