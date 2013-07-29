```
source ./vars
./clean-all
./build-dh     -> takes a long time, consider backgrounding
./pkitool --initca
./pkitool --server myserver
./pkitool client1
./pkitool --pass client
```
Typical usage for adding client cert to existing PKI:
```
source ./vars
./pkitool client-new
```
