项目模板
=======

> 还没在生产环境使用过, 生产环境配置尚不成熟

根据 `cookiecutter-django-rest` 改造, 适合自己的一个Rest项目模板

# 使用

```
pip install cookiecutter
cookiecutter gh:daimon99/cookiecutter-django-rest
```

# 相比原版, 依赖组件方面有如下调整。

## 优化

* django-configurations 用 django-environ 代替

## 增加

* django-crispy-forms (改进restframework web 界面字段显示效果)
* oss2 ( ALIYUN OSS SDK )
* django-aliyun-oss2-storage ( ALIYUN django 组件 )
* django-rest-swagger (django rest 文档展示改进)
* django-import-export ( django import / export 组件 )
* wechatpy[cryptography] ( 微信开发库与加解密库 )
* django-extensions (有加密字段，以及其它很多很好的辅助类）
* django-kronos (非常好的定时任务库）

## 删除

* 暂无

# 使用中注意

* 使用 django-environ 管理配置

提供了参考配置文件 `.env.sample`。
您应该copy该文件, 在项目根目录下创建 `.env` 来管理自己的配置。

* 默认配置不发邮件

在django异常时, 不发邮件, 而是把邮件放在 logs 目录中。

* 重构了bin下的服务安装、 启动、 停止、 状态查询的脚本（适用于测试环境的）

* 时区调整为了北京时间

* 记录数据库访问日志（注意生产环境要禁掉DEBUG）

* 运行`python manage.py test app`时, 不创建数据库, 保留数据库数据(请自己注意删除测试数据)

* bin脚本区分三个环境, 分别在不同端口运行。(tst/qa/prd)

原版说明
=======

# cookiecutter-django-rest
[![Build Status](https://travis-ci.org/agconti/cookiecutter-django-rest.svg?branch=docs-project-readme-travis)](https://travis-ci.org/agconti/cookiecutter-django-rest)
[![Updates](https://pyup.io/repos/github/agconti/cookiecutter-django-rest/shield.svg)](https://pyup.io/repos/github/agconti/cookiecutter-django-rest/)

For creating REST apis for mobile and web applications.

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Features](#features)
- [Contributing](#contributing)

## Overview
This cookiecutter template takes care of the setup and configuration so you can focus on making your api awesome. Scaffolding a project takes seconds and it gives you authentication, user accounts, and the docs and tests to support them. After that, just add your own resources to the api and start shipping.

This project gives you a solid foundation for your api to mature by baking in things like asynchronous queueing, image optimization, and application monitoring.

### What you'll be building

![ia diagram](https://cdn.rawgit.com/agconti/cookiecutter-django-rest/master/media/ia-diagram.svg)

## Quick Start

Install [cookiecutter](https://github.com/audreyr/cookiecutter):
```bash
pip install cookiecutter
```

Scaffold your project:
```
cookiecutter gh:agconti/cookiecutter-django-rest
```

![Scaffolding](media/scaffolding.gif)

Example of the result: https://github.com/agconti/piedpiper-web

## Features

- Django 1.9+
- PostgreSQL
- Complete [Django Rest Framework](http://www.django-rest-framework.org/) integration
- Configured for deploying to [Heroku](https://www.heroku.com)
- Asset storage via [S3](https://github.com/jschneier/django-storages)
- Class based settings and safe environmental variable management via [django-configurations](https://github.com/jazzband/django-configurations)
- [Travis](https://travis-ci.org/) config
- Monitoring with [New Relic](http://newrelic.com/)
- [Token authentication](http://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)
- Docs with [mkdocs](http://www.mkdocs.org/)
- Testing with [django-nose](https://github.com/django-nose/django-nose) and fixtures via [factory-boy](http://factoryboy.readthedocs.org/en/latest/orms.html)
- Caching with Redis via [Django Redis](https://github.com/niwinz/django-redis)
- Easy debugging with [ipython](http://ipython.org/) and [ipdb](https://pypi.python.org/pypi/ipdb)
- Style Enforcement via [flake8](https://flake8.readthedocs.org/en/2.3.0/)
- Fabfile for easily setting up servers

## Contributing
Want a new feature? Open an issue and let's chat!
Find a bug? Submit a Pull Request!

This project adheres to the [Contributor Code of Conduct](.github/CONTRIBUTING.md).
