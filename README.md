# -EarlyBirdTicket
我要搶到高鐵票  

django2[文件](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)
### clone下來後 初始步驟記錄
1. 在clone專案後的同一層資料夾新增虛擬環境venv  
````python3 -m venv django_venv````  
資料夾結構：  
\--- EarlyBirdTicket (這是clone下來的專案)  
\--- django_venv (這是我自己取的名字，可自取)  
2. 切換到虛擬環境  
```source django_venv/bin/activate```  
切換到虛擬環境後，terminal都會顯示一行(django_venv)
3. 安裝django  
```pip install django```  
4. 檢查django版本  
```cd EarlyBirdTicket```  
```python -m django --version```
5. cd 到manage.py所在位置啟動localhost  
```python manage.py runserver```  
會跑錯誤告訴你要跑```python manage.py migrate```  
可不管他，等後面的資料表建立完一起跑，如果跑了也沒關係，可以看到/admin  
    > 初始步驟結束後跑 http://127.0.0.1:8000/ 就會出現首頁，django2首頁有可愛火箭
6. 執行```python manage.py migrate```
由於夏天已經先push上去資料庫migration，下migrate之後就可看到資料庫所有的資料表，以及夏天新增的notification表
> 備註：  
> /EarlyBirdTicket/urls.py參考註解可將首頁導到app tickets的首頁  
#####夏天如何建立migration的筆記請參考檔案create_migration.md
