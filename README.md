## What is Dumbleq?
Dumbleq is a dumb Subleq VM/interpreter implementation created by me for absolutely no reason at all.

### What is Subleq?
If you haven't heard about it before, basically it's the shortened version of `SUBtract and branch if Less-than or EQual to zero`. Subleq is one of the prime examples of `OISC` (or One Instruction Set Computer), which, by the name suggests, has only one instruction to do everything.

A Subleq instruction can look like this:
```
subleq A B C
```
or like this:
```
A B C
```
with A, B, C being numbers.

It works by subtracting the value from address B with the one from address A, if the result is less or equal than 0, we will move the memory pointer to address C.

If A is set to `-1`, the console will start taking input, convert it into ASCII and store it into address B.
If B is set to `-1`, the console will print out the value from memory address A as text.

## How to use Dumbleq?
In the `./src` directory, you should be able to find `dumbleq.py` which is the VM.

To run a file consisting of Subleq instructions, type:
```
python dumbleq.py ./path/to/file
```

There is a `Hello World` program written in Subleq in the `./examples` directory, check it out if you want.

## Copyrights and License
Copyrights © 2022 Nguyen Phu Minh

This project is licensed under the MIT License
