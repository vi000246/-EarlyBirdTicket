### 以下為夏天如何建立migration的筆記

#### 步驟一：建立app
app名字取```tickets```，此app用來建立```notifications```資料表  
```python manage.py startapp tickets```  
資料夾結構：  
\--- manage.py  
\--- EarlyBirdTicket   
\--- tickets   
建立後要去 \--- EarlyBirdTicket裡面的```setting.py```--```INSTALLED_APPS```新增```'tickets'```，不然會跑錯誤跟你說沒這個app

#### 步驟二：嘗試建立一個view(測試網頁有沒有壞掉)
參考[django2文件建立view跑首頁](https://docs.djangoproject.com/en/2.0/intro/tutorial01/#write-your-first-view)  
本專案直接把\--- EarlyBirdTicket裡面的```urls.py```首頁設成看到Hello, world

#### 步驟三：產生資料庫
本專案僅使用通知表```notification```  
參考[django2文件](https://docs.djangoproject.com/en/2.0/intro/tutorial02/#creating-models)  
1. 先建立tickets app要用的table notification  ```/tickets/models.py```  
資料表的[欄位語法參考](https://docs.djangoproject.com/en/2.0/ref/models/fields/)    
2. 新增tickets app要用的migration ```python manage.py makemigrations tickets```    
自動產生一個根據models.py所寫的資料表的migration 0001_initial.py  
3. 產生資料庫的語法 ```python manage.py migrate```
會幫你辨識要新增 /tickets/migrations/0001，重複跑migrate的話也會自動辨識跑過0001了而忽略
> 意外發現新的資料表名稱其實是叫做 tickets_notification，應該是先依app名稱再底線models.py裡面的名稱