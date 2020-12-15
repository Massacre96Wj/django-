#!/bin/sh
#chkconfig: 2345 90 10
#description:auto_run

source /data/env/pyweb/bin/activate &&
echo "进入python-django环境"
uwsgi -x /data/wwwroot/mysite/mysite.xml &&
echo "项目启动成功"
/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf &&
echo "Nginx启动成功，欢迎访问"