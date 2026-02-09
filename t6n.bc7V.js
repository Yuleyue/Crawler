t6n.bc7V = function(W7P, e6c) {
        var i6c = {}
          , e6c = NEJ.X({}, e6c)
          , mf9W = W7P.indexOf("?");
        if (window.GEnc && /(^|\.com)\/api/.test(W7P) && !(e6c.headers && e6c.headers[ev8n.zR2x] == ev8n.Ho5t) && !e6c.noEnc) {
            if (mf9W != -1) {
                i6c = j6d.gV8N(W7P.substring(mf9W + 1));
                W7P = W7P.substring(0, mf9W)
            }
            if (e6c.query) {
                i6c = NEJ.X(i6c, j6d.fP8H(e6c.query) ? j6d.gV8N(e6c.query) : e6c.query)
            }
            if (e6c.data) {
                i6c = NEJ.X(i6c, j6d.fP8H(e6c.data) ? j6d.gV8N(e6c.data) : e6c.data)
            }
            i6c["csrf_token"] = t6n.gM8E("__csrf");
            W7P = W7P.replace("api", "weapi");
            e6c.method = "post";
            delete e6c.query;
            var bWo2x = window.asrsea(JSON.stringify(i6c), bod1x(["流泪", "强"]), bod1x(AY2x.md), bod1x(["爱心", "女孩", "惊恐", "大笑"]));
            e6c.data = j6d.cq7j({
                params: bWo2x.encText,
                encSecKey: bWo2x.encSecKey
            })
        }
        var cdnHost = "y.music.163.com";
        var apiHost = "interface.music.163.com";
        if (location.host === cdnHost) {
            W7P = W7P.replace(cdnHost, apiHost);
            if (W7P.match(/^\/(we)?api/)) {
                W7P = "//" + apiHost + W7P
            }
            e6c.cookie = true
        }
        if (e6c.ClientLogDomainSwitch !== false && (W7P.indexOf("/weapi/feedback/weblog") > -1 || W7P.indexOf("/api/feedback/weblog") > -1)) {
            W7P = W7P.replace(/music\.163\.com|qa\.igame\.163\.com/g, "clientlogusf.music.163.com");
            W7P = W7P + "?csrf_token=" + t6n.gM8E("__csrf")
        }
        cwq5v(W7P, e6c)
    }