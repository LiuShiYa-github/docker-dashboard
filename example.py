#!/usr/bin/python3
# -*- coding: utf-8 -*-
import docker

client = docker.DockerClient(base_url='tcp://10.0.0.30:2375')

"""
获取docker信息
"""
# print(client.info())
# print(client.version())
# print(client.ping())
# print(client.df())
# print(client.events())
for event in client.events(decode=True):
    print(event)
client.events().close()

"""
获取容器信息
好像无法获取创建时间以及运行时间
"""
# for container in client.containers.list(all=True):
#     print(container.short_id)
#     print(container.image)
#     print(container.status)
#     print(container.ports)
#     print(container.name)

"""
创建容器
"""
# container = client.containers.run(image='nginx', detach=True)
# # print(container.logs(follow=True))
# print(container.logs())

"""
删除停止的容器
"""
# container = client.containers.run(image='nginx', detach=True)
# # print(container.logs())
# container.exec_run(cmd="sleep 100", tty=True, stdin=True, )
# container.resize(height=100, width=100)
# # container.rename('nginx')
# # container.restart()
# print(container.stats(stream=False))
# print(container.top())
# container.stop()
# container.remove()


"""
镜像操作
"""
# print(client.images.list())
# client.images.pull(repository="mysql", tag="5.7")
# client.images.remove("mysql")
# print(client.images.search(term="mysql"))
