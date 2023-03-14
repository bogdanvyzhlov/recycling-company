```
$ python -m venv venv
```
If `python --version` refers to version 2, you must use `python 3.10` or upgrade your python)

```
(Windows CMD) $ .\venv\Scripts\activate.bat
(Linux, macOS) $ ./venv/bin/activate
(Windows PowerShell) $ .\venv\Scripts\Activate.ps1
```

Install dependencies into virtual env
```
$ pip install -r requirements.txt
```

Start Flask service. Navigate your browser to **localhost:5000** where the flask is served.
```
$ flask run

```



