run app.py webserver to serve html.

run all microservices in services - eg.:
* webserver on :5000
* light services on :5001
* chart services on :5002
* os services on :5003
* stream services on :8080

* running the camera app:
https://blog.miguelgrinberg.com/post/how-to-build-and-run-mjpg-streamer-on-the-raspberry-pi

* start the cam:
raspistill --nopreview -w 640 -h 480 -q 50 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &>/dev/null &

* start the streamer:
LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i "input_file.so -f /tmp/stream -n pic.jpg -delay 0.1" -o "output_http.so -w /usr/local/www" &

