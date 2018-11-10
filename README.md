* running the camera app
https://blog.miguelgrinberg.com/post/how-to-build-and-run-mjpg-streamer-on-the-raspberry-pi

* cd to project
cd raspi

* start the web server
python app.py &>/dev/null &

* start the cam
raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &>/dev/null &

* start the streamer
LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i "input_file.so -f /tmp/stream -n pic.jpg" -o "output_http.so -w /usr/local/www" &

connect to http://localhost:8080 for the stream
and connect to http://localhost:5000 for the web server

* check partition size and usage
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       7.2G  5.1G  1.8G  74% /
devtmpfs        434M     0  434M   0% /dev
tmpfs           438M     0  438M   0% /dev/shm
tmpfs           438M   17M  422M   4% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           438M     0  438M   0% /sys/fs/cgroup
/dev/mmcblk0p1   41M   22M   20M  53% /boot
tmpfs            88M     0   88M   0% /run/user/1000

