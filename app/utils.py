from flask import jsonify


#Подразумевается, что определен перечень возвращаемых микросервисом статус-кодов
SUCCESS_STATUS_CODE = [200, 201]
ERROR_STATUS_CODE = [400, 404, 500]


def response_handler(metainfo, status_code):
    status = "Success" if status_code in SUCCESS_STATUS_CODE else "Error"
    return jsonify({"status": status, "details": metainfo}), status_code
