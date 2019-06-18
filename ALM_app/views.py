import json
import logging
from django.shortcuts import HttpResponse

from ALM_app.etc import reqProtocolConf

# Create your views here.

# init log default config

logger = logging.getLogger(__name__)


# views
def index(request):
    """
    POST:
        json type：
        {
            "reqmethod": "struct",
            "reqdata": []
        }
    GET:
        http://localhost:8000/ALM_service/?reqmethod=func1&reqdata=[]
    """

    # ------------------------------------------------------------------------------------------------------------------
    # Init local protocol
    # ------------------------------------------------------------------------------------------------------------------
    # Get keys in local protocol configurations：
    #   the key name of function called field defined by service protocol: "reqmethod"
    service_call_func_key = reqProtocolConf.reqJson_MapKeys[reqProtocolConf.Request_CallProcessFunction]
    # Get keys in local protocol configurations：
    #   the key name of submitting data field defined by service protocol: "reqdata"
    service_submit_data_key = reqProtocolConf.reqJson_MapKeys[reqProtocolConf.Request_SubmitData]
    supported_functions_dict = reqProtocolConf.reqJson_SupportFunctions

    # ------------------------------------------------------------------------------------------------------------------
    # Validate the format of request data
    # ------------------------------------------------------------------------------------------------------------------
    # Init parameters
    req_format_valid_flag = False
    req_method_value = None
    req_data_value = None

    # get req_method_value, req_data_value
    if request.method == 'GET':
        req_method_value = request.GET.get(service_call_func_key, None)
        req_data_value = request.GET.get(service_submit_data_key, None)
        if req_method_value and req_data_value:
            req_format_valid_flag = True
    elif request.method == 'POST':
        post_body = request.body
        try:
            post_body_loaded = json.loads(post_body)
        except BaseException as e:
            logger.info("JSON load error：", e)
            return HttpResponse(None)
        if type(post_body_loaded) == dict:
            if service_call_func_key in post_body_loaded.keys() and service_submit_data_key in post_body_loaded.keys():
                req_method_value = str(post_body_loaded[service_call_func_key])
                req_data_value = json.dumps(post_body_loaded[service_submit_data_key], ensure_ascii=False)
                if req_method_value and req_data_value:
                    req_format_valid_flag = True
    else:
        pass

    # Validate the format and component of request data
    if not (req_format_valid_flag and req_method_value and req_data_value):
        return HttpResponse(None)

    # Task distribution
    if req_method_value.strip() == supported_functions_dict[reqProtocolConf.func1]:
        resp_str = func1(req_data_value)
    elif req_method_value.strip() == supported_functions_dict[reqProtocolConf.func2]:
        resp_str = func2(req_data_value)
    else:
        resp_str = None
    return HttpResponse(resp_str, content_type='application/json')


def func1(req_data_value):
    return 1


def func2(req_data_value):
    return 2
