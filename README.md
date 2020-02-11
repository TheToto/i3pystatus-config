Setup
```
python -m venv
. env/bin/activate
pip install -r requirements.txt
```
In i3 config
```
bar {
    status_command /path/to/dir/i3pystatus-config/env/bin/python /path/to/dir/i3pystatus-config/bar.py
}
```
