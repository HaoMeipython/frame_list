from zspider.core.engine import Engine
from baiduspider import Baiduspider
from tiebaspider import Tiebaspider

if __name__ == '__main__':
    baidu=Baiduspider()
    tb=Tiebaspider()
    engine=Engine(tb)
    engine.start_engine()