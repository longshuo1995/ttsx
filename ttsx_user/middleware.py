class UrlPathMiddelware:

    def process_request(self, request):
        path = request.path
        print(path)
        if request.path not in['/user/register/',
                               '/user/login/',
                               '/user/register_handle/',
                               '/user/login_handle/',
                               '/favicon.ico',
                               '/user/invalidate_username/',
                                '/user/logout/',
                           ]:
            request.session['url_path'] = path
            print('真正的url:'+path)
