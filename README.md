### Django创建的表白以及照片墙，并利用uwsgi+nginx部署到远程服务器
地址：[点击直达](www.father.massacre96wj.top)

执行命令在 **mysite.sh** 文件

添加开机自启：

[^_^]: #(修改windows的dos文件为unix的，否则出现^M错误)

`sed -i -e 's/\r$//' mysite.sh `

添加开机自启命令：

在 **/etc/rc.d/rc.local** 添加：

`source /data/wwwroot/mysite/mysite.sh`


