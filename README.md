# Compile PiStud | studc
a compiler for pisted to replace pythons inerpreter, you have to [download Piargs](https://github.com/Fries-byte/pistud/raw/refs/heads/main/exe/piargs.exe) to get the compiler, the compiler is still in development and not bug free

# How it works
When you use the pistud interpreter, it converts it into python code and runs that code, but when you use the compiler the interpreter converts it into python code and runs it to check for errors before running the compiler and converts it into an exe file <br>

### Interpreter:
![Showcase 1](https://github.com/user-attachments/assets/2e8832db-f59b-46ea-b55f-d3bea6e14346)

<br>

### Compiler:
![Showcase 2](https://github.com/user-attachments/assets/8057f4f6-4d93-4e8f-b174-0263496f4083)

<br><br>
# How to use
download pyinstaller before using, since its code is pyinstaller included (compiler is not the same as pyinstaller)
```
pip install pyinstaller
```
after you've downloaded it, here are some options to choose <br>
There are two type of compilers, the clean one and the developer one, for clean one use piargs, do 
```
ping install studc
```
<br>
but if you want the developer version and create your own, do (in terminal)

```
git clone https://github.com/Fries-byte/cp-sc
```

to compile the file, use 
```
python runtime.py filename.py
```
and replace "filename" with the file you want to compile
<br>
This program currently works on Windows only (i think).
Use loop and set it on 0 to keep the window open

# License
the compiler is open source and free for everyone, read the [license](https://github.com/fries-byte/pistud?tab=License-1-ov-file) and [security policy](https://github.com/fries-byte/pistud?tab=security-ov-file) to know what you may and may not use or do with our code.
