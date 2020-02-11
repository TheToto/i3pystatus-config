Setup
```
python -m venv
. env/bin/activate
pip install -r requirements.txt
```
In i3 config :
```
bar {
    status_command /path/to/dir/i3pystatus-config/env/bin/python /path/to/dir/i3pystatus-config/bar.py
}
```
Additional steps :
* Fix `rfkill_name` in `bar.py` for rfkill module :
  Execute `rfkill` and choose a `DEVICE` for wifi and bluetooth

Other programs needed :
* redshift
* light
* rfkill (with user in rfkill group)
* xautolock (already configured)
