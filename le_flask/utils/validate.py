from le_flask.utils.messages import Error
import os


def attr(request, attr):
    all_attr = {}
    for current_attr in attr:
        if not current_attr in request.args:
            print(current_attr)
            print(request.args)
            raise Error("ERROR")
        else:
            all_attr = all_attr | {
                current_attr: request.args.get(current_attr)}
    return all_attr
