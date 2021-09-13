from django.http import HttpResponse
from django.template import loader

from .device import get_interfaces, set_interface

# Create your views here.


def index(request):
    if request.method == "POST":
        desired_state = request.POST.dict()
        interface_to_enable = desired_state.get("enable")
        interface_to_disable = desired_state.get("disable")

        if interface_to_enable:
            set_interface(interface_to_enable, True)

        if interface_to_disable:
            set_interface(interface_to_disable, False)

    interface_list = get_interfaces()
    template = loader.get_template("interfaces/index.html")
    context = {
        "interface_list": interface_list,
    }
    return HttpResponse(template.render(context, request))
