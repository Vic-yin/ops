##服务器测试环境要求
CentOS-7.7-x86_64-Minimal-1908.iso
2C/2G/30GB

#运行命令安装pip3
$yum search python38-pip*
$yum install python38-pip* -y 

#安装依赖
yum install gcc* -y
yum install dbus-python-devel.x86_64 gstreamer-python-devel.x86_64 python-devel.x86_64 -y


#Python虚拟环境配置
$pip3 install virtualenv
$mkdir -p /opt/my_wwwroot
$cd /opt/my_wwwroot
$virtualenv myappenv

#激活虚拟环境
source myappenv/bin/activate
#成功激活之后如下提示:
(myappenv) [root@localhost my_wwwroot]
#在虚拟环境下安装uwsgi
(myappenv) [root@localhost my_wwwroot] pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple uwsgi

#配置启动(注意: 启动在虚拟环境下)
(myappenv) [root@localhost my_wwwroot]  uwsgi --ini /etc/shop.ini &    #第一步启动uwsgi服务
(myappenv) [root@localhost my_wwwroot]  /usr/local/nginx/sbin/nginx           #第二步启动Nginx代理服务

#修改Centos7默认Python的软件源管理工具pip工具链仓库为国内清华源库(如果你上述pip安装失败的话,先修改这个配置然后重新pip来安装一遍)
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple    --修改
pip install pip -U  ---版本升级
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U   ---临时使用(指的是 没有config set情况下会用到)