curl -D /var/folders/x_/_0vldf4d5kz_s_zcbrsff9h80000gn/T/x-cmd-x-bash-std-http-header.___X_BASH_HTTP__HTTP_DEFAULT
-X POST  -H "Content-Type: application/jsonn"
-o /var/folders/x_/_0vldf4d5kz_s_zcbrsff9h80000gn/T/x-cmd-x-bash-std-http-body.___X_BASH_HTTP__HTTP_DEFAULT
-w %{http_code} -d @/var/folders/x_/_0vldf4d5kz_s_zcbrsff9h80000gn/T/tmp.02YHUUXTTW https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=b67b4fa1-e323-4f11-a37e-a0179115abe2 1 > /var/folders/x_/_0vldf4d5kz_s_zcbrsff9h80000gn/T/x-cmd-x-bash-std-http-status.___X_BASH_HTTP__HTTP_DEFAULT 2>/dev/null

curl -D /tmp/x-cmd-x-bash-std-http-header.___X_BASH_HTTP__HTTP_DEFAULT
-X POST  -H "Content-Type: application/json"
-o /tmp/x-cmd-x-bash-std-http-body.___X_BASH_HTTP__HTTP_DEFAULT
-w %{http_code} -d @/tmp/tmp.LegXqaT5iS n/"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=b67b4fa1-e323-4f11-a37e-a0179115abe2" 1 > /tmp/x-cmd-x-bash-std-http-status.___X_BASH_HTTP__HTTP_DEFAULT 2>/dev/null

- D|http: Response Header is: HTTP/2 200
date: Fri, 28 Jun 2024 02:10:08 GMT
content-type: application/json; charset=UTF-8
content-length: 27
server: nginx
error-code: 0
error-msg: ok
x-w-no: 4

x:warn
t='tt' eval "echo \"t"\"