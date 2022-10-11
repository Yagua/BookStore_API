from django.views import View
from django.shortcuts import render
import json
import requests

class RestartUserPasswordView(View):

    def get(self, request, uid, token):
        return render(request, "reset_password.html")

    def post(self, request, uid, token):
        new_password = request.POST.get("new_password", None)
        re_new_password = request.POST.get("re_new_password", None)

        def prepare_errors(data):
            errors = []
            for error, value in data.items():
                errors.append(
                    f"[{error}]: {' - '.join(value)}"
                )
            return " || ".join(errors)

        payload = {
            "uid": uid,
            "token": token,
            "new_password": new_password,
            "re_new_password": re_new_password
        }

        protocol = "http"
        # host = request.get_host()
        host = "192.168.20.71" # test
        url = f"{protocol}://{host}:80/api/v1/auth/users/reset_password_confirm/"
        print(url)
        response = requests.post(url, data=payload)

        if response.status_code == 400:
            data = json.loads(response.content)
            return render(request, "reset_password.html", {
                "error": prepare_errors(data)
            })

        return render(request, "reset_password.html", {
            "success": "Password restored successfully."
        })
