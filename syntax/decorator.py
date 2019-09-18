# 装饰器：本质是一个Python函数，它可以让其他函数在不需要做任何代码改动的前提下增加额外功能。装饰器的返回值也是一个函数对象。
# 它经常用于有切面需求的场景，比如：插入日志、性能测试事务处理、缓存、权限效验等场景。
# 有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。装饰器的作用就是为已经存在的对象添加额外的功能。


def bar():
    print('i am bar')


# 给bar()函数增加日志功能
# 普通实现：
def use_logging(func):
    print("%s is running" % func.__name__)
    func()


# 简单装饰器：
def _use_logging(func):
    def wrapper(*args,**kwargs):
        print("%s is running" % func.__name__)
        return func(*args,**kwargs)
    return wrapper


if __name__ == "__main__":
    # 缺点：改变了原有的代码逻辑结构。 原来执行bar(),现在改成use_logging(bar)
    print("=" * 45)
    use_logging(bar)


    # use_logging就是装饰器，把执行真正业务方法的func包裹在函数里面
    bar = _use_logging(bar)
    print("=" * 45)
    bar()


    # @语法糖：在定义函数的时候使用，避免再一次赋值操作，省去bar=use_logging(bar)
    @_use_logging
    def bar():
        print('i am bar')


    print("=" * 45)
    bar()