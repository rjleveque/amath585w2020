# rsyncs all files in _build/html to the repository used to
# display on the web

rsync -azv _build/html/ rjl@homer.u.washington.edu:public_html/classes/am585w2020/
