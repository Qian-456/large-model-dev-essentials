class Model:
    def __init__(self, id, created, object_type, owned_by):
        self.id = id
        self.created = created
        self.object_type = object_type
        self.owned_by = owned_by

    def to_dict(self):
        return {
            "id": self.id,
            "created": self.created,
            "object": self.object_type,
            "owned_by": self.owned_by
        }

class SyncPage:
    def __init__(self, data, object_type):
        self.data = data  # data 是一个包含多个 Model 对象的列表
        self.object_type = object_type

    def to_dict(self):
        return {
            "data": [model.to_dict() for model in self.data],
            "object": self.object_type
    
        }
sync_page = SyncPage(data=models, object_type="list")

# 将 SyncPage 对象转换为字典
sync_page_dict = sync_page.to_dict()

# 将字典转换为格式化的 JSON 字符串
j_str = json.dumps(sync_page_dict, indent=4)
print(j_str)