#!/usr/bin/env python
# coding: utf-8

__author__ = 'yueyt'

from sanic import Sanic
from sanic.response import json

main = Sanic(__name__)


@main.route('/interface')
async def interface(request):
    return json({"received": True, "message": request.json})


if __name__ == '__main__':
    main.run()
