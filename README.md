# taher-eljamal

taher eljamal encryption algorithm\


## usage: 
```
$ python3 cli.py encrypt -f "inputfile" -o "outputfile"
```

```
$ python3 cli.py decrypt -f "inputfile" -o outputfile -k private_key
```
private key is required for decryption. \
you can try ``` -m ```to decrypt or encrypt a message. \

## Issues:
- Don't try ``` -f ``` and  ```-m ``` together, its just show you an beautifull error. \ 
- non english charachters are not fully supported. \
- its too hard and slow to genereate 'g' for big prime numbers. \
<br>

i will take care of it later ("LATER MEANS NEVER").
the code is the mess right now.