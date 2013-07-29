### Encode

```
$ mencoder file.ts -oac copy -ovc lavc -lavcopts vcodec=mpeg4:v4mv:mbd=2:trell:cmp=3:subcmp=3:mbcmp=3:autoaspect:vpass=1 -o film.avi

$ mencoder file.ts -oac copy -ovc lavc -lavcopts vcodec=mpeg4:v4mv:mbd=2:trell:cmp=3:subcmp=3:mbcmp=3:autoaspect:vpass=2 -o film.avi
```

### Resize

```
$ mencoder Ibiza-France5.avi -oac copy -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:trell -vf scale=640:360 -o Ibiza-France5-small.avi
```
