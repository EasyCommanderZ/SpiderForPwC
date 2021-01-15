### IP Pool

由于项目爬取的网站中有视频以及PDF的下载需求，并且由于目标网站的特殊性，项目需要同时具有**科学上网**以及**防止反爬虫**的能力。因此，本项目配合[clash](https://github.com/Dreamacro/clash) 来实现IP池，让爬虫更加高效可用。

#### 相关代码

本部分的实现在各项目中的`ClashControl.py`文件中，针对不同项目的特点有些许不同。实现了类`ClashControl`其中主要的函数有：

```python
class ClashControl:
    def getProxies(self)
    def checkProxy(self, proxyName)
    def getRandomProxy(self)
    def changeProxyByProxyName(self, proxyName)
    def changeRandomAvailableProxy(self)
```

#### 工作模式

1. 首先在本地/远程主机配置好clash，并导入代理节点信息，之后保持clash打开状态。本项目中所涉及的clash信息及配置如下：

   ```json
   clash_host = "127.0.0.1"
   controller_port = "65117"
   proxy_port = "1717"
   ```

2. 调用clash提供的RESTful AP进行代理控制，具体见代码；

3. 在项目中对应的位置加入下载和切换策略，并根据目标网站的反爬策略等进行相应的调整，保证爬虫的可用性。

#### 使用方法

在需要使用到的类中，引入`ClashControl`类并创建对象，设置http请求的代理为clash提供的代理端口，使用类中构造的函数进行爬取策略设计即可。

#### 依赖

```
Proxy Software ： clash
Python Libraries：
    random
    psutil==5.8.0
    requests==2.23.0
```

#### 分工

- 张峄天：完成IP池开发



