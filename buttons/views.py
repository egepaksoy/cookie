from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Users
from .hasher import generate
# set SESSION: req.session["key"] = value
# delete SESSION: del req.session["key"] = value
# get SESSION: req.session["key"], req.session.get("key" or "value")
# save SESSION: req.session.modified = True
# query SESSION: req.session["key"]
# set COOKIE: res.set_cookie("key", "value")
# delete COOKIE: res.delete_cookie("key")
# get COOKIE: req.COOKIES.get("key")
# query COOKIE: if req.COOKIES.has_key("key")
# TODO: session[uname] olucak ama değeri dict olarak alıcak ve değer de {serial: token} sonrada cookie de set_cookie(serial, token) şeklinde olucak sonra seriali aricaz ve gelen değerdeki kullanıcı adı iile giriş yapılcak


def home(req):
    if req.COOKIES.get("serial"):
        if req.COOKIES.get("serial") == req.session["serial"]:
            return render(req, "home.html")
        else:
            return HttpResponse("Cookie ile session uyuşmuyor")
    else:
        return redirect("/signin")


def login(req):
    if req.method == "POST":
        res = redirect("/")
        uname = req.POST.get("uname")
        passwd = req.POST.get("passwd")
        remember = req.POST.get("remember")
        generated = generate("token", uname)
        if remember:
            req.session["serial"] = generated[0]
            res.set_cookie("serial", generated[0])
        return res
    else:
        res = render(req, "login.html")
        return res


def signup(req):
    return HttpResponse("signup page")