import datetime
import os
import platform

import psutil
import uptime
from flask import Flask, request

app = Flask(__name__)

WEB_PING_VERSION = '1.3.5'


@app.route('/')
@app.route('/ping')
def ping():
    return "pong\n"


@app.route('/healthcheck')
def healthcheck():
    return {
        'host_name': _get_pod_name() or platform.node(),
        'date_time': datetime.datetime.now()
    }


@app.route('/info')
def get_info():
    data = {
        'app_version': WEB_PING_VERSION,
        'date_time': datetime.datetime.now(),
        'machine': {
            'host_name': platform.node(),
            'boot_time': '{}'.format(uptime.boottime()),
            'up_time': '{}'.format(datetime.timedelta(seconds=uptime.uptime())),
            'architecture': platform.architecture()[0],
            'cpu': _get_cpus(),
            'memory': _get_mem(),
        },
        'OS': {
            'platform': platform.platform(),
            'version': platform.version()
        },
        'kubernetes': {
            'pod_name': _get_pod_name() or 'N/A'
        },
        'client': {
            # 'ip': get_client_ip(),
            'REMOTE_ADDR': request.environ.get('REMOTE_ADDR'),
            'HTTP_X_REAL_IP': request.environ.get('HTTP_X_REAL_IP'),
            'HTTP_X_FORWARDED_FOR': request.environ.get('HTTP_X_FORWARDED_FOR')
        }
    }
    return data


def get_client_ip():
    # return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    return request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)


# @app.route('/log')
# def log(rows_number=20):
#     data = get_log(rows_number)
#     return _render_list(data)


# def _render_list(data):
#     return "\n".join([json.dumps(d) for d in data])


# def _write_log_to_db():
#     conn = psycopg2.connect(
#         host="localhost",
#         database="suppliers",
#         user="postgres",
#         password="Abcd1234")
#     return


def _get_mem():
    vm = psutil.virtual_memory()
    return {
        'total': '{} GB'.format(round(vm.total / (1024 ** 3))),
        'used': '{} GB'.format(round(vm.used / (1024 ** 3))),
    }


def _get_cpus():
    cpu_freq = psutil.cpu_freq()
    core_usage = []
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        core_usage.append('{}: {}%'.format(i, percentage))

    return {
        'total_cores': psutil.cpu_count(logical=True),
        'physical cores': psutil.cpu_count(logical=False),
        'frequency': {
            'current': round(cpu_freq.current),
            'min': cpu_freq.min,
            'max': cpu_freq.max,
        },
        'total_usage': psutil.cpu_percent(),
        'cores_usage': core_usage
    }


def _get_pod_name():
    """Get the current pod name."""
    return os.getenv("HOSTNAME")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run('0.0.0.0', port)
