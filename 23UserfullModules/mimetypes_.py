#!/usr/bin/env python
# -*-coding:utf-8 -*-

import mimetypes

"""
MIME(Multipurpose Internet Mail Extensions, 多用途互联网邮件扩展)

Content-Type: text/plain; charset="UTF-8"
表明信息的类型，缺省值为"text/plain"，主要类型/次要类型，主要类型有九种
    application、audio、example、image、message、model、multipart、text、video
    
如果信息的主要类型是"text"，那么还必须指明编码类型"charset"，缺省值是ASCII
"""