word-click-captcha
==============================

## Pull Darknet docker image
---------------------------------
```
docker pull loretoparisi/darknet
```


##  Start a docker container and mount current working directory into it
```
docker run --rm -it -v $(pwd):/root/darknet/project --name darknet loretoparisi/darknet bash
```

## download pretrained model weight
```
wget https://pjreddie.com/media/files/darknet19_448.conv.23 ./models/darknet19_448.conv.23
```

## Start training process
```
cd /darknet/project

../darknet detector train config/obj.data config/tiny-yolo-obj.cfg models/darknet19_448.conv.23
```

## test model
```
../darknet detector test config/obj.data config/tiny-yolo-obj.cfg backup/tiny-yolo-onj.backup data/labels/test/0000t1.jpg
```