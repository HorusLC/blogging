def dumper(obj):
    try:
        return obj.to_json()
    except AttributeError:
        return obj.__dict__


def object_hook(jsdict):
    entity_module_name = jsdict['_module']
    entity_class_name = jsdict['_class']
    module = __import__(entity_module_name, fromlist=[entity_class_name])
    cls = getattr(module, entity_class_name)
    if hasattr(cls, 'from_json'):
        return cls.from_json(jsdict)
    obj = cls()
    obj.__dict__ = jsdict
    return obj
