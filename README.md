# xbox_nxt
Python script to control NXT Motors using XBOX 360/One Controller

installation instructions:

1. install python 3.x

2. install required libs:
pip install --upgrade --pre nxt-python
pip install common

3. manually install pybluez from here:
  https://github.com/pybluez/pybluez

- extract pybluez-master.zip
- cmd / cd into folder and run "python setup.py install"
- if it gives an error you need to install vcpp build tools from here
  https://visualstudio.microsoft.com/visual-cpp-build-tools/

4. make sure the brick is paired (test connection with bricxcc if you want) 
- for this you need to have the nxt drivers installed
http://www.mindsensors.com/content/18-enhanced-firmware-for-nxt

5. in line 114 of the script change ur nxt name
- with nxt.locator.find(name="Bender") as b:

6. run script with "python xbox_nxt.py"
