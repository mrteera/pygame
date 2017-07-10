pip3 install cx_Freeze --upgrade
export PYTHONPATH=/usr/local/Cellar/numpy/1.12.1/lib/python3.6/site-packages
python3 setup.py bdist_dmg
# Or Windows
python setup.py bdist_msi
