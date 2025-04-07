### **Minimalistyczny Guide: Import Backupu MySQL na Linux**  

**1. Wgraj backup na serwer**  
```bash  
scp backup.sql user@server_ip:/tmp/  
```  

**2. Połącz się z serwerem**  
```bash  
ssh user@server_ip  
```  

**3. Importuj do istniejącej bazy**  
```bash  
mysql -u root -p nazwa_bazy < /tmp/backup.sql  
```  

**4. Sprawdź dane**  
```bash  
mysql -u root -p -e "USE nazwa_bazy; SHOW TABLES;"  
```  

**Jeśli błąd:**  
```bash  
mysql -u root -p nazwa_bazy < backup.sql 2> errors.txt  
```  

✅ **Gotowe!** Baza zaimportowana.  

*(Zastąp `nazwa_bazy`, `user`, `server_ip` swoimi danymi)* 🚀