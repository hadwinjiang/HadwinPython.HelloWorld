def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))


tag('img', src="Monet.jpg", alt="Sunrise by Claude Monet", border=1)
# img
# {'src': 'Monet.jpg', 'alt': 'Sunrise by Claude Monet', 'border': 1}
# <class 'dict'>


def tag_01(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result


tag_01('img', src="Monet.jpg", alt="Sunrise by Claude Monet", border=1)

