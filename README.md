rpm-dashing
===========

RPM Build of [Shopify Dashing](http://dashing.io) utilizing the [CentOS SCL ruby193](http://wiki.centos.org/AdditionalResources/Repositories/SCL) and EPEL nginx

Installation
---------------------

**Install epel-release**

`yum install http://mirrors.kernel.org/fedora-epel/6/i386/epel-release-6-8.noarch.rpm`

**Install SCL repo**

`yum install centos-release-SCL`


**Install dashing RPM** (and this will install a few dependencies)

`yum install dashing-1.3.2-1.el6.x86_64.rpm`

**Remove default nginx config**

`rm /etc/nginx/conf.d/default.conf`

**Start dashing/thin webserver**

`/etc/init.d/dashing start`

**Start nginx**

`/etc/init.d/nginx start`


**Open port 80**

`iptables -A INPUT -i eth0 -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT`


****

### Check functionality of sample dashboard

<http://$SERVER/sample>

Should be similar to:
![sample]
[sample]: http://i.imgur.com/Pok4ygI.png


****

Config Tweaks
---------------------
- edit `/opt/dashing/config.ru` and set the 'auth_token' value
- add additional *dashboards/jobs/widgets*


