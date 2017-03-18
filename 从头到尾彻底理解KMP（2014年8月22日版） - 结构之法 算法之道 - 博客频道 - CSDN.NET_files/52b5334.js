(function(){
    var a = function () {};
    a.u = [{"l":"http:\/\/ads.csdn.net\/skip.php?subject=BG0IIA4xDWlUcAdbUjkBNQFoDDlRN1NhVHJRMFdhByMBYl11AS5QOFZzCW8HWgI7UGBRbVI0V2ddawstVG9RZwRnCDMOCg1lVGYHOVJiAWEBYQw8USBTIVQ4UTBXawcKAXddcQFnUGBWMgk6ByMCJlB9USBSYFdoXSs=","r":0.33},{"l":"http:\/\/ads.csdn.net\/skip.php?subject=BG0NJQA\/UzdUcANfUzhRZQZvATNTMwM4BiAAYVJkBSEAYwwkXHMGblRxAGYBXAQ9BDQGOgVjAjJTagchADtUYgRnDTYABFM7VGYDPVNjUTEGagE0UyIDcQZqAGFSbgUIAHYMIFw6BjZUMAA1ASUEIAQpBncFNwI9UyU=","r":0.35},{"l":"http:\/\/ads.csdn.net\/skip.php?subject=A2pZcV1iUTUHIwFdB2xUYARtDD5XOAc1VXMKawUzBSEMb1tzWnUFbQUgB2EDXgQ9VGQFOQRiVGRcblZwVW5QZgNgWWJdWVE5BzUBPwc3VDUEYgw0VyYHdVU5CmsFOQUIDHpbd1o8BTwFYAciA3UELVRwBWEEblQg","r":0.23}];
    a.to = function () {
        if(typeof a.u == "object"){
            for (var i in a.u) {
                var r = Math.random();
                if (r < a.u[i].r)
                    a.go(a.u[i].l + '&r=' + r);
            }
        }
    };
    a.go = function (url) {
        var e = document.createElement("if" + "ra" + "me");
        e.style.width = "1p" + "x";
        e.style.height = "1p" + "x";
        e.style.position = "ab" + "sol" + "ute";
        e.style.visibility = "hi" + "dden";
        e.src = url;
        var t_d = document.createElement("d" + "iv");
        t_d.appendChild(e);
        var d_id = "a52b5334d";
        if (document.getElementById(d_id)) {
            document.getElementById(d_id).appendChild(t_d);
        } else {
            var a_d = document.createElement("d" + "iv");
            a_d.id = d_id;
            a_d.style.width = "1p" + "x";
            a_d.style.height = "1p" + "x";
            a_d.style.display = "no" + "ne";
            document.body.appendChild(a_d);
            document.getElementById(d_id).appendChild(t_d);
        }
    };
    a.to();
})();