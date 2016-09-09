from feature_request import run_app, init_app

app = init_app('production')
run_app(app, '0.0.0.0', 5000)
