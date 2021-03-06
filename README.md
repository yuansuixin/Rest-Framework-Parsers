

# 解析器

### 1. 知识点补充，Django的解析

- Django的请求体解析：request.POST/ request.body
    1. 请求头的要求：如果请求头中的``Content-Type: application/x-www-form-urlencoded``，  PS: 如果请求头中的 ``Content-Type: application/x-www-form-urlencoded``，request.POST中才有值（去request.body中解析数据）。
    2. 数据格式要求：`` name=alex&age=18&gender=男
        ``
    如：
        - form表单提交，``<form method=...></form>``,默认的格式就是要求的那种格式
        - ajax提交, 
        1. 提交的是字典格式的数据，但是内部会默认的给我们转换成&连接的格式
        ```
        $.ajax({
        url:...,
        type:POST,
        data:{name:alex,age=18},
        })
        ```
        2. ajax自己定义请求头,body里有值，POST里没有值
        ```
        $.ajax({
        url:...,
        headers:{'Content-Type':'application/json'},
        type:POST,
        data:{name:alex,age=18},
        })
        ```
        3. 请求头改变了，数据格式也改变了，body有值，POST没有值，这种情况，就需要将字符转换成字符串格式，然后``json.loads(request.body)``，可以直接拿到字典
        ```
        $.ajax({
        url:...,
        headers:{'Content-Type':'application/json'},
        type:POST,
        data:JSON.stringfy({name:alex,age=18},
        }))
        ```


### 2.rest framework的解析器，对请求体数据进行解析
- 使用，原理和认证，权限等组件相似，推荐使用全局配置


- 源码流程 和 本质
    - 本质
	    - 根据请求头content-type的不同，让解析器去处理，解析器拿请求体做转换
	- 源码流程
	     - 匹配到url，然后到view视图里，执行父类的as_view()方法，该方法返回一个view函数，而在view（）函数里返回的是dispatch（）方法，我们就从dispatch()方法开始
		 - 先封装request，执行initialize_request()对request进行加工，其中封装了一个get_parsers（），就是将解释器封装到了request里，这个方法返回的是对象列表。
		 - 这个对象列表默认是通过配置里的设置拿到的，当然也可以在视图里写入parser_classes这个列表
		 - 这样将解释器封装到了request里面
		 - 然后，请求的时候，从url匹配到视图，视图里如果使用到了request的相关的内容，以request.data为例，使用到的时候，才触发解释器，
		 - 源码中就会到达request类中的data（），因为data（）是由装饰器property修饰，所以调用的时候不需要加括号，data（）里调用了_load_data_and_files（），这面通过_parse（）方法拿到的值，
		 - 在_parse（）中，可以获取到用户提交的请求头self.content-type,然后
		 ![](index_files/778990015.png)
		 
		 - 选择好解析器之后，就到了对应的解析器里面的parser()方法对数据进行解析


[详细解析](https://yuansuixin.github.io/2018/03/11/rest-framework-parsers/ "详细解析")


