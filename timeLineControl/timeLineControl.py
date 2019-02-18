# -*- coding:utf-8 -*-


class TimeLineControl(object):
    def __init__(self):
        self.version = '0.1'

    def find_shot(self,eps_num,shot_num):
        # 根据提供的集数和镜头号，打开对应的剪辑序列并且把时间针移动到该镜头的第一帧
        pass

    def import_check_shots(self,check_dict):
        # 根据给定的待检查信息(dict),将对应镜头的最新版本导入相应时间线的对应位置
        # 注意：有上一版本的，需要在last_version轨道上放入上一版本的素材
        # 注意判断时间线的对应位置是否有上一次检查留下的素材(对比版本做相应处理)
        pass

    def clear_old_version(self,submit_dict):
        # submit_dict是检查完发送到CGTW的镜头信息
        # 清除submit_dict中的包含镜头上一个版本还老的素材(为了让文件不卡)
        print('hello~')
        pass
